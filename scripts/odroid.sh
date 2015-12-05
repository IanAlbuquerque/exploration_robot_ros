
source $(pwd)/scripts/set_env.sh
echo "Launching odroid machine"
roslaunch odroid_machine remote_zumy.launch mname:=$zumyXY
