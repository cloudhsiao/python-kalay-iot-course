import cv2

#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 30

cap = cv2.VideoCapture(0)

def get_image():
    retval, im = cap.read()
    return im

# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
    temp = get_image() 

snapshot = get_image()
cv2.imwrite("grab.png", snapshot)

del(cap)
