import numpy as np
import matplotlib.pyplot as plt
import h5py
def file_opener(filenames):
    with h5py.File(filenames, "r") as hf:  # output-6_2.h5
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
        return (x, dens, t, last_checkpoint)
# fig = plt.figure(figsize=[10.4, 7.8])
fig = plt.figure(figsize=[8,6])
x1, dens1, t1, last_checkpoint1 = file_opener('./o100_30prcnt.h5')
print('Plotting ' + last_checkpoint1 + ' at t = {}'.format(t1))
plt.plot(x1[33:45, 0], np.mean(dens1[33:45,:], axis=1), 'k-', label ='After 100 orbits')
# print(x1[25:45,0])
# print(dens1[25:45,:].shape)

x2, dens2, t2, last_checkpoint2 = file_opener('./o200_30prcnt.h5')
print('Plotting ' + last_checkpoint2 + ' at t = {}'.format(t2))
plt.plot(x2[33:45, 0], np.mean(dens2[33:45,:], axis=1), 'k:', label ='After 200 orbits')

plt.xlabel('Radial Distance r',fontsize=14)
plt.ylabel('Vertically Averaged Surface Density',fontsize=14)
plt.title('Jupiter-mass planet at $r_p = 1$: \n Migration speed = 30% of sound-speed',fontsize=16)
plt.legend(prop={'size': 14})
plt.savefig('./Results/steady_state.png')
plt.show()

