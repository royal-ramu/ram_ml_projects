import cv2
orgimg = cv2.imread(r'C:\Users\dell\Downloads\mouth-marvels-theme\assets\images\cosmetic-removebg-preview.png')
h,w = orgimg.shape[:2]
print("Original image height={},Original image width={}".format(h,w))
resi_img=cv2.resize(orgimg,(400,400))
resiz_h,resiz_w=resi_img.shape[:2]
print("Original image height={},Original image width={}".format(resiz_h,resiz_w))
cv2.imshow('original',orgimg)
cv2.imshow('resized',resi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
