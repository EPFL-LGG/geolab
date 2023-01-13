import numpy as np

import geolab as geo

'''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 TUTORIAL 4: RENDER A GRID SHELL
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''

# -----------------------------------------------------------------------------
# READ DATA
# -----------------------------------------------------------------------------

npz = np.load('data/gridshell.npz', allow_pickle=True)

P = npz['arr_0']  # list of np.array of vertices

N = - npz['arr_1']  # list of np.array per edge


# -----------------------------------------------------------------------------
# INITIALIZE THE PLOTTER
# -----------------------------------------------------------------------------

plotter = geo.figure()

plotter.size = (2500, 2500)  # set the size of the image

plotter.path = 'ex_4'  # the folder where the images are saved

plotter.position_name = 'pos_1'  # the file name of the camera position


# -----------------------------------------------------------------------------
# MAKE A RECTANGULAR PIPE AND PLOT IT
# -----------------------------------------------------------------------------

for i in range(len(P)):

    V, F, bf = geo.mesh_rectangular_pipe(P[i], N[i], height=0.2, width=0.4,
                                         closed=False, return_bottom_faces=True)

    data = np.zeros(len(F))

    data[bf] = 1

    plotter.plot_faces(V, F, face_data=data, color=['cornflower', (200, 200, 200)],
                       lut_range=[0, 1], smooth=True)

# -----------------------------------------------------------------------------
# SAVE THE FIGURE
# -----------------------------------------------------------------------------

plotter.name = 'gridshell'

plotter.set_view()

plotter.save_figure()


# -----------------------------------------------------------------------------
# CLOSE THE PIPES
# -----------------------------------------------------------------------------

plotter.clear_figure()

for i in range(len(P)):

    V, F, bf = geo.mesh_rectangular_pipe(P[i], N[i], height=0.2, width=0.4,
                                         closed=False, return_bottom_faces=True)

    H = geo.halfedges(F)

    H, fs = geo.fill_boundaries(H, return_face_shift=True)

    data = np.zeros(geo.number_of_faces(H))

    data[bf - fs] = 1

    plotter.plot_faces(V, H, face_data=data, color=['cornflower', (200, 200, 200)],
                       lut_range=[0, 1], smooth=True)


plotter.name = 'gridshell_closed'

plotter.position_name = 'pos_2'  # the file name of the camera position

#plotter.set_view()

#plotter.save_figure()


# -----------------------------------------------------------------------------
# PLOT VERTEX DATA
# -----------------------------------------------------------------------------

plotter.clear_figure()

for i in range(len(P)):

    V, F, bf = geo.mesh_rectangular_pipe(P[i], N[i], height=0.2, width=0.4,
                                         closed=False, return_bottom_faces=True)

    H = geo.halfedges(F)

    H, fs = geo.fill_boundaries(H, return_face_shift=True)

    data = np.tile(V[:, 2], 4)

    lut_range = [np.min(data), np.max(data)]

    plotter.plot_faces(V, H, vertex_data=data, color='plasma', lut_range=lut_range,
                       smooth=True)

plotter.name = 'gridshell_data'  # the file name of the image to be saved

#plotter.set_view()

#plotter.save_figure()
