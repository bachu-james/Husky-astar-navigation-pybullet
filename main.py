from src.simulator.world import World
from src.simulator.robot import HuskyRobot
from src.gui.click_interface import ClickGUI
from src.controller.navigator import Navigator
from src.planner.gridmap import GridMap
from src.planner.astar import AStarPlanner
import math


def main():

    gui = ClickGUI()
    start, goal = gui.run()

    # Planner
    grid = GridMap()
    planner = AStarPlanner(grid)
    path = planner.plan(start, goal)

    # World
    world = World()
    world.load_environment()

    world.create_marker([start[0], start[1], 0.2], [0,1,0,1])
    world.create_marker([goal[0], goal[1], 0.2], [1,0,0,1])

    world.draw_path(path)

    # Spawn heading
    dx = path[1][0] - start[0]
    dy = path[1][1] - start[1]
    yaw = math.atan2(dy, dx)

    robot = HuskyRobot()
    robot_id = robot.load([start[0], start[1], 0.1], yaw)

    nav = Navigator(robot_id, path)

    while True:
        nav.move()
        world.step()


if __name__ == "__main__":
    main()