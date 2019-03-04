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
fig = plt.figure(figsize=[10.4, 7.8])
x1, dens1, t1, last_checkpoint1 = file_opener('./rodeo_v20_o100.h5')
print('Plotting ' + last_checkpoint1 + ' at t = {}'.format(t1))
plt.plot(x1[33:45, 0], np.mean(dens1[33:45,:], axis=1), 'r', label ='After 100 orbits')
# print(x1[25:45,0])
# print(dens1[25:45,:].shape)

x2, dens2, t2, last_checkpoint2 = file_opener('./rodeo_v20_o200.h5')
print('Plotting ' + last_checkpoint2 + ' at t = {}'.format(t2))
plt.plot(x2[33:45, 0], np.mean(dens2[33:45,:], axis=1), 'b', label ='After 200 orbits')

plt.xlabel('Radial Distance r')
plt.ylabel('Vertically Averaged Surface Density')
plt.title('Simulation for 100 orbits with planet at $r_p=1$ and migration at 20% soundspeed')
plt.legend()
# plt.savefig('./Graphs/Results/steady_state.png')
plt.show()

