import cv2
img = cv2.imread("1.JPG", cv2.IMREAD_UNCHANGED)

#resize  image width & hight
width = 800
height = 440

dim = (width, height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#print('Resized Dimensions : ',resized.shape)

cv2.imwrite("resized.jpeg",resized)    #change location if you want to save image
print("resized image saved in your source code folder")
#cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()