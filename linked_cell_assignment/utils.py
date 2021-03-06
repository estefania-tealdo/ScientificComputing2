import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams, patches
import time
from itertools import product
import math

def lj_potential(distance, c1=1e-15, c2=1e-5):
    return   (c1 / distance**12) - (c2 / distance**6)

def get_successor_neighbor_delta_coordinate(a=1):
    """Returns neighbor_delta_coordinate

    Parameters
    ---------
    a: int
        Variable linked-cell parameter
    """

    neighbor_delta_coordinate = []
    ############# Task 1.1 begins ##################
    for i in range(0,a):
        for j in range(0,a):
            #if distance of [1,1] amd [i,j] is less than a
            if ( math.sqrt(( (0+i)-(0+1) )**2 + ((0+j)-(0+1))**2) < a ):
                neighbor_delta_coordinate.append(np.array([i,j]))

    ############ Task 1.1 ends #####################
    return neighbor_delta_coordinate

def plot_all_cells(ax, list_cells, edgecolor='r',domain=1):
    for c in list_cells:
        c.plot_cell(ax, edgecolor=edgecolor)
    ax.tick_params(axis='both',labelsize=0, length = 0)
    plt.xlim(left=0, right=domain)
    plt.ylim(bottom=0, top=domain)
    ax.set_aspect('equal', adjustable='box')

def get_mean_relative_error(direct_potential, linked_cell_potential):
    return np.mean(np.abs((direct_potential - linked_cell_potential) / direct_potential))


testlst = get_successor_neighbor_delta_coordinate(a=3)
testlst
