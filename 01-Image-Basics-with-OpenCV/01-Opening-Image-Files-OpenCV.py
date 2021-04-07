import cv2

img = cv2.imread('../DATA/00-puppy.jpg')

while True:
    
    # cv2.imshow('Name of the image window', image variable)

    cv2.imshow('Puppy',img)

    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    
    # IF we've waited at least 1 ms (cv2.waitKey(1)) AND we've pressed the Esc key (0xFF == 27), the image will be closed.
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
