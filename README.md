# Gamepad_teleop_ROS
Node to publish Twist messages to '/cmd_vel' topic, taking input from a gamepad

# How to use:
1. Put the folder into the /src folder in the catkin workspace
2. Run catkin_make
3. Source the setup.bash file
4. User 'rosrun' to run the program
5. Remember to set the '/joy_node/dev' parameter to '/dev/input/jsX' (X--> depends on your device)
6. Use 'rostopic echo' to view the joy node's output and find the array number(position) of the required buttons and change it in the script.

# Requirements:

ROS joy package should be running

The node subscribes to the joy node. Install and run it first.

# Working
1. D-Pad is used to increase/decrease the maximum linear/angular speed.
  
  Up/Down - Linear speed
  
  Left/Right - Angular speed
  
2. Thumb sicks are used to control direction.
