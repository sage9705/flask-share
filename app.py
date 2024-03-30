import socket
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Generate the IP address dynamically
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

@app.route('/')
def index():
    ip_address = get_ip_address()
    port = 5000  # You can choose any available port
    return render_template('index.html', ip_address=ip_address, port=port)


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return "No file part", 400

        files = request.files.getlist('file')  # Get a list of uploaded files
        for file in files:
            if file.filename == '':
                return "No selected file", 400

            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))

        return "Files uploaded successfully!"
    except Exception as e:
        return f"Error uploading files: {str(e)}", 500



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
