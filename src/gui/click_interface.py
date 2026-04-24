import cv2
import numpy as np


class ClickGUI:
    def __init__(self):
        self.map_size = 600
        self.scale = 50

        self.start = None
        self.goal = None

    def world_to_pixel(self, x, y):
        px = int(self.map_size / 2 + x * self.scale)
        py = int(self.map_size / 2 - y * self.scale)
        return px, py

    def pixel_to_world(self, px, py):
        x = (px - self.map_size / 2) / self.scale
        y = -(py - self.map_size / 2) / self.scale
        return round(x, 2), round(y, 2)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:

            wx, wy = self.pixel_to_world(x, y)

            if self.start is None:
                self.start = (wx, wy)
                print("Start:", self.start)

            elif self.goal is None:
                self.goal = (wx, wy)
                print("Goal:", self.goal)

    def draw_grid(self, img):

        for i in range(0, self.map_size, 50):
            cv2.line(img, (i, 0), (i, self.map_size), (220, 220, 220), 1)
            cv2.line(img, (0, i), (self.map_size, i), (220, 220, 220), 1)

        # center axis
        cv2.line(img, (300, 0), (300, 600), (0, 0, 0), 2)
        cv2.line(img, (0, 300), (600, 300), (0, 0, 0), 2)

    def draw(self):
        img = np.ones((600, 600, 3), dtype=np.uint8) * 255

        self.draw_grid(img)

        cv2.putText(img, "Click GREEN start then RED goal",
                    (120, 25),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 0, 0), 2)

        cv2.putText(img, "Center = (0,0)",
                    (240, 580),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 0, 0), 1)

        if self.start:
            px, py = self.world_to_pixel(*self.start)
            cv2.circle(img, (px, py), 8, (0, 255, 0), -1)

        if self.goal:
            px, py = self.world_to_pixel(*self.goal)
            cv2.circle(img, (px, py), 8, (0, 0, 255), -1)

        cv2.imshow("Select Start and Goal", img)

    def run(self):
        cv2.namedWindow("Select Start and Goal")
        cv2.setMouseCallback("Select Start and Goal", self.mouse_callback)

        while True:
            self.draw()

            key = cv2.waitKey(10)

            if self.start and self.goal:
                break

            if key == 27:
                break

        cv2.destroyAllWindows()
        return self.start, self.goal