# Mission 3

## Assistive.prediction_draft

When comparing with the baseline, the larger threshold and margin would shorten detection delay. Citing insufficient evidence when there's missing data would prevent movement without creating a STOP.

## Warehouse.prediction_draft

When comparing with the baseline, the increased threshold and margin will lower detection delay and any unsafe movements, but could increase stops that aren't necessary.

## context_comparison

The final Warehouse policy used a 0.80 m threshold and 0.15 m margin, which resulted in a 0.95 m stop boundary. The Assistive policy used a larger 1.05 m threshold and 0.25 margin, which resulted in a 1.30 m boundary. The latter is necessary because movement near people needs more clearance. 

Warehouse policy selected Stop when there were missing readings while Assistive policy selected Insufficient evidence. The Warehouse policy had a 0.62% false-safe rate and 5.61% unnecessary-stop rate, while the Assistive policy had 0% for both. Both had zero delay and dangerous-command events.

## error_costs

In the warehouse, workers and owners bear the cost of false-safe and unnecessary-stop costs. The Warehouse baseline had a 0.62% false-safe rate, 5.61% unnecessary-stop rate, and 0.10 s delay. Revising kept both error rates unchanged but eliminated delay. 

With the Assistive robot, users bear the costs. The baseline had a 0% false-safe rate, 1.35% unnecessary stops, and 0.05 s delay. All three were reduced to zero in the revision.

## limitations

These seven tests establish that both final policies met the simulation limits for false-safe movement, unnecessary stops, delay, and dangerous commands. However, they do not establish the policies will still be safe in the real-world, with real hardware, different environments, variable human behavior, and unexpected longer sensor failure. 

Before deployment, I would consult stakeholders who have different levels of mobility for the Assistive robot. An additional test could be to test in the real-world how the robot's clearance, stopping delay, and abstention behavior changes with sudden approaches or longer sensor dropout.
