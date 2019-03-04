import numpy as np
import matplotlib.pyplot as plt
import h5py
with h5py.File('./rodeo.h5', "r") as hf:  # output-6_2.h5
    # Select last available checkpoint
    last_checkpoint = None
    # print(hf.keys())
    for k in hf.keys():
        # print(k)
        if (k != 'coords' and k != 'param'):
            last_checkpoint = k
    # Get x coordinate
    gc = hf.get('coords')
    x = np.array(gc.get('x'))
    # Get density
    g = hf.get(last_checkpoint)
    dens = np.array(g.get('dens'))
    # Simulation time at checkpoint
    t = g.attrs['time']
    print('Plotting ' + last_checkpoint + ' at t = {}'.format(t))
    plt.plot(x[:, 0], np.mean(dens, axis=1))
    plt.xlabel('Radial Distance r')
    plt.ylabel('Vertically Averaged Surface Density')
    plt.title('Simulation for 100 orbits at migration of 50% soundspeed ')
    # plt.savefig('./Graphs/Results/graph_0.001planet_100orbit_50prcnt.png')
    plt.show()

