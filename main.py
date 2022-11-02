from flask import render_template, Response
from app import app
import os
import cv2

picFolder = os.path.join('static','pics')
camera = cv2.VideoCapture(0)

app.config['UPLOAD_FOLDER'] = picFolder

def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/")
def home():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'hospital.png')
    return render_template("home.html", user_image = pic1)

@app.route("/rec")
def rec():
    return render_template("rec.html")

@app.route("/video")
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
