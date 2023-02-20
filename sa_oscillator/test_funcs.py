import numpy as np

class Step:

    def __init__(self, tstep=0.0, start_value=0.0, final_value=1.0):
        self.tstep = tstep
        self.start_value = start_value 
        self.final_value = final_value

    def __call__(self,t):
        if t < self.tstep:
            value = self.start_value
        else:
            value = self.final_value
        return value


class SquareWave:

    def __init__(self, period=1.0, lower_value=0.0, upper_value=1.0):
        self.period = period
        self.lower_value = lower_value
        self.upper_value = upper_value

    def __call__(self,t):
        tmod = t % self.period
        if tmod < 0.5*self.period:
            value = self.lower_value
        else:
            value = self.upper_value
        return value


class SineWave:

    def __init__(self, period=1.0, amplitude=1.0, offset=1.0):
        self.period = period
        self.amplitude = amplitude
        self.offset = offset

    def __call__(self,t):
        return self.amplitude*np.sin(2.0*np.pi*t/self.period) + self.offset


def zero_func(t):
    return 0.0


