# Face Recognition Application
This is a simple face recognition application that detects and displays faces in images or real-time video using the **face_recognition** and **opencv-python** libraries.

## Prerequisites
+ Docker: Make sure Docker is installed on your machine.

## Usage
1. Clone this repository to your local machine.

2. Navigate to the project directory.

3. Open the **main.py** file in a text editor and adjust the **video_mode** variable to *True* or *False* depending on whether you want to perform face recognition on images or video.

4. If **video_mode** is set to *False*, provide the path to the image file in the **path_image** variable.

5. In a terminal, run the following command to start the application:
`docker-compose up`
This will build the Docker image and start the container (add **--build** if you change the value of **video_mode**).

6. If **video_mode** is set to *True*, the application will use the webcam as the video source. It will display the video feed with detected faces and the number of faces found in each frame.

If **video_mode** is set to *False*, the application will process the specified image and display the image with detected faces.

Press the **Esc** key to exit the application.

Please note that the first time you run the **docker-compose up** command, it may take some time to build the Docker image. Subsequent runs will be faster.

**Note**: If you encounter any issues related to display or video access, make sure you have executed the **xhost +** command in your terminal before running the **docker-compose up** command.

Enjoy face recognition with Docker!
