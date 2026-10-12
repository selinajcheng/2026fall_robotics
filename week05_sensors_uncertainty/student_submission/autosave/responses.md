# Week 5: Sensors, Noise, and Uncertainty

- course_id: CSCI 39536
- email: selina.cheng72@cuny.edu
- name: Selina Cheng

## concepts.observation

When noise is increased, the spread of the distribution and variance/standard deviation values increase. As the noise decreases, the distribution of distances get closer and closer to the center and standard deviation/variance values decrease. Moving bias shifts the center of the distribution further away from the truth. Increasing bias shifts the distribution and median/mean values (with all other values besides bias unaffected) higher, while decreasing bias lower than shifts the distribution and median/mean values lower.

## final.course_reflection

This activity made me think differently about how robots actually make sense of their surroundings. I previously thought it was as simple as sensing distances since it should be just a measurement of reality, but noise, bias, quantization, dropout, and outliers can make it much more complex. Readings could be incomplete or misleading. I also learned about the trade-off between improving one quality and worsening another. In particular, smoothing estimates might make the robot more stable, but it can also increase response delay. It really does come down to thinking about what the robot is used for and what we want to prioritize. 

I also find it pretty interesting that the robots in different contexts require different policies, and this ties back to considering where the robot is and how the robot is being used to affect which configurations we want. Warehouse work is affected by these different settings differently from another person's safety or trust in a robot that's meant to be assisting them.

The lab reinforced the lesson that robotics isn't just about the technical aspect, but also about thinking about the end-to-end nature of what the robot is being used for, who will be affected by the decisions that are made during engineering, and, as a result, what kind of errors are acceptable (and which aren't). 

## final.synthesis

Mission 1 showed that, instead of the direct truth, sensors provide evidence that is imperfect. For example, at a target of 2.00 m, the quantized sensor produced a mean of 1.986 m, a -0.014 m bias, and 0.004307 m² variance. More samples would stabilize the mean, but they don't remove bias. 

Mission 2 showed me that estimation inherently involves trade-offs that we have to make. Increasing the moving-average window from 3 to 11 raised the RMSE from 0.1395 m to 0.1601 m while keeping a response delay of 1.10 s. This showed me that smoothing didn't automatically make things better. I chose a median filter with window 3 and equal fusion weight because it gave the lowest RMSE with a relatively low delay, achieving balance between the noisier sensor A and biased sensor B but with more stable readings.

Mission 3 connected those estimates to decisions regarding deployment. The final Warehouse policy had a 0.62% false safe rate, a 5.61% unnecessary stop rate, zero delay, and no dangerous command. The Assistive policy used a larger threshold and margin and instead abstained when there were missing readings. This produced zero false safe, unnecessary stop, delay, and dangerous command results. 

## mission_1.bias

-0.0141

## mission_1.bias_vs_variance

My prediction matched the statistics. The mean was 1.986m, showing a small bias while variance was low. Bias tells us how far away the mean of the readings is from the true value, while variance tells us how spread apart the readings are. 

## mission_1.dropouts

6

## mission_1.mean

1.986

## mission_1.median

2.00

## mission_1.more_samples

No, more samples would only make the mean more stable but it wouldn't remove bias. The bias would remain the same at -0.014 m.

## mission_1.outliers

1

## mission_1.prediction

A consistently biased sensor would show readings that cluster around a mean that's clearly different from the true 2.00 m distance. Its calculated bias (mean - true distance) would be either negative or positive and its variance would remain low. For a noisy but unbiased sensor, the readings would be spread more widely and hence would have higher variance. The mean, however, would be still around 2.00 m and the bias would be small.

## mission_1.prediction_draft

A consistently biased sensor would show readings that cluster around a mean that's clearly different from the true 2.00 m distance. Its calculated bias (mean - true distance) would be either negative or positive and its variance would remain low. For a noisy but unbiased sensor, the readings would be spread more widely and hence would have higher variance. The mean, however, would be still around 2.00 m and the bias would be small.

## mission_1.profile

quantized

## mission_1.robot_consequence

This imperfection could change the robot's decision about when to slow down or stop near a person. If the measured distance is rounded up, the robot could believe the person to be farther away than they really are, reducing clearance and safety.

## mission_1.variance

0.004307

## mission_2.comparison

With the moving-average filter, RMSE increased 0.1395 m with window 3, 0.1504 m with window 7, and 0.1601 m with window 11. All three had the same delay. For the matched window-3, the median had a slightly lower RMSE than the moving average (0.1389m) with the same delay of 1.1 seconds, but the median's maximum error increased.

## mission_2.fusion_choice

The RMSE values were 0.1389 m, 0.127 m, and 0.1335 m for sensor A weights of 0.25, 0.50, and 0.75, respectively. For each, response delays were 1.1, 0.9, and 0.45 seconds, respectively. I selected 0.5 because it produces the lowest RMSE (0.127m) with a moderate delay (0.90 s). We want to balance sensor A's fast but prone-to-outlier readings with the steadier and slower readings from sensor B. 

## mission_2.manual_average

4.1667

## mission_2.manual_fusion

2.25

## mission_2.manual_median

2.3

## mission_2.prediction_draft

Compared with window 7, window 11 should have lower error due to smoothing but higher response delay. 

## mission_2.responsiveness

Smoothing reduces variation in the short term but makes response delay higher. In the results, all three moving average windows had a response delay of 1.1 seconds, but with the window 3 median, increasing sensor A's weight reduced the delay from 1.1 seconds to 0.90 and 0.45 seconds. A delayed response estimate in distance would cause the robot to brake too late and reduce safety clearance. 

## mission_2.selected

0

## mission_3.Assistive.prediction_draft

When comparing with the baseline, the larger threshold and margin would shorten detection delay. Citing insufficient evidence when there's missing data would prevent movement without creating a STOP.

## mission_3.Warehouse.prediction_draft

When comparing with the baseline, the increased threshold and margin will lower detection delay and any unsafe movements, but could increase stops that aren't necessary.

## mission_3.context_comparison

The final Warehouse policy used a 0.80 m threshold and 0.15 m margin, which resulted in a 0.95 m stop boundary. The Assistive policy used a larger 1.05 m threshold and 0.25 margin, which resulted in a 1.30 m boundary. The latter is necessary because movement near people needs more clearance. 

Warehouse policy selected Stop when there were missing readings while Assistive policy selected Insufficient evidence. The Warehouse policy had a 0.62% false-safe rate and 5.61% unnecessary-stop rate, while the Assistive policy had 0% for both. Both had zero delay and dangerous-command events.

## mission_3.error_costs

In the warehouse, workers and owners bear the cost of false-safe and unnecessary-stop costs. The Warehouse baseline had a 0.62% false-safe rate, 5.61% unnecessary-stop rate, and 0.10 s delay. Revising kept both error rates unchanged but eliminated delay. 

With the Assistive robot, users bear the costs. The baseline had a 0% false-safe rate, 1.35% unnecessary stops, and 0.05 s delay. All three were reduced to zero in the revision.

## mission_3.limitations

These seven tests establish that both final policies met the simulation limits for false-safe movement, unnecessary stops, delay, and dangerous commands. However, they do not establish the policies will still be safe in the real-world, with real hardware, different environments, variable human behavior, and unexpected longer sensor failure. 

Before deployment, I would consult stakeholders who have different levels of mobility for the Assistive robot. An additional test could be to test in the real-world how the robot's clearance, stopping delay, and abstention behavior changes with sudden approaches or longer sensor dropout.
