#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Empty

pub = rospy.Publisher('toggle_led', Empty, queue_size=10)

def callback(Empty):
    rospy.loginfo(rospy.get_caller_id() + "Tx2 heard response from X1")
    pub.publish()

def blink_led():
    rospy.init_node('tx2', anonymous=True)
    rospy.Subscriber('toggle_led_main', Empty, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        blink_led()
    except rospy.ROSInterruptException:
        pass
