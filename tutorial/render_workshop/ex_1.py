import geolab as geo

'''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 TUTORIAL 1: RENDER A MESH
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

plotter.path = 'ex_1'  # the folder where the images are saved

plotter.position_name = 'pos_1'  # the file name of the camera position

plotter.name = 'img_1'  # the file name of the image to be saved


# -----------------------------------------------------------------------------
# PLOT THE MESH
# -----------------------------------------------------------------------------

plotter.plot_faces(V, F, color='cornflower', smooth=False, glossy=0.5)

plotter.plot_edges(V, F, color='k', tube_radius=0.005, glossy=0)


# -----------------------------------------------------------------------------
# SET THE CAMERA POSITION AND SAVE THE IMAGE
# -----------------------------------------------------------------------------

plotter.set_view()

plotter.save_figure()
