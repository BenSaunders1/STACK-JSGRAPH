## https://edstem.org/au/courses/15277/discussion/1770839

import numpy as np
import math as Math
from Plot import Plot



# const state_response = (a) => (x) => a * (1 - Math.exp(-x / 1)); 
# const zero_state_response = (a) => (x) => a * Math.exp(-1 * (x - 10)); 
# const v_state_response = (a) => (x) => a * (1 - Math.exp(-(x - 10) / 1)) - 2; 
# const v_zero_state_response = (a) => (x) => x >= 9.9 ? -2 : a * Math.exp(-1 * x); 
# const v_zero_state_response_noise = (x) => x >= 9.9 ? -2.6 : 2 * Math.exp(-1 * x); 

fig = Plot((3, 2), (10, 16))

P1 = fig.addSubplot()

# plotGraph(boards[0], state_response(2), 0, 10, "blue", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-x))
P1.addPlot((0, 10), f, "blue", noiseBase=0.05)

# plotGraph(boards[0], zero_state_response(2), 10, 20, "blue", 2, 0.03); 
f = lambda x: 2 * np.exp(-(x - 10))
P1.addPlot((10, 20), f, "blue", noiseBase=0.05)

# plotGraph(boards[0], v_state_response(2), 10, 20, "red", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-(x - 10))) - 2
P1.addPlot((10, 20), f, "red", noiseBase=0.05)

# plotGraph(boards[0], v_zero_state_response_noise, 0, 10, "red", 2, 0.03); 
f = lambda x: 2 * np.exp(-x)
P1.addPlot((0, 10), f, "red", bridgePoint=-2.05, noiseBase=0.05)

P1.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(1, "V", "red"), (1, "mA", "blue")]
)

P2 = fig.addSubplot()

# plotGraph(boards[0], state_response(2), 0, 10, "blue", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-x))
P2.addPlot((0, 10), f, "blue", noiseBase=0)

# plotGraph(boards[0], zero_state_response(2), 10, 20, "blue", 2, 0.03); 
f = lambda x: 2 * np.exp(-(x - 10))
P2.addPlot((10, 20), f, "blue", noiseBase=0)

# plotGraph(boards[0], v_state_response(2), 10, 20, "red", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-(x - 10))) - 2
P2.addPlot((10, 20), f, "red", noiseBase=0)

# plotGraph(boards[0], v_zero_state_response_noise, 0, 10, "red", 2, 0.03); 
f = lambda x: 2 * np.exp(-x)
P2.addPlot((0, 10), f, "red", bridgePoint=-2.05, noiseBase=0)

P2.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(1, "V", "red"), (1, "mA", "blue")]
)

P3 = fig.addSubplot()

# plotGraph(boards[2], state_response(1), 0, 10, "red", 2); 
f = lambda x: 1 * (1 - np.exp(-x))
P3.addPlot((0, 10), f, "red", noiseBase=0.05)

# plotGraph(boards[2], zero_state_response(1), 10, 20, "red", 2); 
f = lambda x: 1 * np.exp(-(x - 10))
P3.addPlot((10, 20), f, "red", noiseBase=0.05)

# plotGraph(boards[2], v_state_response(1), 10, 20, "blue", 2);
f = lambda x: 1 * (1 - np.exp(-(x - 10))) - 1
P3.addPlot((10, 20), f, "blue", noiseBase=0.05)

# plotGraph(boards[2], v_zero_state_response(1), 0, 10, "blue", 2); 
f = lambda x: 1 * np.exp(-x)
P3.addPlot((0, 10), f, "blue", bridgePoint=-1.05, noiseBase=0.05)

P3.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(1, "V", "blue"), (1, "mA", "red")]
)


P4 = fig.addSubplot()

# plotGraph(boards[0], state_response(2), 0, 10, "blue", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-x))
P4.addPlot((0, 10), f, "red", noiseBase=0.05)

# plotGraph(boards[0], zero_state_response(2), 10, 20, "blue", 2, 0.03); 
f = lambda x: 2 * np.exp(-(x - 10))
P4.addPlot((10, 20), f, "red", noiseBase=0.05)

# plotGraph(boards[0], v_state_response(2), 10, 20, "red", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-(x - 10))) - 2
P4.addPlot((10, 20), f, "blue", noiseBase=0.05)

# plotGraph(boards[0], v_zero_state_response_noise, 0, 10, "red", 2, 0.03); 
f = lambda x: 2 * np.exp(-x)
P4.addPlot((0, 10), f, "blue", bridgePoint=-2.05, noiseBase=0.05)

P4.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(1, "V", "red"), (1, "mA", "blue")]
)

P5 = fig.addSubplot()

# plotGraph(boards[4], state_response(1), 0, 10, "blue", 2); 
f = lambda x: 1 * (1 - np.exp(-x))
P5.addPlot((0, 10), f, "blue", noiseBase=0)

# plotGraph(boards[4], zero_state_response(1), 10, 20, "blue"); 
f = lambda x: 1 * np.exp(-(x - 10))
P5.addPlot((10, 20), f, "blue", noiseBase=0)

# plotGraph(boards[4], v_state_response(1), 10, 20, "red", 2); 
f = lambda x: 1 * (1 - np.exp(-(x - 10))) - 1
P5.addPlot((10, 20), f, "red", noiseBase=0)

# plotGraph(boards[4], v_zero_state_response(1), 0, 10, "red", 2); 
f = lambda x: 1 * np.exp(-x)
P5.addPlot((0, 10), f, "red", bridgePoint=-1.05, noiseBase=0)

P5.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(1, "V", "blue"), (1, "mA", "red")]
)

P6 = fig.addSubplot()

# plotGraph(boards[0], state_response(2), 0, 10, "blue", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-x))
P6.addPlot((0, 10), f, "red", noiseBase=0)

# plotGraph(boards[0], zero_state_response(2), 10, 20, "blue", 2, 0.03); 
f = lambda x: 2 * np.exp(-(x - 10))
P6.addPlot((10, 20), f, "red", noiseBase=0)

# plotGraph(boards[0], v_state_response(2), 10, 20, "red", 2, 0.03); 
f = lambda x: 2 * (1 - np.exp(-(x - 10))) - 2
P6.addPlot((10, 20), f, "blue", noiseBase=0)

# plotGraph(boards[0], v_zero_state_response_noise, 0, 10, "red", 2, 0.03); 
f = lambda x: 2 * np.exp(-x)
P6.addPlot((0, 10), f, "blue", bridgePoint=-2.05, noiseBase=0)

P6.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(1, "V", "red"), (1, "mA", "blue")]
)


# fig.showPlot()
fig.savePlot("A1Q15.png")  


# while True:
#     pass