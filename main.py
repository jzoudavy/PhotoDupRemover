import cv2
import numpy as np
import os
import time


# return list of pics and only pics. no videos
def generateFileList(param):
    a = [name for name in os.listdir(r"C:\Users\jhg\Pictures\old_picture_dump") if (name.endswith(".jpeg") or name.endswith(".JPG") or name.endswith(".jpg"))  ]

    return a


def main():
    root_path=r"C:\Users\jhg\Pictures\old_picture_dump"

    image_list=generateFileList(root_path)

    # Define a function to compute the Mean Squared Error between two images.

    for image in image_list:
        image_path1=os.path.join(root_path,image)
        img1 = cv2.imread(image_path1)
        for image in image_list:
            image_path2 = os.path.join(root_path, image)
            if image_path1 != image_path2:
                img2 = cv2.imread(image_path2)


                if img1.shape == img2.shape:
                    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)




                    h, w = img1.shape
                    diff = cv2.subtract(img1, img2)
                    err = np.sum(diff ** 2)
                    mse = err / (float(h * w))
                    print("Image matching Error between the two images:", mse)
                    print("image 1:", image_path1)
                    print("image 2:", image_path2)
                #else we skip the compare

'''
possible ways to speed this thing up
1. multithread it
2. make it use the gpu
3. run it on nvidia jetson nano, but network latency? connect nano to switch maybe?
4. 
'''
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    print("time elapsed: {:.2f}s".format(time.time() - start_time))
