# approach -> comapre initial frame with the next frame
import cv2
import imutils

cap=cv2.VideoCapture(0)
frist_frame=None
area=500

while True:
    _,frame=cap.read()
    # background code
    text="Normal"
    resize=imutils.resize(frame,width=500)
    gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
    gaussian_blur=cv2.GaussianBlur(gray,(21,21),0)
    # background end here
    
    # compare code 
    if frist_frame is None:
        frist_frame=gaussian_blur
        continue
    comapre=cv2.absdiff(frist_frame,gray)
    threshold=cv2.threshold(comapre,25,255,cv2.THRESH_BINARY)[1]
    threshold=cv2.dilate(threshold,None,iterations=2)
    contours=cv2.findContours(threshold.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours=imutils.grab_contours(contours)
    # compare code ends

    # tracking code

    for i in contours:
        if cv2.contourArea(i) < area:
            continue
        (x,y,w,h)=cv2.boundingRect(i)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        text="object detected"
    print(text)
    cv2.putText(frame,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    
    # tracking complete
    
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if key ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()