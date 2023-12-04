import cv2 #import openCV for camera use
from deepface import DeepFace #import deepface for face verification

def take_picture(): #function created called take_picture
    print("Scanning face...")
    cap = cv2.VideoCapture(0) #0 is the main camera on my laptop
    while True:
        ret, frame = cap.read() #returns true if the frame is available, creating an infinite loop to be broken out of
        cv2.imwrite('img1.jpg', frame) #image write
        videoShow = cv2.putText(frame, "Press q to stop scanning", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3) #Add text to frame which will be shown
        cv2.imshow("Scanning Face", videoShow) #Display the webcam with text
        key = cv2.waitKey(1)
        if key == ord("q"):
            break #breaks the infinite loop created by the ret, frame
    cv2.destroyAllWindows() #if statement used to close camera when user presses "q"
    cap.release()
    print("Face scan complete")


take_picture() #The function take_picture is called
img1 = "img1.jpg"
img2 = "Actual.jpg"

model_name = "Facenet"

authentication = DeepFace.verify(img1_path=img1, img2_path=img2, model_name=model_name) #compares img1 & img2 in order to compare them

if authentication['verified']: #if both images match then display image taken with text
    image = cv2.imread(img1)
    imageDisplay = cv2.putText(image, "MATCH! ACCESS GRANTED!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.imshow("FaceID", imageDisplay)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #Displays the image taken of the user with text over it saying that Access has been granted
else:
    image = cv2.imread(img1) #if both images do not match or a face is not detected using "else" then display image taken with text
    imageDisplay = cv2.putText(image, "NO MATCH! ACCESS DENIED!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    cv2.imshow("FaceID", imageDisplay)
    cv2.waitKey(0)
    cv2.destroyAllWindows() #Displays the image taken of the user with text over it saying that Access has not been granted


