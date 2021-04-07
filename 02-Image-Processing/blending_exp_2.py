import cv2
import matplotlib.pyplot as plt
 
img1 = cv2.imread('DATA/dog_backpack.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread('DATA/watermark_no_copy.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2 = cv2.resize(img2,(600,600))
 
x_offset = img1.shape[1]-img2.shape[1]
y_offset = img1.shape[0]-img2.shape[0]
 
# GRAP REGION OF INTEREST (ROI)
roi = img1[y_offset:,x_offset:]
 
# BLENDING WITH MASK
mask = img2 != 255
mask = mask.astype(np.uint8)

# Now we have mask matrix and can use it to clear background of our small image:
img2_cleared = img2*mask
plt.imshow(img2_cleared)

# Now we could complete the task to blend our region of interest with cleared small image:
roi_blended = cv2.bitwise_or(roi,img2_cleared)
plt.imshow(roi_blended)