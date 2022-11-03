import cv2
camera_port = 0
camera = cv2.VideoCapture(camera_port, cv2.CAP_DSHOW)
if not camera.isOpened():
    raise IOError("cantopenwebcam")
return_value, image = camera.read()
print("we have taken a pic of u,chk the folder")
cv2.imwrite("image.png", image)
camera.release()
cv2.destroyAllWindows()
