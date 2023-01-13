import numpy as np

import geolab as geo

'''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 TUTORIAL 2: RENDER DATA ON A MESH
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''

# -----------------------------------------------------------------------------
# READ A MESH
# -----------------------------------------------------------------------------

V, F = geo.read_mesh('data/dino.obj')


# -----------------------------------------------------------------------------
# INITIALIZE THE PLOTTER
# -----------------------------------------------------------------------------

plotter = geo.figure()

plotter.size = (2500, 2500)  # set the size of the image

plotter.path = 'ex_2'  # the folder where the images are saved

plotter.position_name = 'pos_1'  # the file name of the camera position


# -----------------------------------------------------------------------------
# PLOT FACE DATA
# -----------------------------------------------------------------------------

data = np.random.random(len(F))

lut_range = [np.min(data), np.max(data)]

plotter.plot_faces(V, F, face_data=data, lut_range=lut_range, color='plasma',
                   smooth=False)

plotter.name = '1_face_data'  # the file name of the image to be saved

plotter.set_view()

plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT VERTEX DATA
# -----------------------------------------------------------------------------

plotter.clear_figure()  # clear previous plots

data = V[:, 2]  # get the z coordinate of each vertex as data to show

lut_range = [np.min(data), np.max(data)]

plotter.plot_faces(V, F, vertex_data=data, lut_range=lut_range, color='plasma',
                   smooth=False)

plotter.name = '2_vertex_data'  # the file name of the image to be saved

#plotter.set_view()

plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT EDGE DATA
# -----------------------------------------------------------------------------

plotter.clear_figure()  # clear previous plots

H = geo.halfedges(F)  # makes the halfedges array

E = geo.edges(H)  # extract the edges (igl.edges(F) can be used instead)

data = np.random.random(len(E))

lut_range = [np.min(data), np.max(data)]

plotter.plot_edges(V, F, edge_data=data, lut_range=lut_range, color='plasma',
                   tube_radius=0.05)

plotter.plot_faces(V, F, color='w', smooth=False)

plotter.name = '3_edge_data'  # the file name of the image to be saved

#plotter.set_view()

plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT DATA AT POINTS
# -----------------------------------------------------------------------------

plotter.clear_figure()  # clear previous plots

data = V[:, 2]

lut_range = [np.min(data), np.max(data)]

plotter.plot_points(V, vertex_data=data, lut_range=lut_range, color='plasma',
                    radius=0.1)

plotter.plot_faces(V, F, color='w', smooth=False)

plotter.name = '4_points'  # the file name of the image to be saved

#plotter.set_view()

plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT VECTORS AT VERTICES
# -----------------------------------------------------------------------------

plotter.clear_figure()  # clear previous plots

vectors = np.random.random((len(V), 3))

plotter.plot_vectors(vectors, anchor=V, color='plasma', scale_factor=1,
                     position='head')  # position can be 'head', 'tail', or 'center'.

plotter.plot_faces(V, F, color='w', smooth=False)

plotter.name = '5_vectors'  # the file name of the image to be saved

#plotter.set_view()

plotter.save_figure()

