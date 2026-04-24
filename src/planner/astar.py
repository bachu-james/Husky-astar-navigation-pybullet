import heapq
import math


class AStarPlanner:
    def __init__(self, gridmap):
        self.map = gridmap

    def heuristic(self, a, b):
        return math.dist(a, b)

    def neighbors(self, node):
        x, y = node

        dirs = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (-1,-1), (1,-1), (-1,1)
        ]

        result = []

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.map.width and 0 <= ny < self.map.height:
                if self.map.grid[ny][nx] == 0:
                    result.append((nx, ny))

        return result

    def plan(self, start_world, goal_world):

        start = self.map.world_to_grid(*start_world)
        goal = self.map.world_to_grid(*goal_world)

        open_list = []
        heapq.heappush(open_list, (0, start))

        came_from = {}
        g_cost = {start: 0}

        while open_list:

            _, current = heapq.heappop(open_list)

            if current == goal:
                break

            for nb in self.neighbors(current):

                new_cost = g_cost[current] + self.heuristic(current, nb)

                if nb not in g_cost or new_cost < g_cost[nb]:
                    g_cost[nb] = new_cost
                    priority = new_cost + self.heuristic(nb, goal)

                    heapq.heappush(open_list, (priority, nb))
                    came_from[nb] = current

        path = []
        node = goal

        while node != start:
            path.append(self.map.grid_to_world(*node))
            node = came_from[node]

        path.append(start_world)
        path.reverse()

        return path