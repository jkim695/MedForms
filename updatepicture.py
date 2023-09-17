from flask import Flask, render_template, request, redirect, url_for, send_file
import fill_out_form

app = Flask(__name__)

@app.route('intermediate.html', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        medicaid = request.form['medicaid']
        name = request.form['name']
        DOB = request.form['DOB']
        sex = request.form['sex']
        address = request.form['address']
        phone = request.form['phone']

        # Execute the desired Python script with the captured variables
        # Create or modify an image using Pillow (PIL)
        information = (medicaid, name, DOB, sex, address, phone)
        return information


@app.route('new_form.html')
def get_updated_image():
    fill_out_form.add_patient_info_to_jpg(information,'1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg', '1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg')
    return send_file('output.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
