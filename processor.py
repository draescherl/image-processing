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

    # def __surrounding_average(self, x, y):
    #     average = [0] * self.depth
    #     divisor = 0
    #     for i in range(-1, 2):
    #         for j in range(-1, 2):
    #             if (0 <= x + i < self.width) and (0 <= y + j < self.height):
    #                 for k in range(self.depth):
    #                     average[k] += self.img[x + i][y + j][k]
    #                 divisor += 1
    #     for k in range(self.depth):
    #         average[k] /= divisor
    #     return average

    def __surrounding_mean(self, x, y):
        surroundings = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    surroundings.append(statistics.fmean(self.img[x + i][y + j]))
                except IndexError:
                    pass
        return statistics.fmean(surroundings)

    def blur(self):
        copy = self.img.copy()
        for x in range(0, self.width):
            for y in range(0, self.height):
                copy[x][y] = self.__surrounding_mean(x, y)
        self.img = copy.copy()
