import vector
import math
import game
import action
import hero
import direction

import time

import heapq

def manhattanDistance(p,q):
	if not isinstance(p,vector.Vector):
		raise ValueError("Variable is not a Vector.")
	if not isinstance(q,vector.Vector):
		raise ValueError("Variable is not a Vector.")

	return math.fabs(p.x - q.x) + math.fabs(p.y - q.y)

def solveGameGradientDescending(game_to_solve,max_steps = 1000):
	if not isinstance(game_to_solve,game.Game):
		raise ValueError("Variable is not a Game.")

	def functionToMinimize(game_to_solve,hero_state):
		goal_position = game_to_solve.getGoalPosition()
		return manhattanDistance(hero_state.getPosition(),goal_position)

	goal_position = game_to_solve.getGoalPosition()
	hero_state = game_to_solve.getHero().copy()

	actions_to_take = []

	steps = 0
	while True:
		steps += 1

		min_dist = float("inf")
		best_action = None
		for act in action.ACTIONS:
			next_hero_state = game_to_solve.transitionModel(hero_state,act)
			dist = functionToMinimize(game_to_solve,next_hero_state)
			if dist < min_dist:
				min_dist = dist
				best_action = act

		hero_state = game_to_solve.transitionModel(hero_state,best_action)
		actions_to_take.append(best_action)

		print "--"
		print goal_position
		print hero_state.getPosition()

		if goal_position == hero_state.getPosition() or steps > max_steps:
			break

	return actions_to_take

def solveAStar(game_to_solve):
	if not isinstance(game_to_solve,game.Game):
		raise ValueError("Variable is not a Game.")

	def heuristic(game_to_solve,hero_state):
		goal_position = game_to_solve.getGoalPosition()
		return manhattanDistance(hero_state.getPosition(),goal_position)

	goal_position = game_to_solve.getGoalPosition()
	hero_start_state = game_to_solve.getHero().copy()

	heap = [(heuristic(game_to_solve,hero_start_state),hero_start_state,None,None)]

	HEAP_HEURISTIC = 0
	HEAP_STATE = 1
	HEAP_ACTION_TAKEN_THERE = 2
	HEAP_FATHER_STATE = 3

	visited = []
	recover_map = {}

	RECOVER_ACTION = 0
	RECOVER_FATHER = 1

	ACTIONS_COST = 1

	while True:
		heap_element = heapq.heappop(heap)
		while heap_element[HEAP_STATE] in visited:
			if len(heap) == 0:
				return []
			heap_element = heapq.heappop(heap)
		visited.append(heap_element[HEAP_STATE])
		recover_map[heap_element[HEAP_STATE]] = (heap_element[HEAP_ACTION_TAKEN_THERE], heap_element[HEAP_FATHER_STATE])

		if goal_position == heap_element[HEAP_STATE].getPosition():
			recover_map[hero_start_state] = None

			actions = []

			state_tuple = heap_element[HEAP_STATE]
			recover = recover_map[state_tuple]

			while recover != None:
				actions.append(recover[RECOVER_ACTION])
				new_state = recover[RECOVER_FATHER]
				state_tuple = new_state
				recover = recover_map[state_tuple]

			actions.reverse()
			return actions


		actions_possible = action.ACTIONS
		for act in actions_possible:
			next_state = game_to_solve.transitionModel(heap_element[HEAP_STATE], act)   
			heapq.heappush(heap, (heap_element[0] + ACTIONS_COST + heuristic(game_to_solve,next_state) - heuristic(game_to_solve,heap_element[HEAP_STATE]), next_state, act, heap_element[HEAP_STATE]))


