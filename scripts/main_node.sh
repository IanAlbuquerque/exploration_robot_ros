
source $(pwd)/scripts/set_env.sh
echo "Launching main node"
roslaunch main main_node.launch zumy_name:=$zumyXY base_ar:=$base_ar zumy_ar:=$zumy_ar origin_ar:=$origin_ar end_ar:=$end_ar discretization_x:=$discretization_x discretization_y:=$discretization_y
