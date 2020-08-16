# Gamepad_teleop_ROS
Node to publish Twist messages taking input from a gamepad

# How to use:
1. Put the folder into the /src folder in the catkin workspace
2. Run catkin_make
3. Source the setup.bash file
4. User 'rosrun' to run the program
5. Remember to set the '/joy_node/dev' parameter to '/dev/input/jsX' (X--> depends on your device)

# Requirements:

The node subscribes to the joy node. Install and run it first.
