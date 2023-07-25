#!/usr/bin/env python3
import rospy         #We had the dependencies

if __name__ == '__main__':
    rospy.init_node("test_node")   #Initialize a node first
    rospy.loginfo("Test node has been started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():    #Tells if the node got a shutdown request
        rospy.loginfo("Hello")
        rate.sleep()                  #Pauses the program for 0.1 second
