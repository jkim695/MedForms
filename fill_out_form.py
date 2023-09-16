from add_text_to_jpg import add_text_to_image
from patient_code_to_info import print_patient_info, patient_name_to_code, patient_code_to_info
from doctor_login import login, add_patients

def add_patient_info_to_jpg(information):
    medicaid_number, full_name, DOB, sex, telephone, address = print_patient_info(information)
    input_image_path = "1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg"
    output_image_path = "1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg"
    font_size = 20
    text_color = (255, 0, 0)
    add_text_to_image(input_image_path, output_image_path, medicaid_number, (249, 305), font_size, text_color)
    add_text_to_image(input_image_path, output_image_path, full_name, (218, 334), font_size, text_color)
    add_text_to_image(input_image_path, output_image_path, DOB, (125, 360), font_size, text_color)
    add_text_to_image(input_image_path, output_image_path, sex, (289, 360), font_size, text_color)
    add_text_to_image(input_image_path, output_image_path, telephone, (486, 304), font_size, text_color)
    add_text_to_image(input_image_path, output_image_path, address, (428, 359), font_size, text_color)
    
def doctor_log_in(accounts, username, password):
    if login(accounts, username, password) == True:
        name = accounts[username][1]
        address = accounts[username][2]
        telephone = accounts[username][3]
        provider_id = accounts[username][4]
        patients = accounts[username][5]
        input_image_path = "1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg"
        output_image_path = "1694880457959-c696be11-7d15-4f4a-a6a5-f66b1a543d4020) FINALV_1 copy.jpg"
        font_size = 20
        text_color = (255, 0, 0)
        add_text_to_image(input_image_path, output_image_path, name, (442, 453), font_size, text_color)
        add_text_to_image(input_image_path, output_image_path, address, (408, 506), font_size, text_color)
        add_text_to_image(input_image_path, output_image_path, telephone, (465, 534), font_size, text_color)
        add_text_to_image(input_image_path, output_image_path, provider_id, (574, 425), font_size, text_color)
        new_patient = str(input('Is this a new patient? Y for Yes and N for No: \n'))
        if new_patient == 'Y':
            pfirst_name = input('Please enter their first name: \n')
            plast_name = input('Please enter their last name: \n')
            pmiddle_initial = input('Please enter their middle initial: \n')
            pYOB = input('Please enter their year of birth: \n')
            pMOB = input('Please enter their month of birth: \n')
            pDOB = input('Please enter their day of birth: \n')
            pmedicaid = input('Please enter their medicaid number: \n')
            psex = input('Please enter their sex: \n')
            p_telephone = input('Please enter their telephone number: \n')
            p_address = input('Please enter their address: \n')
            patients = add_patients(patients, pmedicaid, pfirst_name, plast_name, pmiddle_initial, pYOB, pMOB, pDOB, psex, p_telephone, p_address)
            code = patient_name_to_code(pfirst_name, plast_name, pmiddle_initial, pYOB, pMOB, pDOB)
            code, information = patient_code_to_info(pmedicaid, pfirst_name, plast_name, pmiddle_initial, pYOB, pMOB, pDOB, psex, p_telephone, p_address)
            pmedicaid_number, pfull_name, pDOB, psex, ptelephone, paddress = print_patient_info(patients[code])
            add_patient_info_to_jpg(information)
            
        if new_patient == 'N':
            code = input('Please enter their patient code: \n')
            pmedicaid_number, pfull_name, pDOB, psex, ptelephone, paddress = print_patient_info(patients[code])
            code, information = patient_code_to_info(pmedicaid, pfirst_name, plast_name, pmiddle_initial, pYOB, pMOB, pDOB, psex, p_telephone, p_address)
            add_patient_info_to_jpg(information)