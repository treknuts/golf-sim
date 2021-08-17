from pylab import *
from math import *

acceleration_x = 0  # m/s^2
acceleration_y = -9.8  # m/s^2

velocity_initial = 75  # m/s
velocity_initial_angle = 10.9  # degrees - launch angle

v0_x = velocity_initial * cos(velocity_initial_angle * pi / 180)
v0_y = velocity_initial * sin(velocity_initial_angle * pi / 180)

time_max = 2 * v0_y / (-acceleration_y)
time_step = .01  # seconds
t = arange(0, time_max, time_step)
x = zeros(len(t))
y = zeros(len(t))

for i in range(len(t)):
    x[i] = v0_x * t[i] + 1 / 2.0 * acceleration_x * (t[i]) ** 2
    y[i] = v0_y * t[i] + 1 / 2.0 * acceleration_y * (t[i]) ** 2


plot(x, y, 'b.')
axis('equal')
show()
