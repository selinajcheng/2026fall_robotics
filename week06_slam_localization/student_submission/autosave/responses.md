# Week 6: SLAM and Mapping

- name: Selina Cheng
- email: selina.cheng72@cuny.edu

## final.course_reflection

This activity made me think a lot about the fact that the range of sensors can be much less than I thought it was, and it's much harder to be able to map out an area without a larger range or some additional exploration, and even if you were to explore more area, there is still the concern of whether or not the sensor mapped information actually aligns and is accurate to the actual environment that was being mapped in the first place. 

This activity also changed how I think about what it means for a robot to know its environment. Watching a map form in RViz made mapping much more visceral and concrete by comparing the two routes also revealed that collecting more information and covering more area as an explicit intention is not necessarily something that results in a better understanding of the area for the robot. 

This activity also made me realize just how much more judgment there is in robotics, because the engineer can't actually just accept a larger map or higher coverage as evidence that the robot actually understands the space and the map has to be compared with the visible structures and the robot's behavior itself as well throughout the mapping activity. The activity also made me a little bit more cautious about trusting outputs without actually checking them against other evidence. 

## final.synthesis

Based on the two maps, the robot can estimate the free space and occupied boundaries around the entrance, the hallway connected to the entrance, and the openings into the rooms that were explored. The robot can't know what's inside unexplored rooms or what's behind walls that were blocking the LiDAR's line of sight. Additionally, unknown cells represent missing evidence, and it would be unknown whether that area is occupied or safe. 

Route 1 took 8 minutes and mapped 14.49% of its map area, while Route 2 took 9 minutes and covered 17.39% of the map area. The known area per minute rate increased from 1.26 to 1.61 m²/min. However, the second map's greater coverage didn't make it more reliable. In fact, its quality score decreased from 34.8 for map 1 to 32.3 for map 2, and its speckle fraction increased from 9.86% to 16.47%, and occupied components increased from 45 to 129. And visually, you could tell that map 2 contained more distorted obstacle boundaries that were clearly inaccurate.

Strategy 2's inaccuracies might have been independent of the route itself due to the robot falling or tilting, which may have disrupted its pose estimate and contributed to inaccurate scans. The images alone can't distinguish the geometry error from collision effects or any additional non-adometry errors. 

I would explicitly trust map 1 more for a later task because its walls appear to be accurate to the actual TurtleBot3 house and the quality score is higher, has less speckle despite covering less area, though not actually a bit less. Neither map still proves geometrically accuracy without an actual comparison with the ground truth distances and positions of the walls. 

## mission_1.drift_and_revisit

When I returned to a previously scanned area, I didn't notice any change in previously mapped walls. Evidence such as periodic before-after screenshots and SLAM diagnostic data would be helpful in determining whether SLAM corrected drift.

## mission_1.limitations

An area that remained unknown was the area to the right side of the hallway immediately accessible through the entrance. My route was initially planned to include rotation during the time the robot was in the hallway, but the LiDAR's line of sight was only able to cover a shorter distance than I expected, so much of the area opposite the direction the robot went in remained unknown.

## mission_1.route.original_prediction

I plan to move for about 4 units to the right and also create map coverage of the opening, and see what that looks like by moving around the entrance. Then I will go inside the entrance and move around to create further map coverage by rotating around once inside the entrance.

I predict the map coverage will be weakest when the robot is in a constrained area that still has a lot of unknown map area that can only be accessible through small openings (in which case the LiDAR scan can't easily scan for).

## mission_1.route.prediction_draft

I plan to move for about 4 units to the right and also create map coverage of the opening, and see what that looks like by moving around the entrance. Then I will go inside the entrance and move around to create further map coverage by rotating around once inside the entrance.

I predict the map coverage will be weakest when the robot is in a constrained area that still has a lot of unknown map area that can only be accessible through small openings (in which case the LiDAR scan can't easily scan for).

## mission_2.comparison

Route 2 gave more useful coverage for the time spent.  The prediction that the known area would increase was correct. However, the map quality decreased, which is something that's visibly seen and also seen in the quality score dropping by 2.5 points. The known area per minute increased by 0.35 m²/min, despite just an approximately 1-minute increase in elapsed time. The trade-off is that the map accuracy and quality decrease despite there being much more known area, and so the trade-off is more about usable known quantities. 

## mission_2.map_choice

I would trust the first strategy much more. The one limit is that, for strategy two, I did likely actually make the robot fall over, and hence some of the readings were incorrect due to this. Maybe another run would probably be much more reliable in reassessing whether strategy two was good or not.

However, I definitely would trust the first strategy much more, just because it made use of a lot more rotation to map out an area around multiple given points during the route. Additionally, the walls are clearly very aligned and follow the actual structure of the area. Despite there being some missing rooms, at least the room that is included is mapped out accurately. The limit of what these images and the numbers cannot prove is that wall positions and distances are geometrically accurate.

## mission_2.strategy.original_prediction

My second route will take the robot to enter through the entrance, but instead of just entering another room through the hallway, the robot will traverse the hallway back and forth. It may produce a clearer map as it will cover more overall space.

## mission_2.strategy.prediction_draft

My second route will take the robot to enter through the entrance, but instead of just entering another room through the hallway, the robot will traverse the hallway back and forth. It may produce a clearer map as it will cover more overall space.
