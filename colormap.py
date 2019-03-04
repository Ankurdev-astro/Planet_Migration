import numpy as np
import matplotlib.pyplot as plt
import h5py
with h5py.File('./o100_30prcnt.h5', "r") as hf:  # output-6_2.h5
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
    dens2D = np.squeeze(dens)
    # Simulation time at checkpoint
    t = g.attrs['time']
    print('Plotting ' + last_checkpoint + ' at t = {}'.format(t))
    plt.pcolormesh(dens2D)
    plt.xlabel(r'Averaged Surface Density along $\phi$')
    plt.ylabel(r'Averaged Surface Density along $r$')
    plt.suptitle('Relative Perturbation of Surface Density')
    plt.title('#Orbits: 100, No Migration')
    # plt.savefig('./Graphs/colormap_refGap.png')
    # plt.colorbar()
    plt.show()

