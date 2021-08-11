from PIL import ImageGrab
import numpy as np
import cv2

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter('output.mp4', fourcc, 2.5, (2560, 1600))

while True:
    img = ImageGrab.grab(bbox=(0, 0, 2560, 1600))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow("Secret Recorder", img_final)
    capture_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
