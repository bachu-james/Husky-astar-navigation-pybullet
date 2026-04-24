import pybullet as p
import pybullet_data
import math


class HuskyRobot:
    def __init__(self):
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

    def load(self, start_pos=[0,0,0.1], yaw=0):

        quat = p.getQuaternionFromEuler([0,0,yaw])

        self.robot_id = p.loadURDF(
            "husky/husky.urdf",
            start_pos,
            quat
        )

        return self.robot_id