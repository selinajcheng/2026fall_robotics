# Mission 1

## Scan Observation

I found a list of many exact number measurements, which represents the distances between the robot and objects around it.

## Guided Checks

{'node_list': True, 'guard_info': True, 'bridge_info': True, 'scan_info': True, 'scan_message': True, 'command_topics': True}

## Graph Explanation

A ROS 2 graph is a map of the current programs running and how they exchange messages. From this mission, the /ros_gz_bridge publishes LiDAR readings on /scan.

## Command Path Explanation

A proposed command travels on /student_cmd_vel. The /course_cmd_vel_guard node safety checks the command. Then it publishes the approved command on /cmd_vel and is sent to the simulator.

## Tools Explanation

Gazebo is a robot simulator while RViz is data viewer for ROS 2. The second is used to display information while the first simulates physics.
