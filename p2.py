import snap
import numpy as np
import matplotlib.pyplot as plt

# P2 of HW1

G1 = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
CntV = snap.TIntPrV()
snap.GetOutDegCnt(G1, CntV)
degs = {}
for p in CntV:
	deg = p.GetVal1()
	degs[deg] = p.GetVal2()
ps = sorted(degs.items())
fig = plt.figure ()
ax = fig.add_subplot(111)
ax.scatter([k for (k,v) in ps], [v for (k,v) in ps])
ax.set_xscale ('log')
ax.set_yscale ('log')
plt.xlim((1e-1,1e3))
plt.ylim((1e-1,1e4))
plt.title("Distribution of out-degree of nodes in the network")
fig.savefig("p2.png")