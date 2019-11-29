import cv2
#aloy_annen = cv2.imread("aloy.jpg")
#cv2.imshow("thesth2",aloy_annen[0:400,150:430])
#cv2.imshow("thesth",aloy_annen)
#cv2.imwrite("thesth2.jpg",aloy_annen[0:400,150:430])
#font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(aloy_annen,'Thesth uyer',[350,260]
cap = cv2.VideoCapture(0)
while(True):
    
    ret,frame=cap.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gframe',grey)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()
