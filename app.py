from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from fill_out_form import add_patient_info_to_jpg

app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index.html')

@app.route('/forms')
def index2():
    return render_template('forms.html')

@app.route('/medicines')
def index3():
    return render_template('medicines.html')

@app.route('/diagnoses')
def index4():
    return render_template('diagnoses.html')

@app.route('/login')
def index5():
    return render_template('login.html')

@app.route('/new_form', methods=['GET', 'POST'])
def index6():
    if request.method == 'POST':
        medicaid = request.form['medicaid']
        name = request.form['name']
        dob = request.form['dob']
        sex = request.form['sex']
        address = request.form['address']
        phone = request.form['phone']

        # Execute the desired Python script with the captured variables
        # Create or modify an image using Pillow (PIL)
        information = (medicaid, name, dob, sex, address, phone)
        add_patient_info_to_jpg(information, 'static/1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg', 'static/1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg')
    
    # Return the image as a response
    return send_file('static/1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
