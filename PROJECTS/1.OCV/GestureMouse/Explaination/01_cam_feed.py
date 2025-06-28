import cv2  # Import the OpenCV library for image and video processing

# -------------------- Initialize Webcam --------------------
cap = cv2.VideoCapture(0)  # Open the default webcam (camera index 0)
cap.set(3, 640)  # Set the width of the video frame to 640 pixels
cap.set(4, 480)  # Set the height of the video frame to 480 pixels

# -------------------- Main Loop to Read and Display Frames --------------------
while True:
    success, img = cap.read()  # Read a frame from the webcam; 'success' is True if frame was read successfully
    
    # i dectected a hand 
    # we need find the location of the fingures
    # trach the distanced
    
    cv2.imshow("Webcam Feed", img)  # Display the frame in a window titled "Webcam Feed"

    # Exit loop when the user presses the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
