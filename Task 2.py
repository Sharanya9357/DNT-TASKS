import cv2

# Open the input video file
input_video = cv2.VideoCapture('input_video.mp4')

# Get the video dimensions
frame_width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculate the frame rate and the frame interval to skip
frame_rate = int(input_video.get(cv2.CAP_PROP_FPS))
frame_interval = int(1.0 / frame_rate / 0.75)

# Create the output video file
output_video = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (frame_width, frame_height))

# Loop over the frames of the input video and write out every frame_interval-th frame
frame_num = 0
while True:
    ret, frame = input_video.read()
    if not ret:
        break

    if frame_num % frame_interval == 0:
        output_video.write(frame)

    frame_num += 1

# Release the video objects
input_video.release()
output_video.release()
