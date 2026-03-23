import urllib.request
import bz2
import os

url = "http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2"
compressed_file = "shape_predictor_68_face_landmarks.dat.bz2"
output_file = "shape_predictor_68_face_landmarks.dat"

if not os.path.exists(output_file):
    print("Downloading the model (approx 100MB)... please wait.")
    urllib.request.urlretrieve(url, compressed_file)
    print("Extracting file...")
    with bz2.BZ2File(compressed_file) as fr, open(output_file, "wb") as fw:
        fw.write(fr.read())
    os.remove(compressed_file)
    print("Success! The model is ready.")
else:
    print("Model already exists in this folder.")