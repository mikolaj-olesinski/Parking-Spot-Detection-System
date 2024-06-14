import os
import numpy as np
import pickle
import cv2
from skimage.transform import resize
from func import get_all_parking_spots, get_parking_spots_for_cropped


##For better performance use the cropped video uncomment/comment 101 and 141 lines

def load_model(model_path):
    """
    Function to load the classifier model from a given path.

    Parameters:
    model_path (str): Path to the model file (.p or .pkl).

    Returns:
    classifier: Loaded classifier model.
    """
    classifier = pickle.load(open(model_path, 'rb'))
    return classifier


def load_video(video_path):
    """
    Function to open and initialize video capture.

    Parameters:
    video_path (str): Path to the video file.

    Returns:
    cv2.VideoCapture: Video capture object.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video stream or file at {video_path}")
    return cap


def refine_parking_spot(frame, x, y, w, h, min_ratio=0.8, max_ratio=1.2):
    """
    Function that refines the parking spot by detecting the parking spot lines.

    Parameters:
    frame (numpy.ndarray): The frame from the video.
    x (int): The x-coordinate of the parking spot.
    y (int): The y-coordinate of the parking spot.
    w (int): The width of the parking spot.
    h (int): The height of the parking spot.
    min_ratio (float): The minimum ratio of the parking spot lines.
    max_ratio (float): The maximum ratio of the parking spot lines.

    Returns:
    tuple: The refined coordinates of the parking spot.
    """
    roi = frame[y:y+h, x:x+w]

    if roi.size == 0 or roi is None:
        return (x, y, w, h)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        
        if len(approx) == 4:
            (nx, ny, nw, nh) = cv2.boundingRect(approx)
            
            if (min_ratio * w <= nw <= max_ratio * w) and (min_ratio * h <= nh <= max_ratio * h):
                return (x + nx, y + ny, nw, nh)
    
    return (x, y, w, h)


def process_video(video_path, model_path, output_video_path):
    """
    Function to process a video, detect parking spots and save the processed video.

    Parameters:
    video_path (str): Path to the input video file.
    model_path (str): Path to the model file (.p or .pkl).
    output_video_path (str): Path to save the output processed video.
    """
    classifier = load_model(model_path)
    cap = load_video(video_path)

    if cap is None:
        return

    image_size = (25, 27)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        #approx_parking_spots = get_all_parking_spots()  # Assuming this function retrieves parking spots
        approx_parking_spots = get_parking_spots_for_cropped()  # Uncomment this line if you want to use a cropped video better performance

        refined_spots = []
        for (x, y, w, h) in approx_parking_spots:
            refined_spot = refine_parking_spot(frame, x, y, w, h)
            refined_spots.append(refined_spot)
        
        for (x, y, w, h) in refined_spots:
            if x + w > frame.shape[1] or y + h > frame.shape[0]:
                print(f"Coordinates {x, y, w, h} are out of bounds.")
                continue
            
            roi = frame[y:y+h, x:x+w]
            
            if roi.size == 0 or roi is None:
                print(f"Empty ROI at coordinates {x, y, w, h}.")
                continue
            

            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            resized_roi = resize(gray_roi, image_size, anti_aliasing=True)

            flattened_roi = resized_roi.flatten()

            prediction = classifier.predict([flattened_roi])[0]

            color = (0, 255, 0) if prediction == 0 else (0, 0, 255)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    #video_path = './parking_1920_1080.mp4'
    video_path = './parking_crop.mp4'  # Uncomment this line if you want to use a cropped video better performance
    model_path = './model.p'
    output_video_path = './output_video.mp4'

    process_video(video_path, model_path, output_video_path)
