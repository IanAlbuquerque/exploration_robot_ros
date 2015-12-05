
# zumyXY='zumy1d'

# export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/scratch/shared:~/final_proj

# source /home/cc/ee106a/fa15/class/ee106a-bc/final_proj/devel/setup.bash

# export ROS_HOSTNAME=$(hostname --short).local
# export ROS_MASTER_URI=http://$(hostname --short).local:11311
# export ROSLAUNCH_SSH_UNKNOWN=1
# echo "names set"


# roslaunch odroid_machine remote_zumy.launch mname:=$zumyXY
#roslaunch main main_node.launch zumy_name:=$zumyXY base_ar:=1 zumy_ar:=2
###roslaunch zumy_teleop zumy_teleop.launch mname:=zumyXY

gnome-terminal --title=odroid -e scripts/odroid.sh
sleep 6s
gnome-terminal --title=main_node -e scripts/main_node.sh
sleep 5s
gnome-terminal --title=homography -e scripts/homography.sh
sleep 5s