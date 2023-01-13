import numpy as np

import geolab as geo

'''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 TUTORIAL 3: RENDER A KNOT
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''

# -----------------------------------------------------------------------------
# READ A MESH
# -----------------------------------------------------------------------------

P = geo.read_polyline('data/torus_knot.obj')


# -----------------------------------------------------------------------------
# INITIALIZE THE PLOTTER
# -----------------------------------------------------------------------------

plotter = geo.figure()

plotter.size = (2500, 2500)  # set the size of the image

plotter.path = 'ex_3'  # the folder where the images are saved

plotter.position_name = 'pos_1'  # the file name of the camera position


# -----------------------------------------------------------------------------
# MAKE A PIPE
# -----------------------------------------------------------------------------

V, F = geo.mesh_circular_pipe(P, radius=0.4, closed=True, vertex_normals=None,
                              comb=False)
# Notes:
# if 'vertex_normals' is 'None' and comb is 'False', Frenet frame is used.
# If 'comb' is 'True', a smooth normal field is computed (avoids twist at inflection points)
# if specified, vertex normals must lie in the

# -----------------------------------------------------------------------------
# PLOT THE MESH FACES
# -----------------------------------------------------------------------------

plotter.plot_faces(V, F, color='cornflower', smooth=True, glossy=0.5)

plotter.name = 'knot'  # the file name of the image to be saved

plotter.set_view()

plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT A PIPE WITH TWO COLORS
# -----------------------------------------------------------------------------

plotter.clear_figure()

sides = 64

V, F = geo.mesh_circular_pipe(P, radius=0.4, closed=True, vertex_normals=None,
                              comb=False, sides=sides)


data = np.repeat([0, 1], sides//2)

data = np.tile(data, len(P))

plotter.plot_faces(V, F, face_data=data, color=[(200, 200, 200), 'cornflower'],
                   lut_range=[0, 1], smooth=True, glossy=0.5)

plotter.name = 'knot_split'  # the file name of the image to be saved

# plotter.set_view()

# plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT VERTEX DATA
# -----------------------------------------------------------------------------

plotter.clear_figure()

sides = 64

V, F = geo.mesh_circular_pipe(P, radius=0.4, closed=True, vertex_normals=None,
                              comb=False, sides=sides)

data = np.tile(V[:, 2], sides)

lut_range = [np.min(data), np.max(data)]

plotter.plot_faces(V, F, vertex_data=data, color='plasma', lut_range=lut_range,
                   smooth=True)

plotter.name = 'knot_data'  # the file name of the image to be saved

#plotter.set_view()

#plotter.save_figure()


