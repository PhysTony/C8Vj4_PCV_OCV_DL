import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),thickness=4)        

img = cv2.imread('..\DATA\dog_backpack.jpg')
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_circle)

while True: # Runs forever until we break with Esc key on keyboard
    cv2.imshow('my_drawing',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()