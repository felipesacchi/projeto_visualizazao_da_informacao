import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
collection = mpl.collections.StarPolygonCollection(
    5, 0, [250, ],  # five point star, zero angle, size 250px
    offsets=np.column_stack([x, y]),  # Set the positions
    transOffset=ax.transData,  # Propagate transformations of the Axes
)
ax.add_collection(collection)
ax.autoscale_view()