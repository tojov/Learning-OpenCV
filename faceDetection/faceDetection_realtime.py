import cv2


cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while(True):
	ret, frame = cap.read()
	gVid = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gVid, 1.1, 4)
	for(x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
	cv2.imshow('faceDetect', frame)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()

