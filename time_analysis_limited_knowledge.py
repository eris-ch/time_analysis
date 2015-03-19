import cPickle as pickle
from cyclic_processes import *

[events,trajectories] = pickle.load(open('all_timestamps.pkl','rb'))
       
#for roi in trajectories:
#    if trajectories[roi]!=[]:

region = 6 # available: 1,3-9
roi_traj = trajectories.keys()[region]
roi_view = events.keys()[region]

traj_ts, ind = time_wrap(trajectories[roi_traj])
view_ts, ind = time_wrap(events[roi_view])

dyn_cl = dynamic_clusters()
for t in range(len(traj_ts)):
    dyn_cl.add_element(t+1,traj_ts[t])

interval = 1800.0 # interval (bin size) is 1800 (1/2 hour) by default, but if the data are very sparse you can increase it
period = 86400.0
n_bins = int(period/interval)

fitting = activity_time(traj_ts,period,interval)

know = binning(view_ts,n_bins,interval)
know = [float(k)/max(know) for k in know]

# querying the fitting of new data x:
# p = fitting.query_model(x%86400)
# example below
pc = []
pf = []
for v in traj_ts:
    pc.append(dyn_cl.query_clusters(v))
    pf.append(fitting.query_model(v))

plt.plot(traj_ts,pc,label='dynamic clustering')
plt.plot(traj_ts,pf,label='GMM fitting')
plt.plot(np.arange(0,period+1,interval),know,label='knowledge')
plt.xlabel('samples')
plt.ylabel('probability')
plt.legend()
#click = plt.waitforbuttonpress() # close plot with keypress
#plt.close()

