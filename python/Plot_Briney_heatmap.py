#!/usr/bin/python
#
#
#

import os
import sys
import string
import gzip
import math
import numpy as np
#from numpy import *
#from pylab import *
import matplotlib
#matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class nlcmap(LinearSegmentedColormap):
    """A nonlinear colormap"""

    name = 'nlcmap'

    def __init__(self, cmap, levels):
        self.cmap = cmap
        self.monochrome = self.cmap.monochrome
        self.levels = asarray(levels, dtype='float64')
        self._x = self.levels-self.levels.min()
        self._x/= self._x.max()
        self._y = linspace(0, 1, len(self.levels))

    def __call__(self, xi, alpha=1.0, **kw):
        yi = interp(xi, self._x, self._y)
        return self.cmap(yi, alpha)


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap

    im = ax.imshow(data, vmin=0,vmax=1.0,**kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, shrink=0.3, **cbar_kw)
    cbar.ax.set_yticks([0.0,0.2,0.4,0.6,0.8,1.0])
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels,ha='center')

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=False, bottom=True, labeltop=False, labelbottom=True)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), ha="center",rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.set_ylabel("Amino Acids",ha='center')
    ax.set_xlabel("Position")
    ax.grid(which="minor", color="w", linestyle='-', linewidth=1)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.4f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)
    valfmtExp = matplotlib.ticker.StrMethodFormatter("{x:.0e}")
    
    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    fontSize=6
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) < threshold)])
            if data[i,j]<0.001:
                text = im.axes.text(j, i, valfmtExp(data[i, j], None), fontsize=fontSize,weight="bold",**kw)
            else:
                text = im.axes.text(j, i, valfmt(data[i, j], None), fontsize=fontSize,weight="bold",**kw)
            texts.append(text)

    return texts

def read_table(infile):
    pos=[]
    AA=[]
    table = np.array([])

    with open(infile,'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            dataline=line.rstrip().split()
            if "A" in dataline:
                AA=dataline[1:]

            else:
                pos.append(dataline[0])
                if len(table)==0:
                    table=np.array([float(x) for x in dataline[1:]])
                else:
                    table=np.vstack((table,np.array([float(x) for x in  dataline[1:]])))

    #print(table)
    return pos,AA,table

pos,AA,table=read_table('Briney.counts.Uniq.Functiona.20AA.txt')


fig, ax = plt.subplots(figsize=[8.2,8.2])
print(fig.get_size_inches())

#cmap_lin1 = cm.jet
#cmap_nonlin = nlcmap(cmap_lin1,table)
    
#im, cbar = heatmap(harvest, vegetables, farmers, ax=ax, cmap="YlGn", cbarlabel="harvest [t/year]")
#im, cbar = heatmap(table, pos, AA, ax=ax, cmap="YlGn", cbarlabel="harvest [t/year]")
#im, cbar = heatmap(table.transpose(), AA,pos, ax=ax, cmap="YlGn", cbarlabel="Fraction of Reads")
#im, cbar = heatmap(table.transpose(), AA,pos, ax=ax, cmap="bwr", cbarlabel="Fraction of Reads")
im, cbar = heatmap(table.transpose(), AA,pos, ax=ax, cmap="turbo", cbarlabel="Fraction of Reads")
#im, cbar = heatmap(table.transpose(), AA,pos, ax=ax, cmap=cmap_nonlin, cbarlabel="Fraction of Reads")
texts = annotate_heatmap(im, valfmt="{x:.3f}")

fig.tight_layout()

plt.savefig("Briney.counts.Uniq.Functional.20AA.V7.pdf",bbox_inches='tight')
plt.close("all")
