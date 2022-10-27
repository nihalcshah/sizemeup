import cv2
import os


def facialDetection(imgPath):
    dirname = os.path.dirname(__file__)
    print(dirname)
    print(os.getcwd())
    k = '.'+imgPath
    # k = os.path.join(dirname, imgPath[1:])
    print(k)
    print(os.path.exists(k))

    img = cv2.imread(k)
    # cv2.imshow("dsf",img)
    # cv2.waitKey(0)
    # img = cv2.flip(img, 1)
    basename = os.path.basename(imgPath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(os.path.exists('./sizing/haarcascade_frontalface_default.xml'))
    face_cascade = cv2.CascadeClassifier('./sizing/haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    imgPath = k.replace(basename, basename+"_detected")
    cv2.imwrite(imgPath, img)
    return imgPath, len(faces)