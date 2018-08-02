ROS PACKAGES

Steps for setting up workspace:
mkdir ~/catkin_ws
cd ~/catkin_ws
catkin_make
cd src
git init
git remote add ros https://github.com/terrabiters/ros_packages
git pull 


To add files:
git add <filename> or (git add . ) to add all files in folder
git commit -m <message here on changes made>
git push ros master
