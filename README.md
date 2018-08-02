ROS PACKAGES

Steps for setting up workspace:
mkdir ~/catkin_ws
cd ~/catkin_ws
catkin_make
cd src
git init
git remote add ros https://github.com/terrabiters/ros_packages
git pull ros master
gedit ~/.bashrc
Add this to end: "source ~/catkin_ws/devel/setup.bash"
close and repopen a new terminal

To Run:
Connect teensy and Logitech controller to computer
In a terminal:
roscore
In a new terminal:
roslaunch terrabot terrabot.launch

To add files:
git add <filename> or (git add . ) to add all files in folder
git commit -m <message on changes made>
git push ros master


