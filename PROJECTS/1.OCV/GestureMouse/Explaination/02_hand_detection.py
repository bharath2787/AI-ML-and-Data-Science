import cv2  # OpenCV library for computer vision tasks
import gesture_detection as ht  # Custom module for hand detection and tracking

# -------------------- Initialize Webcam --------------------
cap = cv2.VideoCapture(0)  # Start capturing video from the default webcam (camera index 0)
cap.set(3, 640)  # Set the width of the video frame to 640 pixels
cap.set(4, 480)  # Set the height of the video frame to 480 pixels

# -------------------- Create Hand Detector --------------------
detector = ht.handDetector()  # Create an instance of the hand detector from the custom module

# -------------------- Main Loop --------------------
while True:
    success, img = cap.read()  # Read a frame from the webcam
    img = detector.findHands(img)  # Detect hands and draw landmarks on the image
    lmlist, bbox = detector.findPosition(img)  # Get list of landmark positions and bounding box if a hand is found

    # -------------------- Display the Frame --------------------
    cv2.imshow("Hand Detection", img)  # Show the frame with hand detection in a window titled "Hand Detection"

    # Exit the loop and close the window when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
