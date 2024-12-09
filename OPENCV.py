import cv2

image = cv2.imread("3x3 logo.png")

if image is None:

    print("Error: Image not found. Check the file path.")

else:
    cv2.namedWindow("Loaded Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Loaded Image", 800, 500)
    cv2.imshow("Loaded Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()