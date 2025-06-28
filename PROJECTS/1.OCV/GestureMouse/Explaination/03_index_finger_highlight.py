import cv2  # OpenCV library for image and video processing
import gesture_detection as ht  # Custom hand tracking module (based on MediaPipe or similar)

# -------------------- Initialize Webcam --------------------
cap = cv2.VideoCapture(0)  # Open the default webcam
cap.set(3, 640)  # Set the video frame width to 640 pixels
cap.set(4, 480)  # Set the video frame height to 480 pixels

# -------------------- Initialize Hand Detector --------------------
detector = ht.handDetector()  # Create a hand detector object

# -------------------- Main Loop --------------------
while True:
    success, img = cap.read()  # Read a frame from the webcam
    img = detector.findHands(img)  # Detect and draw hand landmarks on the frame
    lmlist, bbox = detector.findPosition(img)  # Get list of hand landmarks and bounding box

    # Check if hand landmarks are detected
    if len(lmlist) != 0:
        fingers = detector.fingersUp()  # Get a list indicating which fingers are up (1) or down (0)

        # Check if only the index finger is up (fingers[1] == 1), and all others are down
        if fingers[1] == 1 and all(f == 0 for i, f in enumerate(fingers) if i != 1):
            x, y = lmlist[8][1:]  # Get the x, y coordinates of the index fingertip (landmark 8)

            # Draw a green filled circle at the index fingertip position
            cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)

            # Display a label next to the index fingertip
            cv2.putText(img, "Index Finger Up", (x + 20, y - 20),
                        cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

    # -------------------- Show Output --------------------
    cv2.imshow("Index Finger Detection", img)  # Display the processed frame

    # Exit loop and close program when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
