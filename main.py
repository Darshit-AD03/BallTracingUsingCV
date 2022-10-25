from collections import deque


from imutils.video import VideoStream
import numpy as np
import cv2
import argparse
import time
import imutils
import calc


ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", default='aaaa.mp4', help="Path to the (optional) video file")
ap.add_argument("-b", "--buffer", default=64, type=int, help="max buffer size")
args = vars(ap.parse_args())

greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = deque(maxlen=args["buffer"])

if not args.get("video", False):
    vs = VideoStream(src=0).start()
else:
    vs = cv2.VideoCapture(args["video"])

time.sleep(2.0)


counterF = 0

coords = []

time1 = None

InputFrame = input("Enter Frame at which projectile starts")
while True:
    counterF += 1
    frame = vs.read()
    frame = frame[1] if args.get("video", False) else frame
    if frame is None:
        break

    fps = vs.get(cv2.CAP_PROP_FPS)  # OpenCV2 version 2 used "CV_CAP_PROP_FPS"


    # print(counterF)








    frame = imutils.resize(frame, width=600)
    # resize = cv2.resize(frame, (1000, 1000))

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M['m10']/M['m00']), int(M['m01']/M['m00']))

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            coords.append((int(x), int(y), int(radius) * 2, counterF))

            # print((int(x), int(y), (int(radius)**2)))
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    pts.append(center)

    for i in range(1, len(pts)):
        if pts[i-1] is None or pts[i] is None:
            continue

        thickness = int(np.sqrt(args["buffer"] / float(i+1)) * 2.5)
        cv2.line(frame, pts[i-1], pts[i], (0, 0, 255), thickness)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

if not args.get("video", False):
    vs.stop()
else:
    vs.release()

cv2.destroyAllWindows()



for x, y, z, f in coords:

    point1 = coords[0]

    if (x, y == calc.mirror(point1[0], point1[1])):
        z2 = z
        # print(point1[2]-z2)
        if abs(point1[2]-z2) <= 50:#in same plane
            pxDist = abs(x-point1[0])
            print(pxDist)
            actualDist = (pxDist * calc.ballDiameter) / point1[2]  # Use this distance for calculation of projectile
            frame2 = f
        else:#in different plane
            actualDist = calc.distanceBetweenEndPonits(point1[0], point1[1], point1[2], z)    # Use this distance for calculation of projectile
            frame2 = f


TimeOfProjectile = (frame2 - int(InputFrame))/fps

print(TimeOfProjectile, actualDist)
print(point1)