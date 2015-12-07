export zumyXY='zumy1d'
export base_ar=0
export zumy_ar=1
export origin_ar=3
export end_ar=4
export discretization_x=4
export discretization_y=4

export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/scratch/shared:~/final_proj

source /home/cc/ee106a/fa15/class/ee106a-az/final_proj/devel/setup.bash

export ROS_HOSTNAME=$(hostname --short).local
export ROS_MASTER_URI=http://$(hostname --short).local:11311
export ROSLAUNCH_SSH_UNKNOWN=1
echo "Environment set"