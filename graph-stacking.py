import numpy as np
import matplotlib.pyplot as plt
import h5py
#filenames = ['./output-6_3.h5', './rodeo_v20_o100.h5']
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

x1, dens1, t1, last_checkpoint1 = file_opener('./o05_30prcnt.h5')
print('Plotting ' + last_checkpoint1 + ' at t = {}'.format(t1))
plt.plot(x1[:, 0], np.mean(dens1, axis=1), 'k-', label ='At 5 orbits')

x2, dens2, t2, last_checkpoint2 = file_opener('./o10_30prcnt.h5')
print('Plotting ' + last_checkpoint2 + ' at t = {}'.format(t2))
plt.plot(x2[:, 0], np.mean(dens2, axis=1), 'k--', label ='At 10 orbits')

x3, dens3, t3, last_checkpoint3 = file_opener('./o25_30prcnt.h5')
print('Plotting ' + last_checkpoint3 + ' at t = {}'.format(t3))
plt.plot(x3[:, 0], np.mean(dens3, axis=1), 'k^:', markevery=10, label ='At 25 orbits')

x4, dens4, t4, last_checkpoint4 = file_opener('./o50_30prcnt.h5')
print('Plotting ' + last_checkpoint4 + ' at t = {}'.format(t4))
plt.plot(x4[:, 0], np.mean(dens4, axis=1), 'k:', label ='At 50 orbits')


#
# x1, dens1, t1, last_checkpoint1 = file_opener('./o100_50prcnt.h5')
# print('Plotting ' + last_checkpoint1 + ' at t = {}'.format(t1))
# plt.plot(x1[:, 0], np.mean(dens1, axis=1), 'k-', label ='Jupiter-mass planet at $r_p = 1$')
#
# x2, dens2, t2, last_checkpoint2 = file_opener('./noplanet_o100_50prcnt.h5')
# print('Plotting ' + last_checkpoint2 + ' at t = {}'.format(t2))
# plt.plot(x2[:, 0], np.mean(dens2, axis=1), 'k--', label ='Reference unperturbed density profile')

plt.xlabel('Radial Distance r',fontsize=14)
plt.ylabel('Vertically Averaged Surface Density',fontsize=14)
# plt.suptitle('Simulation for 100 orbits',fontsize=16, weight='bold')
plt.title('Evolution of surface density with Jupiter-mass planet at $r_p = 1$: \n Migration speed = 30% of sound-speed',fontsize=16)
plt.legend(prop={'size': 14})
# plt.savefig('./Results/diff_orbits.png')
plt.show()

