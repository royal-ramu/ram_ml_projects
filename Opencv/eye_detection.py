import cv2
org_img=cv2.imread(r"D:\Saravanan Phone backup\Family pics\FB_IMG_15829499003595551.jpg")
resized_img=cv2.resize(org_img,(700,700))
gry_img=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
eye_detector=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
