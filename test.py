import cv2

res = []
def drawBox(jj, cont): # ,cont2):
    # x, y, w, h = cv2.boundingRect(cnt)
    # if h>30 and w>30:
    # approx = cv2.approxPolyDP(cnt, 0.009 * cv2.arcLength(cnt, True), True)
    #
    # # draws boundary of contours.
    # cv2.drawContours(jj, [approx], 0, (0, 0, 255), 5)
    #
    # # flatted the array containing
    # # the co-ordinates of the vertices.
    # n = approx.ravel()
    # i = 0
    #
    # for j in n :
    #     if(i % 2 == 0):
    #         x = n[i]
    #         y = n[i + 1]
    #
    #         # String containing the co-ordinates.
    #         string = str(x) + " " + str(y)
    #
    #         if(i == 0):
    #             # text on topmost co-ordinate.
    #             cv2.putText(jj, "Arrow tip", (x, y),
    #                         cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0))
    #         else:
    #             # text on remaining co-ordinates.
    #             cv2.putText(jj, string, (x, y),
    #                         cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    #     i = i + 1
    for cnt in cont:
        x, y, w, h = cv2.boundingRect(cnt)
        if h>30 and w>30:
            cv2.rectangle(jj, (x, y), ((x + w), (y + h)), (0, 0, 255), 3, 1)
            cv2.circle(jj,(int(x+(w/2)),int(y+(h/2))),3,(255,0,0),2)
            cv2.putText(jj, "X =", (x, y),1, 1, (0, 255, 0))
            cv2.putText(jj, str(int(x)), (x+30, y),1, 1, (0, 255, 0))
            cv2.putText(jj, "Y =", (x+90,y),1, 1, (0, 255, 0))
            cv2.putText(jj, str(int(y)), (x+120, y),1, 1, (0, 255, 0))

        # for cnt2 in cont2:
        #     z, y2, w2, h2 = cv2.boundingRect(cnt)
        #     if h2>30 and w2>30 and y==y2:
        #            res.append((x,y,z))


cap = cv2.VideoCapture(1)
# cap2 = cv2.VideoCapture(2)

while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    graybelt = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(graybelt, (3, 3), 0)

    # success, img2 = cap2.read()
    # graybelt2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    # blurred2 = cv2.GaussianBlur(graybelt2, (3, 3), 0)

    ##Dtecting white on a black surface
    # success,threshold = cv2.threshold(graybelt, 50,255,cv2.THRESH_BINARY)

    ##Dtecting black on a white surface
    # success,threshold = cv2.threshold(graybelt,100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    success,threshold = cv2.threshold(blurred,100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    # success,threshold2 = cv2.threshold(blurred2,100, 255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    # edged = cv2.Canny(thresholdblur, 10, 100)

    contours,_ = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # contours2,_ = cv2.findContours(threshold2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    drawBox(img, contours) # ,contours2)

    fps = cv2.getTickFrequency() // (cv2.getTickCount() - timer)
    cv2.putText(img, str(fps), (50, 80), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 1)

    cv2.imshow("Tracking", img)
    cv2.imshow("belt", graybelt)
    cv2.imshow("blurred", blurred)
    cv2.imshow("threshold", threshold)
    # cv2.imshow("thresholdblur", thresholdblur)
    # cv2.imshow("Edged image", edged)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
