import cv2
import numpy as np
import os
import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, *args):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.args = args
   def run(self):
      compareImage(self.args[0],self.args[1],self.args[2],self.args[3])



    # Define a function to compute the Mean Squared Error between two images.
def compareImage(img1, img2, image_path1, image_path2):
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    h, w = img1.shape
    diff = cv2.subtract(img1, img2)
    err = np.sum(diff ** 2)
    mse = err / (float(h * w))
    if mse > 5:
        print(f"Image matching Error between the two images is: {mse}. comparing {image_path1} and {image_path2}.")


# return list of pics and only pics. no videos
def generateFileList(root_path):
    a = [name for name in os.listdir(root_path) if (name.endswith(".jpeg") or name.endswith(".JPG") or name.endswith(".jpg") or name.endswith(".png"))  ]
    print(a)
    return a


def main():

    root_path=r"/home/blast/Pictures/Wallpapers"
    root_path = r"C:\Users\jhg\Pictures\old_picture_dump"

    image_list=generateFileList(root_path)


    for index1,image1 in enumerate(image_list):
        image_path1=os.path.join(root_path,image1)
        img1 = cv2.imread(image_path1)
        for index2,image2 in enumerate(image_list):
            image_path2 = os.path.join(root_path, image2)
            img2 = cv2.imread(image_path2)

            if image_path1 != image_path2 and img1.shape == img2.shape:
                while (threading.active_count() < 10):
                    thread1 = myThread(index2, "Thread-"+str(index2), img1, img2, image_path1, image_path2)
                    thread1.start()





'''
possible ways to speed this thing up
1. compare just file names
1. multithread it
2. make it use the gpu
3. run it on nvidia jetson nano, but network latency? connect nano to switch maybe?

49 picutures compare with 7k took approximately 10 hours
'''
if __name__ == '__main__':
    start_time = time.time()
    print("time elapsed: {:.2f}s".format(time.time()))
    main()
    end_time = time.time()

    print("time elapsed: {:.2f}s".format(time.time() - start_time))
