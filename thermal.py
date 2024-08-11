import cv2
import numpy as np

def process_thermal_webcam():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply a colormap to simulate thermal effect
        thermal_colormap = cv2.applyColorMap(gray_frame, cv2.COLORMAP_JET)

        # Display the original frame and thermal simulation
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Thermal Colormap', thermal_colormap)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_thermal_webcam()
