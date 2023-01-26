import matplotlib.pyplot as plt
from math import sin, trunc

r = 1000
C = 0.005
Rh = 1000000
step = 0.01

time = 100


def count_E(value):
    return (abs(sin(value)) + sin(value)) / 2


u = [0]
E = [0]
timeskip = [0]

for t in range(1, trunc(time//step)+1):
    E.append(count_E(t*step))
    u.append(E[t-1]*step/(r*C)+(1-1/C*(1/r+1/Rh)*step)*u[t-1])
    timeskip.append(t*step)


fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot()
ax.grid()
ax.set_xlabel("time, c")
ax.set_ylabel("voltage, A")

line2, = ax.plot(timeskip, E, 'green', label='Input')
line1, = ax.plot(timeskip, u, 'brown', label='Output')

ax.legend(handles=[line1, line2])

fig.show()
