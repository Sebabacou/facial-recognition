import face_recognition
from PIL import Image, ImageDraw 

print("Build successful!")
image = face_recognition.load_image_file("image/2_face.jpg")
print(image)
# face_locations = face_recognition.face_locations(image)
# print(face_locations)