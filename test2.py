import os
import numpy as np
import pickle
import cv2
from skimage.transform import resize
from func import get_all_parking_spots

# Załaduj wytrenowany model
model_path = './image_classification/model.p'
classifier = pickle.load(open(model_path, 'rb'))

# Załaduj przybliżone współrzędne miejsc parkingowych
approx_parking_spots = get_all_parking_spots()

# Ścieżka do pliku wideo i jego otwarcie
video_path = './image_classification/parking_1920_1080.mp4'
cap = cv2.VideoCapture(video_path)

# Sprawdź, czy wideo zostało poprawnie otwarte
if not cap.isOpened():
    print("Error opening video stream or file")

# Upewnij się, że rozmiar obrazów jest prawidłowy
image_size = (25, 27)

# Funkcja do wykrywania miejsc parkingowych na podstawie jednej klatki w określonym obszarze
def refine_parking_spot(frame, x, y, w, h):
    roi = frame[y:y+h, x:x+w]
    
    # Sprawdź, czy ROI nie jest pusty
    if roi.size == 0 or roi is None:
        return (x, y, w, h)
    
    # Konwersja do skali szarości
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    
    # Rozmycie obrazu w celu redukcji szumów
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Wykrywanie krawędzi
    edged = cv2.Canny(blurred, 50, 150)
    
    # Znajdowanie konturów
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        
        if len(approx) == 4:
            (nx, ny, nw, nh) = cv2.boundingRect(approx)
            
            if (0.5 * w <= nw <= 1.5 * w) and (0.5 * h <= nh <= 1.5 * h):
                return (x + nx, y + ny, nw, nh)
    
    return (x, y, w, h)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    refined_spots = []
    for (x, y, w, h) in approx_parking_spots:
        refined_spot = refine_parking_spot(frame, x, y, w, h)
        refined_spots.append(refined_spot)
    
    for (x, y, w, h) in refined_spots:
        # Upewnij się, że współrzędne nie wykraczają poza granice obrazu
        if x + w > frame.shape[1] or y + h > frame.shape[0]:
            print(f"Coordinates {x, y, w, h} are out of bounds.")
            continue
        
        # Wytnij region zainteresowania (ROI) dla miejsca parkingowego
        roi = frame[y:y+h, x:x+w]
        
        # Sprawdź, czy ROI nie jest pusty
        if roi.size == 0 or roi is None:
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
