import cv2, os
import numpy as np
from PIL import Image
import RPi.GPIO as GPIO
import time
from PIL import ImageFile
import face_trainer
GPIO.setwarnings(False)
ImageFile.LOAD_TRUNCATED_IMAGES = True
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.output(4, False)
GPIO.output(17, False)
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("training-results")

print "training completed"
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            break

    os.system('raspistill -w 320 -h 234 -o output.jpg')

    authorized_user_number = 16

    image_path = "output.jpg"
    predict_image_pil = Image.open(image_path).convert('L')
    predict_image = np.array(predict_image_pil, 'uint8')
    faces = faceCascade.detectMultiScale(predict_image)
    for (x, y, w, h) in faces:
            nbr_predicted = recognizer.predict(predict_image[y: y + h, x: x + w])
            verified = nbr_predicted == authorized_user_number
    drunk = False
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    Drunkdata = GPIO.input(21)
    if Drunkdata == 1:
        drunk = True

    if verified and not drunk:
        print "Car Unlocked"
        GPIO.output(4, True)
        GPIO.output(17, False)
    else:
        print "Car Locked"
        GPIO.output(4, False)
        GPIO.output(17, True)
        print drunk
