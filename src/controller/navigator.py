import pybullet as p
import math


class Navigator:
    def __init__(self, robot_id, path):
        self.robot_id = robot_id
        self.path = path
        self.index = 0

        self.wheels_left = [2, 4]
        self.wheels_right = [3, 5]

    def get_pose(self):
        pos, orn = p.getBasePositionAndOrientation(self.robot_id)
        yaw = p.getEulerFromQuaternion(orn)[2]
        return pos[0], pos[1], yaw

    def move(self):

        if self.index >= len(self.path):
            self.stop()
            return True

        gx, gy = self.path[self.index]

        x, y, yaw = self.get_pose()

        dx = gx - x
        dy = gy - y

        dist = math.sqrt(dx**2 + dy**2)

        if dist < 0.35:
            self.index += 1
            return False

        target = math.atan2(dy, dx)
        error = target - yaw

        while error > math.pi:
            error -= 2 * math.pi
        while error < -math.pi:
            error += 2 * math.pi

        # Turn first if large angle
        if abs(error) > 0.4:
            left = -3 * error
            right = 3 * error
        else:
            forward = 6
            turn = 2.5 * error
            left = forward - turn
            right = forward + turn

        self.drive(left, right)
        return False

    def drive(self, left, right):

        for j in self.wheels_left:
            p.setJointMotorControl2(
                self.robot_id, j,
                p.VELOCITY_CONTROL,
                targetVelocity=left,
                force=80
            )

        for j in self.wheels_right:
            p.setJointMotorControl2(
                self.robot_id, j,
                p.VELOCITY_CONTROL,
                targetVelocity=right,
                force=80
            )

    def stop(self):
        self.drive(0, 0)