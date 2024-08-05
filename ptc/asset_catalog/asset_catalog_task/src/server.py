import os
from flask import Flask, request


app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try: 
        file = request.files['file']
        if file:
            if not os.path.exists("../server"):
                os.mkdir("../server")
            file.save(os.path.join("../server", os.path.basename(file.filename) ))
            return f"File {file.filename} upload to server", 200

    except Exception as e:
        raise ValueError(e)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)
