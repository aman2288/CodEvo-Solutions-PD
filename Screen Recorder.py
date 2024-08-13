import cv2
import pyautogui
import win32api
import numpy as np
import time
import threading
import tkinter as tk

recording = False
stop_recording_event = threading.Event()
recording_number = 1

def start_new_recording(filename):
    return cv2.VideoWriter(filename, fourcc, 30.0, dim)

def record_screen():
    global recording_number
    filename = f"recording_{recording_number}.avi" # you can change the name of recording 
    print(f"Starting new recording: {filename}")
    output = start_new_recording(filename)
    start_time = time.time()
    record_duration = 10  # you can change time duration

    while recording:
        image = pyautogui.screenshot()
        frame = np.array(image)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        output.write(frame)

        if (time.time() - start_time) > record_duration:
            print(f"Duration ended for: {filename}")
            break

    output.release()
    recording_number += 1

def start_recording():
    global recording
    recording = True
    stop_recording_event.clear()
    record_thread = threading.Thread(target=record_screen)
    record_thread.start()

def stop_recording():
    global recording
    recording = False
    stop_recording_event.set()

def on_close():
    stop_recording()
    root.destroy()

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
dim = (width, height)
fourcc = cv2.VideoWriter_fourcc(*"XVID")

root = tk.Tk()
root.title("Screen Recorder")

start_button = tk.Button(root, text="Start Recording", command=start_recording)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
