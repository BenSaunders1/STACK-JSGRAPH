from matplotlib.axes import Axes
import numpy as np
import math as Math
import random
from typing import Callable



class Subplot():
    def __init__ (self, index: int, parent, gridSize: tuple):
        self.index = index
        self.axes = parent
        self.format()

    def format(self):
        """Formats the subplot
        
        This method formats the subplot to match a DSO trace.
        """
        self.axes.set_facecolor("black")
        self.axes.spines['bottom'].set_color('white')
        self.axes.spines['top'].set_color('white')
        self.axes.spines['right'].set_color('white')
        self.axes.spines['left'].set_color('white')
        self.axes.tick_params(axis='x', colors='black')
        self.axes.tick_params(axis='y', colors='black')
        self.axes.grid(True, 'both', 'both')
        self.axes.set_title(f"Figure [{self.index + 1}]", loc='center', fontdict={'color': 'black', 'fontname': 'sans-serif'})

    def setAxis(self, xTicks: tuple[float, float, float], yTicks: tuple[float, float, float], xDisplay: tuple[float, str], yDisplay: list[tuple[float, str, str]], fontSize:int = 8):
        """Sets the axis size
        
        This method sets the axis size for the subplot.
        
        Args:
            xTicks (tuple): The x-axis ticks. (min, max, step)
            yTicks (tuple): The y-axis ticks. (min, max, step)
            xDisplay (tuple): The x-axis display. (scalar, unit)
            yDisplay (list[tuple]): The y-axis displays. List[(scalar, unit, colour)]
            fontSize (int): The font size.
        """
        xRange = xTicks[1] - xTicks[0]
        xMargin = xRange * 0.05

        yRange = yTicks[1] - yTicks[0]
        yMargin = yRange * 0.05

        self.axes.set_xlim(xTicks[0] - xMargin, xTicks[1] + xMargin)
        self.axes.set_ylim(yTicks[0] - yMargin, yTicks[1] + yMargin)
        self.axes.hlines(0, xTicks[0] - xMargin, xTicks[1] + xMargin, colors="lightgrey", linewidth=0.5)

        xticks = np.arange(xTicks[0], xTicks[1] + xTicks[2], xTicks[2])
        xticks = np.round(xticks, 4)
        self.axes.set_xticks(xticks)
        self.axes.set_xticklabels([str(tick * xDisplay[0]) + xDisplay[1] for tick in xticks], fontsize=fontSize, color="black")

        yticks = np.arange(yTicks[0], yTicks[1] + yTicks[2], yTicks[2])
        yticks = np.round(yticks, 2)
        self.axes.set_yticks(yticks)
        self.axes.set_yticklabels([str(tick * yDisplay[0][0]) + yDisplay[0][1] for tick in yticks], fontsize=fontSize, color="black")
        self.axes.spines['left'].set_color(yDisplay[0][2])
        
        if len(yDisplay) > 1:
            yticks = np.arange(yTicks[0], yTicks[1] + 1, yTicks[2])
            axes2 = self.axes.twinx()
            axes2.spines['right'].set_color(yDisplay[1][2])
            axes2.set_yticks(yticks)
            axes2.set_yticklabels([str(tick * yDisplay[1][0]) + yDisplay[1][1] for tick in yticks], fontsize=fontSize, color="black")
            axes2.yaxis.set_label_position("right")

            self.axes.vlines(xTicks[0] - xMargin, yTicks[0] - yMargin, yTicks[1] + yMargin, colors=yDisplay[0][2], linewidth=4)
            self.axes.vlines(xTicks[1] + xMargin, yTicks[0] - yMargin, yTicks[1] + yMargin, colors=yDisplay[1][2], linewidth=4)



    def addPlot(self, time: tuple, f: Callable, colour: str, lineWidth: int = 2, numPoints: int = 250, noiseBase: float = 0.02, bridgePoint: float = None):
        """Adds a plot to the subplot
        
        This method adds a plot to the subplot.
        
        Args:
            time (tuple): The time range.
            f (function): The function to plot.
            colour (str): The colour of the plot.
            lineWidth (float): The width of the line.
            numPoints (int): The number of points to plot.
            noiseBase (float): The base noise level.
            bridgePoint (float): Sets the last point of the plot to be the point
        """
        xData = np.linspace(time[0], time[1], numPoints)
        yData = f(xData)
        
        if bridgePoint is not None:
            yData[-1] = bridgePoint

        yData = self.addNoise(yData, noiseBase)
    
        self.axes.plot(xData, yData, color=colour, linewidth=lineWidth)
        

    def addNoise(self, data: np.array, noiseMagnitude: int):
        """Adds noise to the data

        This method adds noise to the data.

        Args:
            data (np.array): The data to add noise to.
            noiseMagnitude (int): The maximum magnitude of the noise.
        """

        if data is None:
            return None
        
        for i in range(len(data)):
            u1 = random.random();
            u2 = random.random();
            z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.pi * u2);
            noiseOffset = noiseMagnitude * z;
            data[i] += noiseOffset

        return data