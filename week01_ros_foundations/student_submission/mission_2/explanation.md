# Mission 2

## Predictions

{'straight': 'I predict the robot will finish 0.45 meters forward from its starting point.', 'rotation': 'I predict its position will not change while its direction will change by a little lower than 1.5 radians to the left.', 'curve': "I predict a short curved path forward and towards the right because the turning speed is higher than the foward speed, making the vertical distance traveled less than it would've been (without turning).", 'curve_modified': 'This curve should be wider and turn the other way because the forward speed is greater than the turning speed and the turning speed is positive, denoting a left turn.'}

## Prediction Locks

{'straight': '2026-09-14T02:09:29.849151+00:00', 'rotation': '2026-09-14T02:12:18.375616+00:00', 'curve': '2026-09-14T02:14:17.294028+00:00', 'curve_modified': '2026-09-14T02:16:13.420578+00:00'}

## Motion Comparison

The Straight live simulation trial was a surprise to me. I had predicted the robot would move forward exactly 0.45 m with 0.15 m/s forward speed in 3 seconds, but I had forgotten that there's factors like friction, delay, etc. in the real world. So it came to me as a surprise when I saw the actual start to end distance was 0.315 m, which felt much less than I'd expected. 

## Measurement Explanation

We'll look at the original/first curved trial. The estimated travel path was 0.394 m while the start-to-end distance was 0.376. The two describe different measurements because the estimated travel path is the curve as measured by odometry while the latter measures the distance from the starting to the end point, a straight line. Hence the latter is always shorter than the former.

## Safety Explanation

The command guards checks every driving command before it's executed for safety and validity. The final zero command exists as a marker for the end of a trial with zero forward and turning speed. The timeout is needed if a program crashes or no new commands are sent after 0.5 seconds.

## Modified Settings

{'linear_x': 0.22, 'angular_z': 0.1, 'duration': 4.0}
