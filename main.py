import cv2

capture = cv2.VideoCapture(0)
face = cv2.CascadeClassifier('default_frontal_face.xml')

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

blur_level = 91
frame_count = 0

while True:
    ret, img = capture.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.2, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_img = img[y:y+h, x:x+w]
        blurred = cv2.GaussianBlur(face_img, (blur_level, blur_level), 0)
        img[y:y+h, x:x+w] = blurred
    
    if len(faces) == 0:
        cv2.putText(img, 'No Face Found!', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    
    cv2.putText(img, f'Blur: {blur_level}', (20, 460), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    frame_count += 1
    cv2.imshow('Face Blur', img)
    
    key = cv2.waitKey(1) & 0xff
    if key == ord('q'):
        break
    elif key == ord('b'):
        blur_level = 51 if blur_level == 91 else 91

capture.release()
cv2.destroyAllWindows()