import cv2
orgimg=cv2.imread(r"C:\Users\dell\Downloads\mouth-marvels-theme\assets\images\cosmetic-removebg-preview.png")
cp_img=orgimg.copy()
cv2.circle(cp_img,(100,100),75,(255,0,0),-2)
cv2.imshow("orgimg",orgimg)
cv2.imshow("cp_img",cp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()