#!/usr/bin/env python3

import argparse
import cv2
from datetime import datetime, timezone, timedelta

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
cap = cv2.VideoCapture()
cap.open(0, apiPreference=cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 30.0)

start = datetime.now(timezone.utc)

while(True):
    # wait a few seconds to stabilize
    ret, frame = cap.read()
    now = datetime.now(timezone.utc)
    if now - start > timedelta(seconds=3):
        break

# Our operations on the frame come here
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Display the resulting frame
cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

cv2.imwrite("base.png", frame)

base_blur = cv2.medianBlur(frame, 21)
cv2.imwrite("base_blur.png", base_blur)
