#importing modules

import cv2
import numpy as np


#capturing video through webcam
cap=cv2.VideoCapture(0)
def trackingFunction(color,bgrValue, colorString,img):
    #tracking function
    (contours,hierarchy)=cv2.findContours(color,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic,contour in enumerate(contours):

        area = cv2.contourArea(contour)
        if (area>1000):#300

            x,y,w,h= cv2.boundingRect(contour)
            img=cv2.rectangle(img,(x,y),(x+w,y+h),bgrValue,2)
            cv2.putText(img,colorString,(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, bgrValue)
            #compute the bounding box
            #return cv2.minAreaRect(contour)
            return w

def distance_to_camera(knownWidth,focalLength,perWidth):
    #compute and return the distance from the marker to the camera
        
    return (knownWidth*focalLength)/perWidth


#text file 
'''distanceName = "C:\\Users\\Diana Wanjiru\\Desktop\\ROBOKEN\\distance\\conversionRatio\\measured\\distancetestfar.txt"
distanceFile=open(distanceName,"w+")

widthFileName="C:\\Users\\Diana Wanjiru\\Desktop\\ROBOKEN\\distance\\conversionRatio\\measured\\widthtestfar.txt"
widthFile=open(widthFileName,"w+")'''

'''meanWidthName="C:\\Users\\Diana Wanjiru\\Desktop\\ROBOKEN\\distance\\conversionRatio\\means\\widthsmeantest.txt"
meanWidthFile=open(meanWidthName,"w+")'''

'''meanDistanceName="C:\\Users\\Diana Wanjiru\\Desktop\\ROBOKEN\\distance\\conversionRatio\\means\\distancemeantest.txt"
meanDistanceFile=open(meanDistanceName,"w+")'''




while(1):
    _, img = cap.read()

    #converting frame (img i.e BGR) to HSV(hue-saturation-value)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                
    #defining the range color,arguments (bgr value, data type)
    red_lower=np.array([0,131,84],np.uint8)
    red_upper=np.array([6,255,255],np.uint8)
    blue_lower=np.array([99,115,150],np.uint8)
    blue_upper=np.array([110,255,255],np.uint8)
    yellow_lower=np.array([22,60,200],np.uint8)
    yellow_upper=np.array([60,255,255],np.uint8)
    green_lower=np.array([65,60,60],np.uint8)
    green_upper=np.array([80,255,255],np.uint8)
    

    

    #colorDetection
    red=cv2.inRange(hsv, red_lower, red_upper)
    blue=cv2.inRange(hsv, blue_lower, blue_upper)
    yellow=cv2.inRange(hsv, yellow_lower, yellow_upper)
    green=cv2.inRange(hsv, green_lower, green_upper)
    

    #Morphological transformation ,dilation
    kernal = np.ones((5,5), "uint8")
    
    red=cv2.dilate(red,kernal)
    res=cv2.bitwise_and(img, img, mask = red)
    blue=cv2.dilate(blue,kernal)
    res1=cv2.bitwise_and(img, img, mask=blue)
    yellow=cv2.dilate(yellow,kernal)
    res2=cv2.bitwise_and(img, img, mask=yellow)
    green=cv2.dilate(green,kernal)
    res3=cv2.bitwise_and(img, img, mask=green)

    
    

    

    
    
    
    
   
    knownWidth=6 #reading in cm
    focalLength=607.6983 #in pixels
    #tracking colors
    redAppaWidth=trackingFunction(red,(0,0,255),"Red color",img)
    #redWidthStorage=str(redAppaWidth)+","
    #widthFile.write(redWidthStorage)
    
    blueAppaWidth=trackingFunction(blue,(255,0,0),"Blue color",img)
    yellowAppaWidth=trackingFunction(yellow,(0,255,255),"Yellow color",img)
    greenAppaWidth=trackingFunction(green,(0,255,0),"Green color",img)
    #correctionFactor=1.5
    
    
    if redAppaWidth:
        redDistance=distance_to_camera(knownWidth,focalLength,redAppaWidth)
        #redDistance=redDistance/correctionFactor
        actualDistance=(1.1326*redDistance) - 1.7127
        conversionRatio=608.49/redDistance
        actualWidth=redAppaWidth/conversionRatio
        #print ("Red Distance",redDistance)
        print ("actualDistance: ",actualDistance)
        print ("actualWidth: ", actualWidth)
        #distanceStorage=str(redDistance)+","
        #distanceFile.write(distanceStorage)
        
    else:
        print("out of range")
    

    '''if greenAppaWidth:
        greenDistance=distance_to_camera(knownWidth,focalLength,greenAppaWidth)
        print ("Green Distance",greenDistance)
    else:
        print("out of range")

    if yellowAppaWidth:
        yellowDistance=distance_to_camera(knownWidth,focalLength,yellowAppaWidth)
        print ("Yellow Distance",yellowDistance)
    else:
        print("out of range")

    if blueAppaWidth:
        blueDistance=distance_to_camera(knownWidth,focalLength,blueAppaWidth)
        print ("blue Distance",blueDistance)
    else:
        #print("out of range")'''
    
    #showing window
    
    #cv2.putText(img,"%.2fcm"%redDistance, cv2.FONT_HERSHEY_SIMPLEX,2.0,(0,0,255),3)
    cv2.imshow("Color Tracking",img)
    if cv2.waitKey(10) & 0xFF== ord('q'):
        from distanceCorrection import correction
        cap.release()
        #closing measurement files
        #distanceFile.close()
        #widthFile.close()

        
        #distanceMean=correction(distanceName)
        #print("Mean Distance"+str(distanceMean))
        
        '''meanDistanceStorage=str(distanceMean)+','
        meanDistanceFile.write(meanDistanceStorage)
        meanDistanceFile.close()
        
        widthMean=correction(widthFileName)
        print("Mean width"+str(widthMean))
        meanWidthStorage=str(widthMean)+','
        meanWidthFile.write(meanWidthStorage)
        meanWidthFile.close()'''
        cv2.destroyAllWindows()
        break
    
            
    

    
    
        
