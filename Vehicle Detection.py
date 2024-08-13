# VEHICLE DETECTION USING OPEN CV IN PYTHON

import cv2
#  it is Path to the Haar cascade file
cascade_path = r'C:\Users\pc\Desktop\project\Vehicle Detection\haarcascade_car.xml'
vehicle_cascade = cv2.CascadeClassifier(cascade_path)
# it check the cascade file loaded correctly
if vehicle_cascade.empty():
    print(f"Error: Could not load Haar cascade from {cascade_path}.")
    exit()
# it is path to the video file
video_path = r'C:\Users\pc\Desktop\project\Vehicle Detection\Cars.mp4'
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Could not open video file at {video_path}.")
    exit()
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cv2.namedWindow('Vehicle Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Vehicle Detection', original_width, original_height)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame or end of video.")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # it is used to detect vehicles in the frame
    vehicles = vehicle_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)
    for (x, y, w, h) in vehicles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Vehicle', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # it display the resulted frame
    cv2.imshow('Vehicle Detection', frame)
    # user has to press 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Detection stopped by user.")
        break
cap.release()
cv2.destroyAllWindows()


