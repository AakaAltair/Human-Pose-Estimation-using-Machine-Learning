

import cv2
import mediapipe as mp
import threading
import time

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Video Path
video_path = 'E:\\sq.mp4'
#video_path = r'E:\aakash\.n\.n\93aa92d'
#video_path = r'E:\aakash\.n\36kr93g82'
#video_path= 'E:\aakash\.n\.n\938h93m92s99'
#video_path= 'E:\aakash\.n\.n\.Download\92h8m9t28'
#video_path= 'E:\aakash\.n\.n\.Download\92sd92mb82w92'
cap = cv2.VideoCapture(video_path)

# Get video properties
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Scroller control
def update_frame(pos):
    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)

cv2.namedWindow("MediaPipe Pose with Scroller")
cv2.createTrackbar("Frame", "MediaPipe Pose with Scroller", 0, frame_count - 1, update_frame)

# Frame variables
current_frame = None
processing_frame = None
processed_frame = None
lock = threading.Lock()

# Frame skip settings
frame_skip_interval = 10  # Process every 2nd frame
frame_counter = 0

# Worker thread for MediaPipe processing
def process_frames():
    global current_frame, processed_frame, frame_counter
    with mp_pose.Pose(
        static_image_mode=False,
        model_complexity=0,
        enable_segmentation=False,
        min_detection_confidence=0.3,  # Lower detection threshold
        min_tracking_confidence=0.3,   # Lower tracking threshold
    ) as pose:
        while cap.isOpened():
            if current_frame is not None:
                # Process only every nth frame
                if frame_counter % frame_skip_interval == 0:
                    frame = current_frame.copy()
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results = pose.process(frame_rgb)

                    # Draw landmarks
                    if results.pose_landmarks:
                        mp_drawing.draw_landmarks(
                            frame,
                            results.pose_landmarks,
                            mp_pose.POSE_CONNECTIONS,
                            mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                            mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
                        )
                    with lock:
                        processed_frame = frame
                # Increment the frame counter
                frame_counter += 1

# Start the processing thread
thread = threading.Thread(target=process_frames, daemon=True)
thread.start()

# Main loop
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video or unable to read frame.")
        break

    # Resize frame for performance
    frame = cv2.resize(frame, (640, 360))

    # Update the scroller position
    current_position = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    cv2.setTrackbarPos("Frame", "MediaPipe Pose with Scroller", current_position)

    # Update the current frame for processing
    with lock:
        current_frame = frame

    # Display the processed frame
    with lock:
        display_frame = processed_frame if processed_frame is not None else frame

    cv2.imshow("MediaPipe Pose with Scroller", display_frame)

    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
