#!/usr/bin/env python
import rospy
import datetime
from std_msgs.msg import Int32

d = datetime.datetime.today()
year = d.year

def countmax(u):
    if u < 100:
        return u
    if u > 100:
        return year


if __name__ == '__main__':
    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Int32, queue_size=1)
    rate = rospy.Rate(10)
    n = 0
    u = 0
    while not rospy.is_shutdown():
        u += 1
        n = countmax(u)
        pub.publish(n)
        rate.sleep()
        if u > 100:
            break
