#!/usr/bin/env python

import rospy
from std_msgs.msg import String,Empty

def blink_led():
    pub = rospy.Publisher('toggle_led_tx2', Empty, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    pub.publish()

if __name__ == '__main__':
    try:
        blink_led()
    except rospy.ROSInterruptException:
        pass



