import os
import numpy as np
import pickle
import cv2
from skimage.transform import resize
from func import get_all_parking_spots

# Załaduj wytrenowany model
model_path = './image_classification/model.p'
classifier = pickle.load(open(model_path, 'rb'))

# Załaduj współrzędne miejsc parkingowych
parking_spots = get_all_parking_spots()

# Ścieżka do pliku wideo i jego otwarcie
video_path = './image_classification/parking_1920_1080.mp4'
cap = cv2.VideoCapture(video_path)

# Sprawdź, czy wideo zostało poprawnie otwarte
if not cap.isOpened():
    print("Error opening video stream or file")

# Upewnij się, że rozmiar obrazów jest prawidłowy
image_size = (25, 27)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    for (x, y, w, h) in parking_spots:
        # Upewnij się, że współrzędne nie wykraczają poza granice obrazu
        if x + w > frame.shape[1] or y + h > frame.shape[0]:
            print(f"Coordinates {x, y, w, h} are out of bounds.")
            continue
        
        # Wytnij region zainteresowania (ROI) dla miejsca parkingowego
        roi = frame[y:y+h, x:x+w]
        
        # Sprawdź, czy ROI nie jest pusty
        if roi.size == 0:
            print(f"Empty ROI at coordinates {x, y, w, h}.")
            continue
        
        # Konwersja ROI do skali szarości
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Przeskalowanie ROI do prawidłowych wymiarów
        resized_roi = resize(gray_roi, image_size, anti_aliasing=True)

        # Spłaszczenie ROI
        flattened_roi = resized_roi.flatten()

        # Predykcja klasy ROI
        prediction = classifier.predict([flattened_roi])[0]
        label = 'empty' if prediction == 0 else 'not_empty'

        # Narysowanie prostokąta i etykiety na klatce
        color = (0, 255, 0) if label == 'empty' else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Wyświetlenie klatki z wynikami
    cv2.imshow('Frame', frame)

    # Naciśnij Q na klawiaturze, aby zakończyć
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Zwolnienie obiektu przechwytywania wideo
cap.release()
cv2.destroyAllWindows()
