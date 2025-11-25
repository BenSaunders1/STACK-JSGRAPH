
import numpy as np
import math as Math
from Plot import Plot





fig = Plot((2, 2), (12, 8))


def decayGraph (settlePoint, settleHeight, decayRate = 0.00014):
    def midFunc(x: np.array) :
        y = np.zeros(len(x))
        for i in range(len(x)):
            if x[i] < settlePoint:
                y[i] = 0.5 * Math.exp(-x[i] / decayRate) * Math.sin(2 * Math.pi * 100000 * x[i])
            else:
                y[i] = settleHeight * Math.sin(2 * Math.pi * 100000 * x[i])

        return y
    
    return midFunc 

print(decayGraph(0.00045, 0.012)(np.array([0.000012, 0.000022, 0.000033, 0.000044, 0.000055])))
def decayGraphInv(settlePoint, settleHeight): 
    def midFunc(x_in: np.array):
        y = np.zeros(len(x_in))
        for i in range(len(x_in)):
            x = -1 * x_in[i] + 0.001
            if (min(x, settlePoint) == x):
                y[i] = 0.5 * Math.exp(-x / 0.00014) * Math.sin(2 * Math.pi * 100000 * x)
            else: 
                y[i] = settleHeight * Math.sin(2 * Math.pi * 100000 * x)

        return y

    return midFunc;

P1 = fig.addSubplot()

NUM_POINTS = 432
P1.addPlot((0, 0.001), decayGraph(0.00045, 0.012), "green", numPoints=NUM_POINTS, lineWidth=1, noiseBase=0)

P1.setAxis(
    (0, 0.001, 0.0001),
    (-0.5, 0.5, 0.1),
    (1000, "ms"),
    [(1000, "mV", "white")]
)

P2 = fig.addSubplot()

P2.addPlot((0, 0.001), decayGraphInv(0.00045, 0.012), "green", numPoints=NUM_POINTS, lineWidth=1, noiseBase=0)

P2.setAxis(
    (0, 0.001, 0.0001),
    (-0.5, 0.5, 0.1),
    (1000, "ms"),
    [(1000, "mV", "white")]
)

P3 = fig.addSubplot()

P3.addPlot((0, 0.001), decayGraph(0.001, 0.012, 0.00025), "green", numPoints=NUM_POINTS, lineWidth=1, noiseBase=0)

P3.setAxis(
    (0, 0.001, 0.0001),
    (-0.5, 0.5, 0.1),
    (1000, "ms"),
    [(1000, "mV", "white")]
)


P4 = fig.addSubplot()

f = lambda x: 0.01 * np.sin(2 * Math.pi * 100000 * x)
P4.addPlot((0, 0.001), f, "green", numPoints=NUM_POINTS, lineWidth=1, noiseBase=0)

P4.setAxis(
    (0, 0.001, 0.0001),
    (-0.5, 0.5, 0.1),
    (1000, "ms"),
    [(1000, "mV", "white")]
)

# fig.showPlot()
fig.savePlot("A2Q9.png")  


# while True:
#     pass