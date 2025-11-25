
import numpy as np
import math as Math
from Plot import Plot





fig = Plot((2, 2), (10, 8))

P1 = fig.addSubplot()

# plotGraph(boards[0], (x) => 2 * (1 - Math.exp(-(x - 10) / 1)) - 2, 10, 20, "#61eb34", 2, 0.005, true, 0.01); 
f = lambda x: 2 * (1 - np.exp(-(x - 10))) - 2
P1.addPlot((10, 20), f, "#61eb34")

# plotGraph(boards[0], (x) => x >= 9.995 ? -2 : 2 * Math.exp(-1 * x), 0, 10, "#61eb34", 2, 0.005, false, 0.01);
f = lambda x: 2 * np.exp(-x)
P1.addPlot((0, 10), f, "#61eb34", bridgePoint=-2)

P1.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(100, "uA", "white")]
)

P2 = fig.addSubplot()

# plotGraph(boards[1], (x) => 2 * Math.exp(-1 * (x - 10)), 10, 20, "#61eb34", 2, 0.005, false, 0.01); 
f = lambda x: 2 * np.exp(-(x - 10))
P2.addPlot((10, 20), f, "#61eb34")

# plotGraph(boards[1], (x) => 2 * (1 - Math.exp(-x / 1)), 0, 10, "#61eb34", 2, 0.005, false, 0.01); 
f = lambda x: 2 * (1 - np.exp(-x))
P2.addPlot((0, 10), f, "#61eb34")

P2.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(100, "uA", "white")]
)

P3 = fig.addSubplot()

# plotGraph(boards[2], (x) => 2 * (1 - Math.exp(-(x - 10) / 1)) - 2, 10, 20, "#61eb34", 2, 0.005, false, 0.01); 
f = lambda x: 2 * (1 - np.exp(-(x - 10))) - 2
P3.addPlot((10, 20), f, "#61eb34")

# plotGraph(boards[2], (x) => x >= 9.995 ? -2 : 2 * Math.exp(-1 * x), 0, 10, "#61eb34", 2, 0.005, false, 0.01); 
f = lambda x: 2 * np.exp(-x)
P3.addPlot((0, 10), f, "#61eb34", bridgePoint=-2)

P3.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(10, "uA", "white")]
)

P4 = fig.addSubplot()

# plotGraph(boards[1], (x) => 2 * Math.exp(-1 * (x - 10)), 10, 20, "#61eb34", 2, 0.005, false, 0.01); 
f = lambda x: 2 * np.exp(-(x))
P4.addPlot((0, 10), f, "#61eb34")

# plotGraph(boards[1], (x) => 2 * (1 - Math.exp(-x / 1)), 0, 10, "#61eb34", 2, 0.005, false, 0.01); 
f = lambda x: 2 * (1 - np.exp(-(x - 10)))
P4.addPlot((10, 20), f, "#61eb34")

P4.setAxis(
    (0, 20, 2),
    (-2, 2, 1),
    (1, "ms"),
    [(100, "uA", "white")]
)

# fig.showPlot()
fig.savePlot("A1Q9.png")  


# while True:
#     pass