#!/usr/bin/env python3

# A basic example of using KokoInterface for cartesian pose control.
# This script allows the user to record four cartesian poses by manually moving the arm to each
# pose and pressing enter. It then plays the four poses back in an infinite loop.

from koko_interface import KokoInterface
import numpy as np

koko = KokoInterface("hekate.cs.berkeley.edu")
koko.disable_control()

recorded_poses = []

position_error_threshold = 0.05
orientation_error_threshold = 0.5

for _ in range(4):
    input("Press enter to record current pose.")
    recorded_poses = np.append(recorded_poses, koko.get_cartesian_pose())

input("Press enter to start the trajectory!")

while True:
    for des_pose in recorded_poses:
        curr_pose = koko.get_cartesian_pose()
        curr_position = curr_pose["position"]
        curr_orientationation = curr_pose["orientation"]

        des_position = des_pose["position"]
        des_orientation = des_pose["orientation"]

        position_error = np.linalg.norm(des_position - curr_position)
        orientation_error = np.linalg.norm(des_orientation - curr_orient)

        while position_error > position_error_threshold or orientation_error > orientation_error_threshold:
            koko.set_cartesian_pose(des_pose)
            curr_pose = koko.get_cartesian_pose()
            curr_position = curr_pose["position"]
            curr_orientationation = curr_pose["orientation"]
