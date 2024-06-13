import cv2
import numpy as np
from func import get_parking_spots_in_column
# Ścieżka do pliku wideo i jego otwarcie
video_path = './image_classification/parking_1920_1080.mp4'
cap = cv2.VideoCapture(video_path)

# Sprawdź, czy wideo zostało poprawnie otwarte
if not cap.isOpened():
    print("Error opening video stream or file")

# Przybliżone współrzędne miejsc parkingowych
approx_parking_spots = get_parking_spots_in_column()

# Funkcja do wykrywania miejsc parkingowych na podstawie jednej klatki w określonym obszarze
def refine_parking_spot(frame, x, y, w, h):
    roi = frame[y:y+h, x:x+w]
    
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
        cv2.rectangle(frame, (refined_spot[0], refined_spot[1]), (refined_spot[0]+refined_spot[2], refined_spot[1]+refined_spot[3]), (0, 255, 0), 2)
    
    # Wyświetlenie klatki z wynikami
    cv2.imshow('Frame', frame)

    # Naciśnij Q na klawiaturze, aby zakończyć
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Zwolnienie obiektu przechwytywania wideo
cap.release()
cv2.destroyAllWindows()
