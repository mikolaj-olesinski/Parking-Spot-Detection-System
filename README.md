# Parking Spot Detection System
This project implements a parking spot detection system using computer vision and machine learning techniques. It detects whether parking spots in a video feed are occupied or not using a Support Vector Machine (SVM) classifier trained on parking spot images. Used OpenCV to detect contours of rectangles in a desired area.

## Used Modules and Their Purpose
- **os**: Handling file paths and directory operations.
- **numpy**: Numerical operations and array handling.
- **scikit-image (skimage)**: Image processing tasks such as reading, resizing images, and preprocessing.
- **scikit-learn**: Training SVM model, grid search for hyperparameter tuning, and evaluating model accuracy.
- **opencv-python (cv2)**: Video input/output operations, image processing, and drawing rectangles for visualization, detecting rectangles in desired area.
- **pickle5**: Saving and reading the model

https://github.com/mikolaj-olesinski/Parking-Spot-Detection-System/assets/137785302/7ae137ba-60ab-4337-9e58-1fe098ee8a86

![image](https://github.com/mikolaj-olesinski/Parking-Spot-Detection-System/assets/137785302/462cba78-42ea-48bc-ab05-96e6a9259413)

## Usage

1. **Instalation:**
 
    - Clone the repository:
      
      ```bash
      git clone https://github.com/mikolaj-olesinski/Parking-Spot-Detection-System
      cd Parking-Spot-Detection-System
      ```

   - Install dependencies:
    
     ```bash
     pip install -r requirements.txt
     ```
2. **Training the Model**

   - Prepare your dataset of parking spot images in the clf-data directory with subdirectories empty and not_empty.
  
   - Run **get_model.py** to train and save the SVM model (model.p):

     ```bash
     python get_model.py
     ```

3. **Running the Parking Spot Detection System:**
   - Adjust the video_path variable in main.py to point to your input video file (parking_1920_1080.mp4 or parking_crop.mp4 for cropped video).
   - Run **classification_on_video.py** to process the video and visualize parking spot occupancy:
  
     ```bash
     python classification_on_video.py
     ```
     
   - Pree 'q' to quit apllication when the video is active
