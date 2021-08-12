import cv2
import glob
import cvlib as cv
import numpy as np
import random
from time import sleep
from cvlib.object_detection import draw_bbox

font = cv2.FONT_HERSHEY_PLAIN

counter = 0
def count(a):
    global counter
    counter +=a
    print ("Total cars:-"+str(counter))
    


def object(i):   
    bbox, label, conf = cv.detect_common_objects(i)
    print (label)
    print('Number of cars in the image is '+ str(label.count('car')))
    b=label.count('car')
    output_image = draw_bbox(i, bbox, label, conf)
    cv2.putText(i,"car:"+str(label.count('car')),(20,50),0,2,(0,0,255),2)
    count (b)
   

path = "/home/pi/Downloads/images/*.*"
for file in glob.glob(path):
    image_read = cv2.imread(file)
    c=cv2.resize(image_read, (640, 480))
    object(c)
    cv2.imshow("FRAME",c)
    cv2.waitKey(500)
    sleep(0.01)
    random.shuffle(c)
    cv2.destroyAllWindows