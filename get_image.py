from flask import Flask, send_file
from PIL import Image
import fill_out_form

app = Flask(__name__)

@app.route('/get_image')
def get_image(medicaid, name, DOB, sex, address, phone):
    # Create or modify an image using Pillow (PIL)
    information = (medicaid, name, DOB, sex, address, phone)
    img = fill_out_form.add_patient_info_to_jpg(information, '1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg')
    img.save('output.jpg')


    # Return the image as a response
    return send_file('output.jpg', mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
