import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from services import find_person, add_single_person


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        photo = request.files['photo']
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        info = request.form['info']

        filename = secure_filename(photo.filename)
        photo.save(f"external/{filename}")

        filepath = os.path.join("external", filename)

        person = add_single_person(filepath, name, age, gender, info)

        if person is False:
            return render_template("notfound.html")
        
        return redirect(url_for('index'))


    return render_template("add.html")

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(f"external/{filename}")

        filepath = os.path.join("external", filename)
        
        data = find_person(filepath)

        if data is None:
            return render_template("notfound.html")
    
        return render_template("results.html", person_info=data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print("Stopping server...")
        exit(0)
