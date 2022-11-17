import cv2 as cv
import numpy as np

img = cv.imread('11.jpg')


res = cv.resize(img, (780, 540), interpolation = cv.INTER_NEAREST)

b, g, r = cv.split(res)

canny = cv.Canny(g, 125, 175)
cv.imshow('aaa', canny)


circles = cv.HoughCircles(canny,cv.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=100, maxRadius=400)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(g,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(g,(i[0],i[1]),2,(0,0,255),3)
cv.imshow('detected circles', g)
# con, hie = cv.findContours(canny, cv.RETR.LIST, cv.CHAIN_APPROX_NONE)


cv.waitKey(0)