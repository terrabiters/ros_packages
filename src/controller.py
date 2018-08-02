#!/usr/bin/env python
import rospy
from std_msgs.msg import String,Empty
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# Author: Andrew Dai
# This ROS Node converts Joystick inputs from the joy node
# into commands for turtlesim

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 1 aka left stick vertical controls linear speed
# axis 0 aka left stick horizonal controls angular speed
def callback(data):
    twist = Twist()
    twist.linear.x = 4*data.axes[3]
    twist.angular.z = 4*data.axes[2]
    pub_drive.publish(twist)
    if data.buttons[0] == 1:
        pub_blink.publish()


# Intializes everything
def start():
    # publishing to "turtle1/cmd_vel" to control turtle1
    global pub_drive
    global pub_blink
    pub_drive = rospy.Publisher('turtle1/cmd_vel', Twist)
    pub_blink = rospy.Publisher('toggle_led', Empty, queue_size=10)

    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, callback)
    # starts the node
    rospy.init_node('Joy2Turtle')
    rospy.spin()

if __name__ == '__main__':
    start()
    
