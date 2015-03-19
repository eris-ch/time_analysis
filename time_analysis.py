
from cyclic_processes import *

[events,trajectories] = pickle.load(open('all_timestamps.pkl','rb'))
       
#for roi in trajectories:
#    if trajectories[roi]!=[]:

roi = trajectories.keys()[7] # available: 1,3-9
timestamps_vec, ind = time_wrap(trajectories[roi])

dyn_cl = dynamic_clusters()
for t in range(len(timestamps_vec)):
    dyn_cl.add_element(t+1,timestamps_vec[t])

## NOTE: interval (bin size) is 1800 (1/2 hour) by default, but if the data are very sparse you can increase it
fitting = activity_time(timestamps_vec,interval=1800.0)

# querying the fitting of new data x:
# p = fitting.query_model(x%86400)
# example below
pc = []
pf = []
for v in timestamps_vec:
    pc.append(dyn_cl.query_clusters(v))
    pf.append(fitting.query_model(v))

plt.plot(timestamps_vec,pc,label='dynamic clustering')
plt.plot(timestamps_vec,pf,label='GMM fitting')
plt.xlabel('samples')
plt.ylabel('probability')

plt.legend()
click = plt.waitforbuttonpress() # close plot with keypress
plt.close()

