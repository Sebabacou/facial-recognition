import face_recognition
import cv2
import os

# Define the mode of the program
video_mode = False

# Class for tools
class tools :

    def draw_point(list_of_point, image):
        """
        Draws a point on the image.

        :param list_of_point:
            The list of points to draw on the image.
        :param image:
            The image on which the points will be drawn.

        :return image:
            The image with the points drawn on it.

        :raises None:
            No exceptions are raised.

        :example:
            Example usage of the function:
            >>> draw_point([(0, 0), (1, 1)], image)

        """
        # Draw a point on the image
        for point in list_of_point:
            if (video_mode == True):
                # Resize the point
                point = (point[0] * 4, point[1] * 4)
            # Draw the point
            cv2.circle(image, point, 2, (0, 255, 0), -1)
        # Return the image with the points drawn on it
        return image

    def define_landmarks(image ,image_video):
        """
        Defines the facial landmarks on the image.

        :param image:
            The image on which the facial landmarks will be defined.
        :param image_video:
            The image on which the facial landmarks will be defined.

        :return image:
            The image with the facial landmarks defined on it.

        :raises None:
            No exceptions are raised.

        :example:
            Example usage of the function:
            >>> define_landmarks(image)

        """
        # Find all facial landmarks in all the faces in the image
        if (video_mode == True):
            face_landmarks_list = face_recognition.face_landmarks(image_video)
        else:
            face_landmarks_list = face_recognition.face_landmarks(image)

        # Draw a point on the image
        for nbr_of_face, face_landmarks in enumerate(face_landmarks_list):
            # Print the location of each facial feature in this image
            for landmark in face_landmarks.values():
                tools.draw_point(landmark, image)

        print("I found {} face(s) in this image.".format(len(face_landmarks_list)))
        # Return the image with the facial landmarks defined on it
        return image


# Class for the mode
class mode :

    def image_mode():
        """
        Displays an image with detected facial landmarks.

        :param None:
            No parameters are required.

        :return None:
            The function does not return any value.

        :raises None:
            No exceptions are raised.

        :example:
            Example usage of the function:
            >>> image_mode()

        """
        # Path of the image to load
        path_image = "image/2_face.jpg"

        # Load the image from file
        image = face_recognition.load_image_file(path_image)

        # Define facial landmarks on the image
        image = tools.define_landmarks(image, None)

        # Check the display environment
        if os.environ.get("DISPLAY"):
            # Display the image with detected facial landmarks
            cv2.imshow("Result", image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def video_mode():
        """ 
        Displays a video with detected facial landmarks.

        :param None:
            No parameters are required.

        :return None:
            The function does not return any value.
                        #

        :raises None:
            No exceptions are raised.

        :example:
            Example usage of the function:
            >>> video_mode()

        """
        # Get a reference to webcam #0 (the default one)
        video_capture = cv2.VideoCapture(0)

        while True:
            # Grab a single frame of video
            unused, frame = video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_frame = small_frame[:, :, ::-1]

            # Define facial landmarks on the image
            frame = tools.define_landmarks(frame, rgb_frame)

            # Display the resulting image
            cv2.imshow('Result', frame)

            # Hit 'esc' on the keyboard to quit!
            if cv2.waitKey(1) == 27 :
                break
        
        # Release handle to the webcam
        video_capture.release()
        cv2.destroyAllWindows()


def main():
    if (video_mode == True):
        mode.video_mode()
    else:   
        mode.image_mode()

if __name__ == "__main__":
    main()