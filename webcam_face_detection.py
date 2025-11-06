import cv2

# Step 1: Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Step 2: Start your webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open webcam")
    exit()

print("Press 'q' to close the window")

# Step 3: Loop to continuously get frames from webcam
while True:
    ret, frame = cap.read()  # Capture each frame
    if not ret:
        print("Failed to capture frame")
        break

    # Step 4: Convert to grayscale (needed for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 5: Detect faces in current frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Step 6: Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Step 7: Show the webcam window
    cv2.imshow("Webcam Face Detection", frame)

    # Step 8: Exit if user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 9: Release resources
cap.release()
cv2.destroyAllWindows()
