# Gamepad_teleop_ROS
Node to publish Twist messages taking input from a gamepad
How to use:
Put the folder into the /src folder in the catkin workspace
Run catkin_make
Source the setup.bash file
User 'rosrun' to run the program
Remember to set the '/joy_node/dev' parameter to '/dev/input/jsX' (X--> depends on your device)

Requirements:
The node subscribes to the joy node. Install and run it first.
