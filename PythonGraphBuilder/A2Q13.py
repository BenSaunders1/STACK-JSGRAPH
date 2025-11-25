
import numpy as np
import math as Math
from Plot import Plot





fig = Plot((2, 2), (10, 8))

A1 = 2.98e-5; 
B1 = 12.71;
C1 = -47.92076;
incline_f = lambda x: A1 * Math.exp(B1 * x + C1);
incline_cutoff = 4.838;

A2 = -8.760207;
B2 = 15.26345;
C2 = -4.511021;
D2 = -9.916656; 
spike_in_f = lambda x: A2 * Math.tan(B2 * (x + C2)) + D2;
spike_in_cutoff = 5.02;

A3 = 8.72;
B3 = 15.749;
C3 = -4.74;
D3 = -8.62; 
spike_out_f = lambda x: A3 * Math.tan(B3 * (x + C3)) + D3;
spike_out_cutoff = 5.045;
spike_end = 5.222;

A = 0.104;
B = -14.7;
C = 82.33;
decline_start = 5.23;
decline_f = lambda x: A * Math.exp(B * x + C);

def main_f(x: np.array):
    y = np.zeros(len(x))
    for i in range(len(x)):
        if (min(x[i], incline_cutoff) == x[i]):
            y[i] = incline_f(x[i]);
        elif (min(x[i], spike_in_cutoff) == x[i]):
            y[i] = spike_in_f(x[i]); 

        if (max(spike_out_cutoff, x[i]) == spike_out_cutoff) * (max(x[i], spike_in_cutoff) == x[i]) == 1:
            y[i] = -112
        if ( (max(spike_out_cutoff, x[i]) == x[i]) * (max(x[i], spike_end) == spike_end) == 1 ):
            y[i] = spike_out_f(x[i]);
        if (max(x[i], decline_start) == x[i]):
            y[i] = decline_f(x[i]);

    return y
        
NUM_POINTS = 200
# plotGraph(boards[0], main_f, 2, 7, "#00ff00", 2, 0.1, false, 0.01); 
P1 = fig.addSubplot()
P1.addPlot((2, 7), main_f, "#00ff00", noiseBase=0, numPoints=NUM_POINTS)
P1.setAxis(
    (2, 7, 1),
    (-120, 40, 10),
    (1, "Hz"),
    [(1, "dB", "white")]
)

def T1(x): return -1 * main_f(x)

# plotGraph(boards[1], T1, 2, 7, "#00ff00", 2, 0.1, false, 0.01); 
P2 = fig.addSubplot()
P2.addPlot((2, 7), T1, "#00ff00", noiseBase=0, numPoints=NUM_POINTS)
P2.setAxis(
    (2, 7, 1),
    (-120, 40, 10),
    (1, "Hz"),
    [(1, "dB", "white")]
)


def T2(x): return main_f(x + 2)

# plotGraph(boards[2], T2, 2, 7, "#00ff00", 2, 0.1, false, 0.01); 
P3 = fig.addSubplot()
P3.addPlot((2, 7), T2, "#00ff00", noiseBase=0, numPoints=NUM_POINTS)
P3.setAxis(
    (2, 7, 1),
    (-120, 40, 10),
    (1, "Hz"),
    [(1, "dB", "white")]
)

def T3(x): return main_f(x) - 30;

# plotGraph(boards[3], T3, 2, 7, "#00ff00", 2, 0.1, false, 0.01);
P4 = fig.addSubplot()
P4.addPlot((2, 7), T3, "#00ff00", noiseBase=0, numPoints=NUM_POINTS)
P4.setAxis(
    (2, 7, 1),
    (-120, 40, 10),
    (1, "Hz"),
    [(1, "dB", "white")]
)

for P in [P1, P2, P3, P4]:
    P.axes.set_xticklabels(["100Hz", "1kHz", "10kHz", "100kHz", "1MHz", "10MHz"], fontsize=8, color="black")

# fig.showPlot()
fig.savePlot("A2Q13.png")  


# while True:
#     pass