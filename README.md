ROS PACKAGES (view in raw)

Steps for setting up workspace:
Install ROS
git clone https://github.com/jetsonhacks/installROSTX2
./installROS.sh
./setupCatkinWorkspace.sh

cd ~/catkin_ws/src
mkdir terrabot && cd terrabot
git init
git remote add ros https://github.com/terrabiters/ros_packages
rm CMakeLists.txt
git pull ros master
cd ..
catkin_make
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


