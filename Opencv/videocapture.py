import cv2
fullbody_lib=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
video_path=cv2.VideoCapture(r"C:\Users\dell\Downloads\istockphoto-1209130964-640_adpp_is.mp4")
while True:
    ret,frame=video_path.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    walking_ppl=fullbody_lib.detectMultiScale(gray,1.1,3)
    count = len(walking_ppl)
    for (x,y,w,h) in walking_ppl:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.putText(frame, f'People Count: {count}',
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 2)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_path.release()
cv2.destroyAllWindows()