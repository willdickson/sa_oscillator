import numpy as np
import scipy as sp
import scipy.integrate as integrate
from .test_funcs import zero_func

class SAForceModel:

    def __init__(self, k=1.0, xeq=1.0, tau0=0.1, tau1=0.5):
        self.k = k
        self.xeq = xeq
        self.tau0 = tau0
        self.tau1 = tau1
        self.xfunc = zero_func

    def ode_func(self, t, y):
        k = self.k
        x = self.xfunc(t)
        xeq = self.xeq
        tau0 = self.tau0
        tau1 = self.tau1
        dy = np.zeros_like(y)
        dy[0] = (1.0/tau0)*(k*(x-xeq) - y[0])
        dy[1] = (1.0/tau1)*(k*(x-xeq) - y[1])
        return dy

    def solve(self, t_eval, y0=None):
        if y0 is None:
            y0 = np.array([0.0, 0.0])
        t_span = (t_eval[0], t_eval[-1])
        x_vals = np.array([self.xfunc(t) for t in t_eval])
        sol = integrate.solve_ivp(self.ode_func, t_span, y0, t_eval=t_eval, dense_output=True)
        force = self.k*x_vals - sol.y[0] + sol.y[1]
        return force







