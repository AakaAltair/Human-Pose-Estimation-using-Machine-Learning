import cv2
import mediapipe as mp

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Load an image
image_path = r'E:\aakash\pose detection\jump.jpg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image from {image_path}")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Perform pose estimation
results = pose.process(image_rgb)

# Create copies for different visualizations
original_image = image.copy()
landmarks_only_image = image.copy()
full_annotation_image = image.copy()

if results.pose_landmarks:
    print("Pose landmarks detected!")
    
    # Extract landmark data
    for idx, landmark in enumerate(results.pose_landmarks.landmark):
        print(f"Landmark {idx}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")
    
    # Get image dimensions
    h, w, _ = image.shape
    
    # Draw keypoints on landmarks_only_image and full_annotation_image
    for landmark in results.pose_landmarks.landmark:
        # Convert normalized coordinates to pixel coordinates
        cx, cy = int(landmark.x * w), int(landmark.y * h)
        # Draw the keypoints
        cv2.circle(landmarks_only_image, (cx, cy), 5, (0, 255, 0), -1)  # Green color, filled circle
        cv2.circle(full_annotation_image, (cx, cy), 5, (0, 255, 0), -1)  # Green color, filled circle
    
    # Draw connections on full_annotation_image
    mp_drawing.draw_landmarks(full_annotation_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
    
    # Display all three images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Landmarks Only', landmarks_only_image)
    cv2.imshow('Full Annotation', full_annotation_image)
else:
    print("No pose landmarks detected.")
    cv2.imshow('Original Image', original_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Release resources
pose.close()