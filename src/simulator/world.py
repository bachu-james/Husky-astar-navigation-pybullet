import pybullet as p
import pybullet_data
import time


class World:
    def __init__(self):
        self.client = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

    def load_environment(self):
        p.loadURDF("plane.urdf")

        self.create_box([2, 2, 0.5], [1, 1, 1])
        self.create_box([-2, 1, 0.5], [1, 1, 1])
        self.create_box([0, -2, 0.5], [1, 1, 1])

        p.resetDebugVisualizerCamera(
            cameraDistance=10,
            cameraYaw=0,
            cameraPitch=-89,
            cameraTargetPosition=[0, 0, 0]
        )

    def create_box(self, pos, size):
        collision = p.createCollisionShape(
            p.GEOM_BOX,
            halfExtents=[size[0]/2, size[1]/2, size[2]/2]
        )

        visual = p.createVisualShape(
            p.GEOM_BOX,
            halfExtents=[size[0]/2, size[1]/2, size[2]/2],
            rgbaColor=[1, 0, 0, 1]
        )

        p.createMultiBody(
            baseMass=0,
            baseCollisionShapeIndex=collision,
            baseVisualShapeIndex=visual,
            basePosition=pos
        )

    def create_marker(self, pos, color):
        visual = p.createVisualShape(
            p.GEOM_SPHERE,
            radius=0.2,
            rgbaColor=color
        )

        p.createMultiBody(
            baseMass=0,
            baseVisualShapeIndex=visual,
            basePosition=pos
        )

    def draw_path(self, path):
        for i in range(len(path) - 1):
            p.addUserDebugLine(
                [path[i][0], path[i][1], 0.1],
                [path[i+1][0], path[i+1][1], 0.1],
                [0, 1, 0],
                3
            )

    def step(self):
        p.stepSimulation()
        time.sleep(1 / 240)