#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy 

#rospy.set_param('joy_node/dev', '/dev/input/js1')

linear_speed = 5
angular_speed = 5

def move(joy_data):
    global linear_speed
    global angular_speed
    
    vel_msg = Twist()
    # 6 and 7 refers to D-PAD input
    if joy_data.axes[7] == 1:
        linear_speed += 1
    elif joy_data.axes[7] == -1:
        linear_speed -=1
    if joy_data.axes[6] == 1:
        angular_speed -=1
    elif joy_data.axes[6] == -1:
        angular_speed += 1

    vel_msg = Twist()
    # 1 and 3 refers to the thumb stick input
    vel_msg.linear.x = (joy_data.axes[1])*linear_speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = (joy_data.axes[3])*angular_speed
    pub.publish(vel_msg)
    print("linear %f"%(vel_msg.linear.x))
    print("angular %f"%(vel_msg.angular.z))
    print("ls %i"%(linear_speed))
    print("as %i"%(angular_speed))

rospy.init_node('joy_control_translator')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber("joy", Joy, callback = move)
rospy.spin()
