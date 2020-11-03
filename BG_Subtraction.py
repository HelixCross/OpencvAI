import cv2
import numpy as np


# Define a function to get the current frame from the camera.
def get_frame(cap, scaling_factor):
    # Read the current frame from the camera to capture the object.
    _, frame = cap.read()

    # Resize the image.
    frame = cv2.resize(frame, None, fx=scaling_factor,
                       fy=scaling_factor, interpolation=cv2.INTER_AREA)

    return frame


if __name__ == "__main__":
    # Define the video object.
    cap = cv2.VideoCapture(0)

    # Define the capture subtractor.
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Define the number of the previous frames to learn.
    # This factor controls the learning rate of the algorithm.
    # This rate will reflect the learning rate from the model itself.
    # This will populate the history from the MOG2 so that the model can learn from it.
    # Feel free to play with the parameters to see some of the models results.
    history = 100

    # Define the learning rate.
    learning_rate = 1.0 / history

    # Keep reading the data from the frame util the user hit ESC.
    while True:
        # Grab the current frame.
        frame = get_frame(cap, 0.5)

        # Compute the mask.
        mask = bg_subtractor.apply(frame, learningRate=learning_rate)

        # Convert the mask from GRAYSCALE to BGR.
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Define the output of the images.
        cv2.imshow("Input", frame)
        cv2.imshow("Output", mask & frame)

        # Check if the user have pressed the ESC key.
        c = cv2.waitKey(10)
        if c == 27:
            break

    # Release the videos capture object.
    cap.release()
    cv2.destroyAllWindows()
