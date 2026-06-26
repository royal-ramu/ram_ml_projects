import cv2
org_img=cv2.imread(r"D:\Saravanan Phone backup\Family pics\FB_IMG_15829499003595551.jpg")
resized_img=cv2.resize(org_img,(700,700))
gray_img=cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +r"haarcascade_smile.xml")
face_detec=face_cascade.detectMultiScale(gray_img,1.1,126)
for (x,y,w,h) in face_detec:
    cv2.rectangle(resized_img,(x,y),(x+w,y+h),(0,255,0),2)
    center=(int(x+w/2),int(y+h/2))
    cv2.circle(resized_img,center,30,(0,0,255),2)
cv2.imshow('Detected image',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
