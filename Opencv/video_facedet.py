import cv2

# Load cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                     'haarcascade_frontalface_default.xml')

smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                      'haarcascade_smile.xml')

eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                    'haarcascade_eye.xml')

# Start webcam
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces_rect = face_cascade.detectMultiScale(
        gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # ROI (face area)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # 👁️ Detect eyes inside face
        eyes = eye_cascade.detectMultiScale(
            roi_gray, scaleFactor=1.1, minNeighbors=10)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 0, 255), 2)

        # 😊 Detect smiles inside face
        smiles = smile_cascade.detectMultiScale(
            roi_gray, scaleFactor=1.7, minNeighbors=20, minSize=(25, 25))

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy),
                          (sx + sw, sy + sh), (0, 255, 0), 2)

    # Show output
    cv2.imshow('Face Eye Smile Detection', frame)

    # ❌ Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()