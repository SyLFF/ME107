import numpy as np
import cv2
# Import image
frame = cv2.imread("turn2.png")
cv2.imshow('Original Frame', frame)
width = frame.shape[0]
height = frame.shape[1]
size = frame.size
# print width
# print height
# print frame.size
# print frame.dtype
allWhite = np.ones((width,height,3), np.uint8) * 255
# cv2.imshow('White Image', allWhite)

# Turn image into gray scale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale', gray)

# Edge detection
edges = cv2.Canny(gray, threshold1=100, threshold2=400)
# cv2.imshow('Edges detection', edges)

#  Probabilisitic HoughLine
lines = cv2.HoughLinesP(edges, rho=1, theta=1*np.pi/360, threshold=10, minLineLength=100, maxLineGap=50)
print(lines)
print(lines[0, :, 0].shape)
# cv2.imshow('Original frame', gray)
#
for x1, y1, x2, y2 in lines[0]:
    cv2.line(allWhite, (x1, y1), (x2, y2), (0, 0, 0), 2)

cv2.imshow('HoughLines', allWhite)
cv2.waitKey(0)

# eliminate duplicate lines from the output of HoughLines
# def lineHelper(lines):
#     for x1, y1, x2, y2 in lines[0]:
#
#         return lines