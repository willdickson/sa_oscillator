import numpy as np
import matplotlib.pyplot as plt

import sa_oscillator.test_funcs as test_funcs
from sa_oscillator.sa_force_model import SAForceModel

t0 = 0.0
t1 = 10.0
num_pts = 10000
t = np.linspace(t0, t1, num_pts)

param = {
    'k'    : 1.5,
    'xeq'  : 2.0,
    'tau0' : 0.2,
    'tau1' : 0.5,
    }


if 0:
    xfunc = test_funcs.Step(
            tstep = 1.0, 
            start_value = param['xeq'], 
            final_value = param['xeq']+2.0
            )
if 0:
    xfunc = test_funcs.SquareWave(
            period = 5.0, 
            lower_value = param['xeq'] - 0.0,
            upper_value = param['xeq'] + 1.0
            )
if 1:
    xfunc = test_funcs.SineWave(
            period = 2.5,
            amplitude = 1.0,
            offset = param['xeq']
            )

force_model = SAForceModel(**param)
force_model.xfunc = xfunc

f = force_model.solve(t) 
x = [xfunc(tval) for tval in t]

fig, ax = plt.subplots(2,1,sharex=True)
ax[0].plot(t,x)
ax[0].set_ylabel('step')
ax[0].grid(True)
ax[1].plot(t,f)
ax[1].set_ylabel('force')
ax[1].grid(True)
ax[1].set_xlabel('t (sec)')

fig, ax = plt.subplots(1,1)
ax.plot(x,f)
ax.set_xlabel('x')
ax.set_ylabel('f')
ax.grid(True)
plt.show()

