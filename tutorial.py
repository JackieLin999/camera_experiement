"""This is a tutorial for hold to use the baseler camera"""
from pypylon import pylon
import cv2
import numpy as np

devices = pylon.TlFactory.GetInstance().EnumerateDevices()

if len(devices) == 0:
    print("No devices detected")
else:
    print(f"Found {len(devices)} device(s):")
    for device in devices:
        print(device.GetModelName())


camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
camera.Open()

numberOfImagesToGrab = 1
camera.StartGrabbingMax(numberOfImagesToGrab)

while camera.IsGrabbing():
    grabResult = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
    if grabResult.GrabSucceeded():
        print("SizeX: ", grabResult.Width)
        print("SizeY: ", grabResult.Height)
        img = grabResult.Array
        img = np.array(img, dtype=np.uint8)
        cv2.imwrite("captured_image.png", img)
    grabResult.Release()
camera.Close()
