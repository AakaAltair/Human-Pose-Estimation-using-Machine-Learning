#importing the opencv module
import cv2

# Path to the video file
video_path = r'C:\Users\RCL-PC\Downloads\cars.mp4'

#video_path = r'E:\aakash\.n\64dd54lrb86k86'

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Cannot open the video file.")
else:
    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Callback function for the trackbar
    def on_trackbar(val):
        cap.set(cv2.CAP_PROP_POS_FRAMES, val)

    # Create a window
    cv2.namedWindow('Video Player')

    # Create a trackbar
    cv2.createTrackbar('Position', 'Video Player', 0, total_frames - 1, on_trackbar)

    while True:
        # Get the current position of the trackbar
        current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        cv2.setTrackbarPos('Position', 'Video Player', current_frame)

        # Read a frame from the video
        ret, frame = cap.read()
        
        # If the frame is read successfully, process it
        if ret:
            # Convert the frame to different color spaces
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lab_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

            # Display the frames in separate windows
            cv2.imshow('Video Player', frame)
            #cv2.imshow('Gray Frame', gray_frame)
            cv2.imshow('RGB Frame', rgb_frame)
            #cv2.imshow('HSV Frame', hsv_frame)
            #cv2.imshow('LAB Frame', lab_frame)

            # Wait for 30 ms and check if the user presses 'q' to quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
        else:
            # Break the loop if no more frames are available
            break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
