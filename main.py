import cv2
import os


def capture_photo(output_path="student_photo.jpg"):

    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    '''Webcam initialize karta hai. 0 means default webcam. cap1 = cv2.VideoCapture(0)  # Laptop default webcam
cap2 = cv2.VideoCapture(1)  # External USB webcam'''
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    print("Press 's' to save the photo or 'q' to quit without saving.")
    while True: #loop ensures the video feed keeps running until the user explicitly takes an action (save or quit).

        '''ret: ret checks whether the frame was successfully captured. A boolean value indicating if the frame was successfully captured.
        True: Frame was successfully captured.
        False: Something went wrong (e.g., no webcam connected or an error occurred).
        frame: The frame is a NumPy array that contains pixel information.The actual image (a single frame) captured by the webcam, stored as a NumPy array. This contains pixel values of the image.'''
        ret, frame = cap.read() # cap.read() reads a frame and stores it in frame. This function is part of OpenCV (cv2) and reads a single frame (image) from the webcam/video source.
        if not ret:
            print("Failed to grab frame.")
            break

        # Display the video feed
        cv2.imshow("Capture Photo", frame)

        # Wait for key press
        key = cv2.waitKey(1)
        if key == ord('s'):  # Save photo
            cv2.imwrite(output_path, frame)
            print(f"Photo saved as {output_path}")
            break
        elif key == ord('q'):  # Quit without saving
            print("Photo capture cancelled.")
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()


def get_full_name():
    print("Enter the full name of the student:")
    name = input("Full Name: ").strip() #Using .strip() ensures the input is clean and free from unnecessary whitespace.
    return name


def main():
    print("Student Attendance Form")
    name = get_full_name()
    if not name:
        print("Error: Name cannot be empty.")
        return

    photo_filename = f"{name.replace(' ', '_')}.jpg" # old : "John Doe" →  new : "John_Doe"
    print("Launching camera to capture photo...")
    capture_photo(output_path=photo_filename)

    if os.path.exists(photo_filename):
        print(f"Form completed. Name: {name}, Photo saved as {photo_filename}")
    else:
        print("Form submission failed. Photo was not saved.")


if __name__ == "__main__":
    main()
