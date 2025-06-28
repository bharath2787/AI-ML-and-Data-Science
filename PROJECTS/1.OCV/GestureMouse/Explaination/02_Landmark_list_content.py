import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Set up the Hands model
hands = mp_hands.Hands(static_image_mode=False,  # For video stream
                       max_num_hands=2,          # Detect up to 2 hands
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set width
cap.set(4, 480)  # Set height

def print_hand_landmarks(results):
    """
    Prints hand landmark coordinates if available.
    """
    if results.multi_hand_landmarks:
        for hand_idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            print(f"\n--- Hand #{hand_idx + 1} ---")
            for id, lm in enumerate(hand_landmarks.landmark):
                print(f"Landmark {id}: x = {lm.x:.4f}, y = {lm.y:.4f}, z = {lm.z:.4f}")
    else:
        print("No hands detected.")

while True:
    success, img = cap.read()
    if not success:
        print("Failed to read frame.")
        break

    # Convert to RGB for MediaPipe
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process image and get results
    results = hands.process(imgRGB)

    # Draw landmarks and print values
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Print landmark values
    print_hand_landmarks(results)

    # Display webcam feed
    cv2.imshow("MediaPipe Hand Landmarks", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
