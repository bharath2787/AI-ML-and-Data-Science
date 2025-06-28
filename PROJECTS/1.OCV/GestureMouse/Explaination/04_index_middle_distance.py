import cv2  # OpenCV library for computer vision tasks
import gesture_detection as ht  # Custom hand tracking module built using MediaPipe

# -------------------- Initialize Camera --------------------
cap = cv2.VideoCapture(0)  # Start video capture from the default webcam (device index 0)
cap.set(3, 640)  # Set the width of the video frame to 640 pixels
cap.set(4, 480)  # Set the height of the video frame to 480 pixels

# -------------------- Initialize Hand Detector --------------------
detector = ht.handDetector()  # Create an instance of the hand detector

# -------------------- Main Loop --------------------
while True:
    success, img = cap.read()  # Read a frame from the webcam
    img = detector.findHands(img)  # Detect hand(s) in the frame and draw landmarks
    lmlist, bbox = detector.findPosition(img)  # Get a list of landmark positions and bounding box

    if len(lmlist) != 0:  # Check if any hand is detected
        fingers = detector.fingersUp()  # Get a list showing which fingers are up (1 for up, 0 for down)

        # If both index finger (fingers[1]) and middle finger (fingers[2]) are up
        if fingers[1] == 1 and fingers[2] == 1:
            # Calculate the distance between the tips of the index (landmark 8) and middle (landmark 12) fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # Display the calculated distance on the image
            cv2.putText(img, f"Distance: {int(length)}px", (50, 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # -------------------- Show Output --------------------
    cv2.imshow("Distance Between Index and Middle", img)  # Display the frame in a window

    # Break the loop and close the program when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
