import face_recognition
import cv2
import os

video_mode = False


class tools :

    def draw_point(list_of_point, image):
        for point in list_of_point:
            if (video_mode == True):
                point = (point[0] * 4, point[1] * 4) # here we multiply by 4 because we resized the image by 0.25
            cv2.circle(image, point, 2, (0, 255, 0), -1)
        return image

    def define_landmarks(image ,image_video):
        if (video_mode == True):
            face_landmarks_list = face_recognition.face_landmarks(image_video)
        else:
            face_landmarks_list = face_recognition.face_landmarks(image)

        for nbr_of_face, face_landmarks in enumerate(face_landmarks_list):
            for landmark in face_landmarks.values():
                tools.draw_point(landmark, image)

        print("I found {} face(s) in this image.".format(len(face_landmarks_list)))
        return image


class mode :

    def image_mode():
        path_image = "image/2_face.jpg"
        image = face_recognition.load_image_file(path_image)
        image = tools.define_landmarks(image, None)

        if os.environ.get("DISPLAY"):
            cv2.imshow("Result", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    def video_mode():
        video_capture = cv2.VideoCapture(0)

        while True:
            unused, frame = video_capture.read()

            #improve performance
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color to RGB color
            rgb_frame = small_frame[:, :, ::-1]

            frame = tools.define_landmarks(frame, rgb_frame)

            cv2.imshow('Result', frame)

            # 27 is the Escape Key
            if cv2.waitKey(1) == 27 :
                break
        video_capture.release()
        cv2.destroyAllWindows()


def main():
    if(video_mode == True):
        mode.video_mode()
    else:   
        mode.image_mode()

if __name__ == "__main__":
    main()