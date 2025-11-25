from Subplot import Subplot
import numpy as np
import matplotlib.pyplot as plt

"""
    Plot class
    Effectively a wrapper for the plt.Figure class,
    However, plt.figure has some weird behaviour when you make a child class.

    Each plot is initilised as a grid of SubPlots
"""
class Plot():
    def __init__(self, gridSize: tuple, figSize: tuple):    
        self.fig = plt.figure(figsize=figSize, dpi=200)
        self.gridSize = gridSize
        self.subplots = []
        self.fig.tight_layout()

        self.format()

    def format(self):
        self.fig.set_facecolor("#e7f3f5")


    def addSubplot(self):
        """ Add a subplot to the plot

        Adds to the grid from left to right, top to bottom

        Returns:
            Subplot: The subplot that was added
        """
        axes = self.fig.add_subplot(self.gridSize[0], self.gridSize[1], len(self.subplots) + 1)
        subplot = Subplot(len(self.subplots), axes, self.gridSize)
        
        self.subplots.append(subplot)
        return subplot

    def showPlot(self):
        """ Show the plot in a new window       
        """
        if len(self.subplots) == 0:
            ValueError("No subplots added to plot")
            return

        if len(self.subplots) < self.gridSize[0] * self.gridSize[1]:
            Warning("Not all subplots have been added to the plot")
      
        plt.show()
        

    def savePlot(self, path: str):
        self.fig.savefig(path, bbox_inches='tight', dpi=200)
        # self.close()