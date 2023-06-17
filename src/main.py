import face_recognition
import cv2
import os

video_mode = False

if video_mode == False:
    path_image = "image/2_face.jpg"

    image = face_recognition.load_image_file(path_image)
    face_landmarks_list = face_recognition.face_landmarks(image)

    for nbr_of_face, face_landmarks in enumerate(face_landmarks_list):
        print("=" * 100)
        print("Face nbr", nbr_of_face)
        for landmark in face_landmarks.values():
            for point in landmark:
                print(point)
                cv2.circle(image, point, 2, (0, 255, 0), -1)

    print("I found {} face(s) in this image.".format(nbr_of_face + 1))

    if os.environ.get("DISPLAY"):
        cv2.imshow("Result", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if (video_mode == True):
    video_capture = cv2.VideoCapture(0)

    while True:
        unused, frame = video_capture.read()
        #improve performance
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color to RGB color
        rgb_frame = frame[:, :, ::-1]

        face_landmarks_list = face_recognition.face_landmarks(rgb_frame)

        for nbr_of_face, face_landmarks in enumerate(face_landmarks_list):
            for landmark in face_landmarks.values():
                for point in landmark:
                    point = (point[0] * 4, point[1] * 4) # here we multiply by 4 because we resized the image by 0.25
                    cv2.circle(frame, point, 2, (0, 255, 0), -1)

        print("I found {} face(s) in this frame.".format(len(face_landmarks_list)))
        cv2.imshow('Result', frame)

        # 27 is the Escape Key
        if cv2.waitKey(1) == 27 :
            break
        video_capture.release()
        cv2.destroyAllWindows()
