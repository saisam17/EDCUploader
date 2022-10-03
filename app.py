from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, flask

cwd = os.getcwd()
upload_folder = os.path.join(cwd,'public')

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/status')
def status():
    return("The Public Server for plugin testing is up and running")

@app.route('/upload')
def upload_file_template():
   return render_template('upload.html')

	
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #hashmap = excel2flapjack.upload(f, pass, username)
      #file = excel2sbol(f)
      #linked_file = addflapjacklinks(file)
      #submit linked_file to synbiohub
      #f.save(os.path.join(upload_folder, secure_filename(f.filename)))
      #fj_user = "username2"
      #fj_pass = "pwd2"
      print(request.form)
      print(request.form['sbhusername'])
      return render_template('upload_success.html', file_uploaded=secure_filename(f.filename))
