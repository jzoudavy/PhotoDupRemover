import cv2
import numpy as np
import os
import threading
import time
import random

class myThread (threading.Thread):
   def __init__(self, name, *args):
      threading.Thread.__init__(self)
      self.threadID =  random.randrange(1000, 10000, 2)
      self.name = name
      self.args = args
   def run(self):
      print("Starting " + self.name)
      compareImage(self.args[0], self.args[1])
      print("Exiting " + self.name)



    # Define a function to compute the Mean Squared Error between two images.
def compareImage(image_path1, image_path2):
    img2 = cv2.imread(image_path2)
    img1 = cv2.imread(image_path1)

    if img1.shape == img2.shape:
        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        h, w = img1.shape
        diff = cv2.subtract(img1, img2)
        err = np.sum(diff ** 2)
        mse = err / (float(h * w))

        print("Image matching Error between the two images:", mse)index1
        print("image 1:", image_path1)
        print("image 2:", image_path2)
    else:
        print("Didn't compare.")

# return list of pics and only pics. no videos
def generateFileList(root_path):
    a = [name for name in os.listdir(root_path) if (name.endswith(".jpeg") or name.endswith(".JPG") or name.endswith(".jpg") or name.endswith(".png"))  ]
    print(a)
    return a


def main():
    root_path=r"C:\Users\jhg\Pictures\old_picture_dump"
    root_path=r"/home/blast/Pictures/Wallpapers"

    image_list=generateFileList(root_path)


    for index1,image in enumerate(image_list):
        image_path1=os.path.join(root_path,image)

        for index2, image in enumerate(image_list):
            image_path2 = os.path.join(root_path, image)
            if image_path1 != image_path2:
                # Create new threads
                thread1 = myThread("Thread-"+image, image_path1, image_path2)

                # Start new Threads
                thread1.start()




'''
possible ways to speed this thing up
single thread i think takes 4s
1. multithread it
1a: one for loop per thread execution time of 0.38s for 4 pics
1b: two for loop per thread execution time is 0.02s for 4 pics
2. make it use the gpu
3. run it on nvidia jetson nano, but network latency? connect nano to switch maybe?
3a: maybe move all the pics to the jetson nano, then do the compare and delete, then put them back?
4. 
'''
if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()

    print("time elapsed: {:.2f}s".format(time.time() - start_time))
