# Mission 2

## comparison

With the moving-average filter, RMSE increased 0.1395 m with window 3, 0.1504 m with window 7, and 0.1601 m with window 11. All three had the same delay. For the matched window-3, the median had a slightly lower RMSE than the moving average (0.1389m) with the same delay of 1.1 seconds, but the median's maximum error increased.

## fusion_choice

The RMSE values were 0.1389 m, 0.127 m, and 0.1335 m for sensor A weights of 0.25, 0.50, and 0.75, respectively. For each, response delays were 1.1, 0.9, and 0.45 seconds, respectively. I selected 0.5 because it produces the lowest RMSE (0.127m) with a moderate delay (0.90 s). We want to balance sensor A's fast but prone-to-outlier readings with the steadier and slower readings from sensor B. 

## manual_average

4.1667

## manual_fusion

2.25

## manual_median

2.3

## prediction_draft

Compared with window 7, window 11 should have lower error due to smoothing but higher response delay. 

## responsiveness

Smoothing reduces variation in the short term but makes response delay higher. In the results, all three moving average windows had a response delay of 1.1 seconds, but with the window 3 median, increasing sensor A's weight reduced the delay from 1.1 seconds to 0.90 and 0.45 seconds. A delayed response estimate in distance would cause the robot to brake too late and reduce safety clearance. 

## selected

0
