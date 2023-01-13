import numpy as np

import geolab as geo

'''
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
 TUTORIAL 5: MAKE AN ANIMATION
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''


# -----------------------------------------------------------------------------
# INITIALIZE THE PLOTTER
# -----------------------------------------------------------------------------

plotter = geo.figure()

plotter.size = (1400, 1080)  # set the size of the image

plotter.path = 'ex_5'  # the folder where the images are saved

plotter.position_name = 'pos_1'  # the file name of the camera position


# -----------------------------------------------------------------------------
# GENERATE DATA
# -----------------------------------------------------------------------------

V, F = geo.mesh_plane(200, 200, (-4, 4), (-4, 4))


# -----------------------------------------------------------------------------
# DEFINE AN ANIMATION CALLBACK
# -----------------------------------------------------------------------------

def make_frame(i, V, F):
    mu = V[:, 0]**2 + V[:, 1]**2
    V[:, 2] = 1/(1 + mu)**.5 * np.cos(mu + i/10)
    plotter.plot_faces(V, F, vertex_data=V[:, 2], lut_range=[-1, 1], color='plasma',
                       glossy=0.8, feature_angle=90)
    return i + 1, V, F


# -----------------------------------------------------------------------------
# SAVE THE FIGURE
# -----------------------------------------------------------------------------

plotter.make_animation(make_frame, 0, V, F, iterations=100, frame_rate=30, delay=0.06)

# frame rate: fps, delay: s
# duration = iterations * delay (if delay is None, delay = 1/frame_rate)


