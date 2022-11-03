import datetime

from PIL import ImageGrab as ig
import numpy as np
import cv2
from win32api import GetSystemMetrics as gsm

width = gsm(0)
height = gsm(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d  %H-%M-%S')


file_name = f'{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_vdo = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

webcam = cv2.VideoCapture(0)


while True:
    img = ig.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    fr_ht, fr_wd, _ = frame.shape
    print(fr_ht, fr_wd)
    img_final[0: fr_ht, 0:fr_wd, :] = frame[0: fr_ht, 0:fr_wd, :]

    # cv2.imshow('Secret Capture', img_np)
    cv2.imshow('Secret Capture', img_final)

    # qcv2.imshow('webcam', frame)

    captured_vdo.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break

'''
did it yaaaa
'''

