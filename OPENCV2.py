import cv2

image = cv2.imread("3x3 logo.png")
print("Error: Image not found. Check the file path.")

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

resizedimg=cv2.resize(gray_image,(224,224))

cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Loaded Image", 800, 500)
cv2.imshow("Loaded Image", image)
key=cv2.waitKey(0)
if key==ord('s'):
    cv2.imwrite("3x3 logo resized.png".resizedimg)
    print("3x3 logo resized has been saved")

cv2.destroyAllWindows()