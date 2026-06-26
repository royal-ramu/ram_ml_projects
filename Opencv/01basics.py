import cv2

img = cv2.imread(r'C:\Users\dell\Downloads\mouth-marvels-theme\assets\images\cosmetic-removebg-preview.png')
cv2.imshow('personal picture', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
