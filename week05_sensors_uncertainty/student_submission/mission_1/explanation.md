# Mission 1

## bias

-0.0141

## bias_vs_variance

My prediction matched the statistics. The mean was 1.986m, showing a small bias while variance was low. Bias tells us how far away the mean of the readings is from the true value, while variance tells us how spread apart the readings are. 

## dropouts

6

## mean

1.986

## median

2.00

## more_samples

No, more samples would only make the mean more stable but it wouldn't remove bias. The bias would remain the same at -0.014 m.

## outliers

1

## prediction

A consistently biased sensor would show readings that cluster around a mean that's clearly different from the true 2.00 m distance. Its calculated bias (mean - true distance) would be either negative or positive and its variance would remain low. For a noisy but unbiased sensor, the readings would be spread more widely and hence would have higher variance. The mean, however, would be still around 2.00 m and the bias would be small.

## prediction_draft

A consistently biased sensor would show readings that cluster around a mean that's clearly different from the true 2.00 m distance. Its calculated bias (mean - true distance) would be either negative or positive and its variance would remain low. For a noisy but unbiased sensor, the readings would be spread more widely and hence would have higher variance. The mean, however, would be still around 2.00 m and the bias would be small.

## profile

quantized

## robot_consequence

This imperfection could change the robot's decision about when to slow down or stop near a person. If the measured distance is rounded up, the robot could believe the person to be farther away than they really are, reducing clearance and safety.

## variance

0.004307
