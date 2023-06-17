FROM python:3.10

WORKDIR /my_face_recognition

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]