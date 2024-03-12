import torch
import yaml
import numpy as np
epochs = 100
it_per_epoch = 100

# read yaml as dict
with open('/data/users/litianhao/S2ADet/project/base/train/exp3/hyp.yaml') as f:
    hyp = yaml.safe_load(f)

lf = lambda x: (1 - x / (epochs-1) ) ** 0.9

nw = max(it_per_epoch * hyp['warmup_epochs'], 1000)

lr0_list = []
lr2_list = []
lf_list = []
start_epoch = 0
for epoch in range(start_epoch, epochs):
    for i in range(it_per_epoch):
        ni = i + epoch * it_per_epoch
        if ni<=nw:
            xi = [0, nw]
            lr2 = np.interp(ni, xi, [hyp['warmup_bias_lr'] , hyp['lr0'] * lf(epoch)])
            lr0 = np.interp(ni, xi, [0 , hyp['lr0'] * lf(epoch)])
        else:
            lr2 = hyp['lr0'] * lf(epoch)
            lr0 = hyp['lr0'] * lf(epoch)
        lr0_list.append(lr0)
        lr2_list.append(lr2)
        # lf_list.append(lf(epoch))

# plot
import matplotlib.pyplot as plt
plt.plot(lr0_list)
plt.plot(lr2_list)
plt.plot(lf_list)
plt.xlabel('epoch')

# label
plt.legend(['lr0', 'lr2', 'lf'])

# save plot
plt.savefig('/data/users/litianhao/S2ADet/debug.png')