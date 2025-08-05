import cv2
import mediapipe as mp
import pyautogui
import math

my_hands = mp.solutions.hands.Hands()    #To Detect Hands
drawing_utils = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)
x1 = x2 = y1 = y2 = 0

while True:
    success , frame = webcam.read()
    frame_height,frame_width , _= frame.shape      #Returns height , width and chnnels
    
    frame = cv2.flip(frame,1)    #Flip the webcam 
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)    #RGB Convert 
    output = my_hands.process(rgb_frame)    
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame , hand)
            landmarks = hand.landmark

            for id , landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                if id==8:
                    cv2.circle(frame , (x,y) , 8 , (0,255,0))
                    x1 = x
                    y1 = y
                if id==4:
                    cv2.circle(frame , (x,y) , 8 , (255,0,0))    
                    x2 = x
                    y2 = y
            dist = dist = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)) // 4
            if dist>45:
                pyautogui.press("Volumeup")   
                # print("Increasing Volume")
            elif dist<30:
                pyautogui.press("Volumedown")   
                # print("Decreasing Volume")  
            cv2.line(frame , (x1,y1) , (x2,y2) , (0,0,255) , 4)
    cv2.imshow("Gesture Volume Cantrol" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting") 
        break

webcam.release()
cv2.destroyAllWindows()
