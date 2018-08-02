ROS PACKAGES

Steps for setting up workspace
mkdir ~/catkin_ws
cd ~/catkin_ws
catkin_make
cd src
git init
git remote add ros https://github.com/terrabiters/ros_packages
git pull
