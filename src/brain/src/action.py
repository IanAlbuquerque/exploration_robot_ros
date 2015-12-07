NUMBER_OF_ACTIONS = 4
FOWARD = 0
RIGHT = 1
BACKWARD = 2
LEFT = 3
ACTIONS = [FOWARD,RIGHT,BACKWARD,LEFT]

def reverse(action):
	if action not in ACTIONS:
		raise ValueError("Action given does not exist.")
	return (action + 2) % NUMBER_OF_ACTIONS