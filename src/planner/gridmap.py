class GridMap:
    def __init__(self):
        self.resolution = 0.5
        self.size = 12   # world from -6 to +6

        self.width = int(self.size / self.resolution)
        self.height = int(self.size / self.resolution)

        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        self.add_obstacles()

    def world_to_grid(self, x, y):
        gx = int((x + 6) / self.resolution)
        gy = int((y + 6) / self.resolution)
        return gx, gy

    def grid_to_world(self, gx, gy):
        x = gx * self.resolution - 6
        y = gy * self.resolution - 6
        return x, y

    def mark_box(self, cx, cy, size=1.5):
        half = size / 2

        x1, y1 = self.world_to_grid(cx - half, cy - half)
        x2, y2 = self.world_to_grid(cx + half, cy + half)

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.grid[y][x] = 1

    def add_obstacles(self):
        self.mark_box(2, 2)
        self.mark_box(-2, 1)
        self.mark_box(0, -2)