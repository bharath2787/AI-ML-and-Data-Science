import cv2  # OpenCV for handling video capture and display
import mediapipe as mp  # MediaPipe for hand tracking

# -------------------- Initialize MediaPipe Hands Module --------------------
mp_hands = mp.solutions.hands  # Access MediaPipe Hands module
hands = mp_hands.Hands()  # Create a Hands object to detect and track hands
mp_draw = mp.solutions.drawing_utils  # For drawing landmarks on the hands

# -------------------- Initialize Webcam --------------------
cap = cv2.VideoCapture(0)  # Open the webcam (camera index 0)

# -------------------- Main Loop --------------------
while True:
    success, img = cap.read()  # Read a frame from the webcam
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB (MediaPipe uses RGB format)

    # -------------------- Process Hand Landmarks --------------------
    results = hands.process(img_rgb)  # Detect hands and landmarks in the image

    # -------------------- If Hands are Detected --------------------
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:  # Loop through all detected hands
            # Draw landmarks and connections on the hands
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            #https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker
    # -------------------- Display Webcam Feed with Hand Landmarks --------------------
    cv2.imshow("MediaPipe Hand Tracking", img)  # Display the frame with landmarks

    # -------------------- Exit Loop --------------------
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit the loop
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
