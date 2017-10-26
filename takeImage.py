import numpy as np
import cv2

# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# k = cv2.waitKey(0) & 0xFF
# if k == ord('e'):  # wait for e key to exit
#     cv2.destroyAllWindows()
# elif k == ord('s'):  # wait for 's' key to save and exite
#     cv2.imwrite('messigray.png', frame)
#     cv2.destroqyAllWindows()

import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('feed', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('imageName.png', frame)
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
