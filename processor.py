import statistics

import matplotlib.image as image


class Processor:

    def __init__(self, img):
        self.img = image.imread(img).copy()
        self.width, self.height, self.depth = self.img.shape

    def to_black_and_white(self, threshold=150):
        white = [255, 255, 255]
        black = [0, 0, 0]
        for x in range(self.width):
            for y in range(self.height):
                mean = statistics.fmean(self.img[x][y])
                self.img[x][y] = black if mean < threshold else white

    def to_greyscale(self):
        for x in range(self.width):
            for y in range(self.height):
                mean = statistics.fmean(self.img[x][y])
                self.img[x][y] = [mean] * self.depth

    def keep_one_colour(self, colour, threshold):
        mean_colour = statistics.fmean(colour)
        for x in range(self.width):
            for y in range(self.height):
                mean_img = statistics.fmean(self.img[x][y])
                if abs(mean_img - mean_colour) > threshold:
                    self.img[x][y] = [255] * self.depth