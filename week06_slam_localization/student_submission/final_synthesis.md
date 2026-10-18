# Final synthesis

Based on the two maps, the robot can estimate the free space and occupied boundaries around the entrance, the hallway connected to the entrance, and the openings into the rooms that were explored. The robot can't know what's inside unexplored rooms or what's behind walls that were blocking the LiDAR's line of sight. Additionally, unknown cells represent missing evidence, and it would be unknown whether that area is occupied or safe. 

Route 1 took 8 minutes and mapped 14.49% of its map area, while Route 2 took 9 minutes and covered 17.39% of the map area. The known area per minute rate increased from 1.26 to 1.61 m²/min. However, the second map's greater coverage didn't make it more reliable. In fact, its quality score decreased from 34.8 for map 1 to 32.3 for map 2, and its speckle fraction increased from 9.86% to 16.47%, and occupied components increased from 45 to 129. And visually, you could tell that map 2 contained more distorted obstacle boundaries that were clearly inaccurate.

Strategy 2's inaccuracies might have been independent of the route itself due to the robot falling or tilting, which may have disrupted its pose estimate and contributed to inaccurate scans. The images alone can't distinguish the geometry error from collision effects or any additional non-adometry errors. 

I would explicitly trust map 1 more for a later task because its walls appear to be accurate to the actual TurtleBot3 house and the quality score is higher, has less speckle despite covering less area, though not actually a bit less. Neither map still proves geometrically accuracy without an actual comparison with the ground truth distances and positions of the walls.
