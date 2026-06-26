import cv2
smile_det=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
v_frame=cv2.VideoCapture(0)
while True:
    ret,frame=v_frame.read()
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    smile_rect=smile_det.detectMultiScale(gray_img,1.5,30)
    if len(smile_rect) > 0:
        text = "Smiling "
        color = (0, 255, 0)
        cv2.putText(frame, text, (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, color, 2)
        for(x,y,w,h) in smile_rect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
    else:
        text = "Please Smile "
        color = (0, 0, 255)
        cv2.putText(frame, text, (20, 40),cv2.FONT_HERSHEY_SIMPLEX,0.8, color, 2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break

# Release resources
v_frame.release()
cv2.destroyAllWindows()