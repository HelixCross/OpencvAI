import cv2
import numpy as np


# Define a function to get the current frame from the web cam.
def get_frame(cap, scaling_factor):
    _, frame = cap.read()

    # Resize the video.
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    # Define the foreground to be removed.
    bg_subtraction = cv2.createBackgroundSubtractorMOG2()

    # Define the history for this frame event.
    history = 100

    # Define th learning rate.
    learning_rate = 1.0 / history

    # Keep reading the frames from the web cam.
    # Until the user hits the ESC.
    while True:
        frame = get_frame(cap, 0.5)

        # Compute the mask for the foreground.
        mask = bg_subtraction.apply(frame, learningRate=learning_rate)

        # Conversion from the garysvale to RGB colour of the video.
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Display the image.
        cv2.imshow("Input", frame)
        cv2.imshow("Output", mask & frame)

        # Check if the user will hit the ESC.
        c = cv2.waitKey(10)
        if c == 27:
            break

    # Release the video from the loop.
    cap.release()

    # Close the windows.
    cv2.destroyAllWindows()