export zumyXY='zumy1d'
export base_ar=1
export zumy_ar=2



export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:/scratch/shared:~/final_proj

source /home/cc/ee106a/fa15/class/ee106a-bc/final_proj/devel/setup.bash

export ROS_HOSTNAME=$(hostname --short).local
export ROS_MASTER_URI=http://$(hostname --short).local:11311
export ROSLAUNCH_SSH_UNKNOWN=1
echo "Environment set"