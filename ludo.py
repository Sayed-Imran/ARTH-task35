import cv2
import numpy as np

img = np.zeros((525,525,3), np.uint8)

cv2.rectangle(img, (0,0), (525,525), (255,255,255), cv2.FILLED)


cv2.rectangle(img, (0,0), (210,210), (0,0,255), cv2.FILLED)
cv2.rectangle(img, (525, 0), (315, 210), (255,0,0), cv2.FILLED)
cv2.rectangle(img, (0,525),(210, 315), (0,255,0), cv2.FILLED)
cv2.rectangle(img, (525,525),(315, 315), (0,255,255), cv2.FILLED)
cv2.rectangle(img, (210,210),(315,315),(255,255,0),cv2.FILLED)

cv2.rectangle(img, (245,35),(280,210),(240,0,0), cv2.FILLED )
cv2.rectangle(img, (35,245), (210, 280), (0,0,240), cv2.FILLED)
cv2.rectangle(img, (245,315), (280, 490), (0,240,0), cv2.FILLED)
cv2.rectangle(img, (315,245),(490,280), (0,240,240), cv2.FILLED)

cv2.rectangle(img, (35,210), (70, 245), (0,0,240), cv2.FILLED)
cv2.rectangle(img, (280, 35), (315, 70), (240, 0, 0), cv2.FILLED)
cv2.rectangle(img, (210,455), (245, 490), (0,240,0), cv2.FILLED)
cv2.rectangle(img, (455,280), (490,315), (0,240,240), cv2.FILLED)

cv2.rectangle(img, (35,35), (175,175), (0,0,0), 2)
cv2.rectangle(img, (350,35), (490,175), (0,0,0), 2)
cv2.rectangle(img, (35,350), (175, 490), (0,0,0), 2)
cv2.rectangle(img, (350,350), (490,490), (0,0,0), 2)

cv2.rectangle(img, (38,38), (172,172), (255,255,255), cv2.FILLED)
cv2.rectangle(img, (38,353), (172, 487), (255,255,255), cv2.FILLED)
cv2.rectangle(img, (353,353), (487,487), (255,255,255), cv2.FILLED)
cv2.rectangle(img, (353,38), (487,172), (255,255,255), cv2.FILLED)

 
#RED MARKS IN THE BOX
for a in [75, 135]:
    for b in [75, 135]:
        cv2.circle(img, (a,b), 20, (0,0,255), cv2.FILLED)
        cv2.circle(img, (a,b), 20, (0,0,0), 2)


#BLUE MARKS IN THE BOX
for a in [390, 450]:
    for b in [75,135]:
        cv2.circle(img, (a, b), 20, (255,0,0), cv2.FILLED)
        cv2.circle(img, (a, b), 20, (0,0,0), 2)


#GREEN MARKS IN THE BOX
for a in [75, 135]:
    for b in [390, 450]:
        cv2.circle(img, (a, b), 20, (0,255,0), cv2.FILLED)
        cv2.circle(img, (a, b), 20, (0,0,0), 2)
        

#YELLOW MARKS IN THE BOX
for a in [390, 450]:
    for b in [390, 450]:
        cv2.circle(img, (a,b), 20, (0, 255,255), cv2.FILLED)
        cv2.circle(img, (a,b), 20, (0, 0,0), 2)

i = 0
j = 35

for a in [210, 245, 280]:
    for b in [245, 280, 315]:
        while(i <= 512):
            cv2.rectangle(img, (a,i), (b,j), (0,0,0), 2)
            cv2.rectangle(img, (i,a), (j,b), (0,0,0), 2)
            i += 35
            j += 35
        i = 0
        j = 35
cv2.rectangle(img, (1,1), (524,524), (0,0,0), 2)

cv2.rectangle(img, (210,210),(315,315),(255,255,0),cv2.FILLED)
cv2.putText(img, "HOME", (215,275), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0),2)

while True:
    cv2.imshow("LUDO", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break