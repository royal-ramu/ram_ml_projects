import cv2
orgimg = cv2.imread(r'C:\Users\dell\Downloads\mouth-marvels-theme\assets\images\cosmetic-removebg-preview.png')
img_resize=cv2.resize(orgimg,(600,400))
cv2.line(orgimg,(0,0),(400,350),(255,255,0),2)
cv2.rectangle(orgimg,(100,100),(250,300),(0,255,255),4)
cv2.circle(orgimg,(100,100),40,(0,0,255),4)
font=cv2.FONT_ITALIC
cv2.putText(orgimg,"Its me",(50,50),font,1,(105,0,52))
cv2.imshow("orgimg",orgimg)
cv2.waitKey(0)
cv2.destroyAllWindows()