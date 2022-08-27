import matplotlib.image as image
import matplotlib.pyplot as plt
import statistics


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


def main():
    p = Processor('inputs/apple.jpg')
    p.to_greyscale()
    plt.imshow(p.img)
    plt.show()


if __name__ == '__main__':
    main()
