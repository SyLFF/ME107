import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # cv2.imshow('Original Frame', frame)

    # Change frames to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Grayscale', gray)

    # Edge detection
    edges = cv2.Canny(gray, 100, 150)
    # cv2.imshow('Edges detection', edges)

    # HoughLine detection
    # Messy look:
    # R_res = 1
    # Theta_res = 1 * np.pi / 180
    # Threshold = 1
    # minLineLength = 1
    # maxLineGap = 100
    # minLineLength = 250
    # maxLineGap = 10
    # lines = cv2.HoughLinesP(edges, R_res, Theta_res, Threshold, minLineLength, maxLineGap)
    lines = cv2.HoughLinesP(edges,rho=1, theta=1*np.pi/360, threshold=1, minLineLength=100, maxLineGap=50)
    for x in range(0, len(lines)):
        for x1, y1, x2, y2 in lines[x]:
            cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow('HoughLines', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
