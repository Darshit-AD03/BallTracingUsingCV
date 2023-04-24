import math
import pandas as pd


df = pd.DataFrame()

max_range = 100  # cm

plane = []
coordinates = (0, 0)  # just for reference

for x in range(max_range * 1000):

    coordinates = (0, 0)  # just for reference

    distance_from_camera_plane = x / 1000  # this distance is in cm
    distance_from_camera_to_ball = 0

    # here add function that takes frame as input and return coordinates of ball in that frame(2d coordinates) and
    # distance of ball from camera

    angle_between_two_lines = math.acos(distance_from_camera_plane / distance_from_camera_to_ball)

    plane.append([coordinates, distance_from_camera_plane, distance_from_camera_to_ball])


