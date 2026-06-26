import cv2
teethimg=cv2.imread(r"C:\Users\dell\Downloads\mouth-marvels-theme\assets\images\cosmetic-removebg-preview.png")
img_resize = cv2.resize(teethimg,(300,400))
file_path=r"C:\Users\dell\Pictures\Saved Pictures\newpic.jpg"
cv2.imwrite(file_path,img_resize)
imgreplace=cv2.imwrite(file_path,img_resize)
cv2.imshow('imgreplace',imgreplace)
cv2.waitKey(0)
cv2.destroyAllWindows()