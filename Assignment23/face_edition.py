import cv2
import cvzone
import keyboard

face_detector = cv2.CascadeClassifier("face_detect.xml")
eyes_detector = cv2.CascadeClassifier("eye_detect.xml")
lips_detector = cv2.CascadeClassifier("smile_detect.xml")
face_emoji = cv2.imread("emoji.jpg", cv2.IMREAD_UNCHANGED)
eyes_emoji = cv2.imread("eyes-emoji.png", cv2.IMREAD_UNCHANGED)
lips_emoji = cv2.imread("lips_emoji.png", cv2.IMREAD_UNCHANGED)

def Add_face_emoji(input_frame):
    faces = face_detector.detectMultiScale(input_frame, 1.3)
    for (x, y, w, h) in faces:
        resize_emoji = cv2.resize(face_emoji, (w + 35, h + 35))
        input_frame = cvzone.overlayPNG(input_frame, resize_emoji, [x, y])
        return input_frame

def Add_eyes_lips_emoji(input_frame):
    eyes = eyes_detector.detectMultiScale(input_frame, 2, maxSize=(45,45))
    for (x, y, w, h) in eyes:
        resize_emoji = cv2.resize(eyes_emoji, (w, h))
        input_frame = cvzone.overlayPNG(input_frame, resize_emoji, [x, y])  
    smile = lips_detector.detectMultiScale(input_frame, 1.3, 15)
    for (x, y, w, h) in smile:
        resize_emoji = cv2.resize(lips_emoji, (w, h))
        input_frame = cvzone.overlayPNG(input_frame, resize_emoji, [x, y])  
    return input_frame

def Rasterize_face(input_frame):
    faces = face_detector.detectMultiScale(input_frame, 1.3)
    for (x, y, w, h) in faces:            
        blurred = input_frame[y:y+h, x:x+w]
        pixlated = cv2.resize(blurred, (15, 15), interpolation=cv2.INTER_LINEAR)
        checkered_face = cv2.resize(pixlated, (w, h), interpolation=cv2.INTER_NEAREST)
        input_frame[y:y+h, x:x+w] = checkered_face
        return input_frame

def Angle_img(input_frame):
    faces = face_detector.detectMultiScale(input_frame, 1.3)
    for (x, y, w, h) in faces:
        input_frame[y : y + h, x : x + w] = cv2.rotate(input_frame[y : y + h, x : x + w], cv2.ROTATE_180)
    return input_frame

video_cap = cv2.VideoCapture(0)

while True:  
    ret, frame = video_cap.read()
    if ret == False:
        break
    k = cv2.waitKey(1)
    if keyboard.is_pressed('1'):
        frame = Add_face_emoji(frame)

    if keyboard.is_pressed('2'):
        frame = Add_eyes_lips_emoji(frame)
            
    if keyboard.is_pressed('3'):
        frame = Rasterize_face(frame)

    if keyboard.is_pressed('4'):
        frame = Angle_img(frame)

    if keyboard.is_pressed('q'):
        exit()

    cv2.imshow("OUTPUT",frame)