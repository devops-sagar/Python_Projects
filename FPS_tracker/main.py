import cv2
import time

# Load the video
cap = cv2.VideoCapture("vid.mp4")

# Get the frames per second (fps) of the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Start the timer
start = time.time()

# Process each frame of the video
while True:
    # Read the next frame
    ret, frame = cap.read()

    # Check if we've reached the end of the video
    if not ret:
        break

    # Perform processing on the frame here

    # Display the frame
    cv2.imshow("Video", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

# Stop the timer
end = time.time()

# Calculate the number of frames processed
num_frames = cap.get(cv2.CAP_PROP_POS_FRAMES)

# Calculate the elapsed time
elapsed_time = end - start

# Calculate the frames per second
fps = num_frames / elapsed_time

# Release the video capture
cap.release()

# Close all windows
cv2.destroyAllWindows()

# Print the fps
print("Frames per second: {:.2f}".format(fps))