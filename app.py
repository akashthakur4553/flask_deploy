from flask import *
from pyresparser import ResumeParser
import os

# from docx import Document
import nltk
nltk.data.path.append("https://github.com/akashthakur4553/flask_deploy/tree/main/stopwords/stopwords")
nltk.download("stopwords")
import spacy

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        data_l = []
        # Get the list of files from webpage
        files = request.files.getlist("file")

        # Iterate for each file in the files List, and Save them
        for file in files:
            file.save(file.filename)
            filed = file.filename
            data = ResumeParser(filed).get_extracted_data()
            data_l.append(data["name"])

        return f"<h1>Files Uploaded Successfully.!</h1> {data_l}"


# if __name__ == "__main__":
#     app.run(debug=True)
