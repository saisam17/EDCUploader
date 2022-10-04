from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os, flask
# noinspection PyUnresolvedReferences
import excel2flapjack as e2f
#import excel2sbol

cwd = os.getcwd()
upload_folder = os.path.join(cwd,'public')

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = upload_folder

@app.route('/status')
def status():
    return("The Public Server for the EDC is up and running")

@app.route('/upload')
def upload_file_template():
   return render_template('upload.html')

	
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      fj_url = "flapjack.rudge-lab.org:8000"
      fj_user = request.form['fjusername']
      fj_pass = request.form['fjpwd']
      with open(request.files['file']) as f:
         hash_map=e2f.main.flapjack_upload(fj_url, fj_user, fj_pass, f)
         print(hash_map)

      #f = request.files['file']

      # hashmap = excel2flapjack.upload(f, fj_user, fj_pass)
      # file = excel2sbol(f)
      #linked_file = addflapjacklinks(file)
      #submit linked_file to synbiohub
      #f.save(os.path.join(upload_folder, secure_filename(f.filename)))
      #print(f)
      #print(request.form)
      #print(request.form['sbhusername'])
      return render_template('upload_success.html', file_uploaded=secure_filename(f.filename))

      #fj_user = "username2"
      #fj_pass = "pwd2"