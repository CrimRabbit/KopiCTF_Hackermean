import matplotlib.pyplot as plt
import numpy as np
import sys

g= [[1,1,1,1,1,1,1,0],
 [1,0,0,0,0,0,1,0],
 [1,0,1,1,1,0,1,0],
 [1,0,1,1,1,0,1,0],
 [1,0,1,1,1,0,1,0],
 [1,0,0,0,0,0,1,0],
 [1,1,1,1,1,1,1,0],
 [0,0,0,0,0,0,0,0]]

# Solution produces tiny image, but no border
# fig = plt.imshow(g, cmap='Greys')
# plt.axis('off')
# plt.imsave('blkwht.png',g,format="png",cmap="Greys")

#Solution has a 2px border
fig = plt.imshow(g, cmap='Greys')
plt.axis('off')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.savefig('blkwht.png', bbox_inches='tight', pad_inches = 0)

plt.show()