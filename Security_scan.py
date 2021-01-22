import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import winsound
import time


cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX

with open('record.txt') as f:
    myDataList = f.read().splitlines()
#
# with open('Scan_Record.txt') as f:
#     ScanDataList = f.read().splitlines()

named_tuple = time.localtime()  # get struct_time
time_string = time.strftime(" %m/%d/%Y, %H:%M:%S ", named_tuple)
print(time_string)
while True:
   # time.sleep(1)
   _, frame = cap.read()
   decodeObj=pyzbar.decode(frame)
   for obj in decodeObj:
      print(" ",obj.data)
      myData=obj.data.decode('utf-8')

      if myData in myDataList:
          pts =np.array([obj.polygon],np.int32)
          pts =pts.reshape((-1,1,2))
          cv2.polylines(frame,[pts],True,(255,0,255),3)
          pts2 =obj.rect
          cv2.putText(frame,str('Entry'),(pts2[0],pts2[1]),font,0.9,
                   (255,0,0),2)
          cv2.putText(frame, str('Welcome Our world'), (150, 350), font, 0.9,
                      (255, 0, 0), 2)
      else:
          pts = np.array([obj.polygon], np.int32)
          pts = pts.reshape((-1, 1, 2))
          cv2.polylines(frame, [pts], True, (255, 0, 255), 3)
          pts2 = obj.rect
          cv2.putText(frame, str('No entry'),(pts2[0],pts2[1]), font, 0.6,
                      (0, 0, 255), 2)

          cv2.putText(frame, str('Sorry,Unknown Person'), (50, 350), font, 0.9,
                      (0, 0, 255), 2)
          winsound.Beep(500, 350)


   cv2.imshow("security scanner",frame)
   key = cv2.waitKey(1)
   if key == 27:
       break
