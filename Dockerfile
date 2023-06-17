FROM python:3.10

WORKDIR /my_face_recognition

RUN apt-get update && apt-get install -y cmake

RUN git clone https://github.com/davisking/dlib.git

RUN cd dlib && \
    mkdir build; cd build; cmake ..; cmake --build . && \
    cd .. ; python3 setup.py install

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]