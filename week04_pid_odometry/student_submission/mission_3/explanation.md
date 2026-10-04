# mission_3 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### technical_analysis

I predicted that increasing forward speed or using too little derivative control would cause the robot to reduce or violate clearance and increase tracking error, but this wasn't the case. My final drive used a forward speed of 0.44 and no derivative control but still reached all four waypoints. My prediction was therefore not fully demonstrated by this drive, though the lowest pedestrian distance (0.29m) was only marginally above the 0.28m requirement.

The robot finds the direction from its estimated position to the next waypoint and uses atan2 to convert the direction to a desired heading. Then substracting the estimated current heading gets us the heading error. PID converts this error into a steering command where proportional error responds to current error, integral control accumulates persistent error, and derivative control helps prevent rapid changes.

An inaccurate wheel radius causes odometry to convert wheel movement into the wrong estimated distance. So even a well-tuned controller can follow the wrong physical path because its steering decisions are based on inaccurate pose estimates.

### human_centered_analysis

The consequential failure for a pedestrian is that they're either endangered or get hurt due to clearance being too low and/or speed being too fast. I would require clearance to be high and speed to be lower if that's the tradeoff that needs to be made. Responsibility belongs to those who choose factors like clearance, speed, and among others.