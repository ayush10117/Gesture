import os
import cv2
from cvzone.HandTrackingModule import HandDetector
import boto3


cam = cv2.VideoCapture(0)
status, photo = cam.read()
cv2.imshow("my photo", photo)
cv2.waitKey()
cv2.destroyAllWindows()
detector = HandDetector()
myhand = detector.FindHands(photo)
mylmlist = myhand[0][0]
myfinger = detector.fingersup(mylmlist)

ec2 = boto3.resource(
    "ec2",
    aws_access_key_id = "Add Your Own",
    aws_secret_access_key = "Add Your Own",
    region_name= "add")

def osLaunch():
    ec2.create_instances(
    InstanceType ="t2.micro",
    ImageId ="ami-0e670eb768a5fc3d4",
    MinCount=1,
    MaxCount=1,
)

if myfinger == [1, 1, 1, 1, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [0, 0, 0, 0, 0]:
    print("No finger detected hence number of instances launched = 0.")
elif myfinger == [0, 1, 1, 0, 0]:
    osLaunch()
    osLaunch()
elif myfinger == [0, 0, 1, 1, 0]:
    osLaunch()
    osLaunch()
elif myfinger == [0, 1, 0, 1, 0]:
    osLaunch()
    osLaunch()
elif myfinger == [1, 1, 0, 0, 0]:
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 1, 0, 0]:
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 0, 1, 0]:
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 0, 0, 1]:
    osLaunch()
    osLaunch()
elif myfinger == [0, 1, 0, 0, 1]:
    osLaunch()
    osLaunch()
elif myfinger == [0, 0, 1, 0, 1]:
    osLaunch()
    osLaunch()
elif myfinger == [0, 0, 0, 1, 1]:
    osLaunch()
    osLaunch()
elif myfinger == [1, 1, 1, 0, 0]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 1, 1, 0]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 1, 0, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 0, 1, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [0, 1, 1, 1, 0]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [0, 0, 1, 1, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [0, 1, 1, 0, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [1, 1, 1, 1, 0]:
    osLaunch()
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [1, 1, 1, 0, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
    osLaunch()
elif myfinger == [1, 1, 0, 1, 1]:
    osLaunch()
    osLaunch()  
    osLaunch()
    osLaunch()
elif myfinger == [1, 0, 1, 1, 1]:
    osLaunch()
    osLaunch()
    osLaunch()  
    osLaunch()
elif myfinger == [0, 1, 1, 1, 1]:
    osLaunch()
    osLaunch()
    osLaunch()
    osLaunch()  
    
