import cv2
image = cv2.imread("image_name.jpg") #image_name is the name of the image that has to be converted to greyscale.
grey_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #grey_image is the name of the converted image. 
cv2.imshow("image name",image)
cv2.imshow("grey image" , grey_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
