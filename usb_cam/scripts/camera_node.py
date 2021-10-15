#!/usr/bin/env python
import rospy
import sys

import cv2
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image

cam0_path  = "/home/catkin_ws/ct/"
def main():
    rospy.init_node('camera_node', anonymous=True)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    rospy.loginfo(cap.get(cv2.CAP_PROP_FPS))
    rospy.loginfo(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    rospy.loginfo(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #bridge = CvBridge()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        time=rospy.get_time()
        timer=str(time)
        try:          
            image_name =timer+ ".jpg"         
            cv2.imwrite(image_name, frame)           
        except CvBridgeError as e:
            rospy.logwarn(e)
        rate.sleep()


if __name__ == '__main__':
    main()
