# Mission 3

## Data To Command

My two functions turn a list of LiDAR distances into a move-or-stop command. front_distance() looks at the LiDAR distances, calculates which ones are valid forward distances and returns the closest valid distance. decide_velocity() compares the result from front_distance() with the stop distance and returns a velocity of 0.0 m/s when the obstacle is too close or data is missing but otherwise returns a capped forward speed.

## Missing Data Safety

The robot stops when there is no valid measurement because without a valid measurement of front distance, the robot can't know whether moving would cause collision, i.e., the path might not be clear, so it's safer to return 0.0 to avoid that.

## System Layers

The obstacle_guard ROS node receives /scan. My functions are called and the proposed speed is published on /student_cmd_vel. The command_guard checks the proposed command and publishes the approved command on /cmd_vel, which is executed in the simulator.
