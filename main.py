import cv2
import numpy as np
import os


# return list of pics and only pics. no videos
def generateFileList(param):
    a = [name for name in os.listdir(".") if (name.endswith(".jpeg") or name.endswith(".JPG") or name.endswith(".jpg"))  ]
    print(len(a))
    return a


def main():

    image_list=generateFileList(r"C:\Users\jhg\Pictures\old_picture_dump")

    # Define a function to compute the Mean Squared Error between two images.

    img1 = cv2.imread(r"C:\Users\jhg\Pictures\old_picture_dump\20160326_181531.jpg")
    img2 = cv2.imread(r"C:\Users\jhg\Pictures\old_picture_dump\20160326_194640.jpg")
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # get dimensions of image
    dimensions1 = img1.shape

    # height, width, number of channels in image
    height1 = img1.shape[0]
    width1 = img1.shape[1]

    # get dimensions of image
    dimensions2 = img2.shape

    # height, width, number of channels in image
    height2 = img2.shape[0]
    width2 = img2.shape[1]

    if height2==height1 and width2 == width1:

        h, w = img1.shape
        diff = cv2.subtract(img1, img2)
        err = np.sum(diff ** 2)
        mse = err / (float(h * w))
        print("Image matching Error between the two images:", mse)
    else:
        print("different dimensions skipped compare")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
