# let's call the triangle PLR, where P is the robot pose, L the left vertex, R the right vertex
# available:P.x, P.y, yaw
# parameters (found on the web):
d = 4 # max monitored distance: reasonably not more than 3.5-4m
alpha = 1 # field of view: 57 deg kinect, 58 xtion, we can use exactly 1 rad (=57.3 deg)

L.x = P.x + d * cos(yaw-alpha/2)
L.y = P.y + d * cos(yaw-alpha/2)
R.x = P.x + d * cos(yaw+alpha/2)
R.y = P.y + d * cos(yaw+alpha/2)
# problem: we don't know what is the direction of yaw = 0,
# so we might have to add a constant angular offset to yaw
