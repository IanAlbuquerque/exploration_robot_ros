
source $(pwd)/scripts/set_env.sh
echo "Launching main node"
roslaunch brain brain.launch discretization_x:=$discretization_x discretization_y:=$discretization_y
