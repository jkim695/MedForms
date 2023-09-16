def patient_name_to_code(first_name, last_name, middle_name, YOB, MOB, DOB):
    #convert the first name to a secure thing
    pass_first_name = str(first_name)[0:2]
    pass_last_name = str(last_name)[0:2]
    pass_middle_name = str(middle_name)[0]
    pass_YOB = str(YOB)[-2:]
    password = pass_first_name + pass_last_name + pass_middle_name + pass_YOB + str(MOB) + str(DOB)
    return password

def patient_code_to_info(medicaid, first_name, last_name, middle_initial, year, month, day, sex, telephone, address):
    code = patient_name_to_code(first_name, last_name, middle_initial, year, month, day)
    information = (medicaid, first_name, last_name, middle_initial, year, month, day, sex, telephone, address)
    return code, information
    

def print_patient_info(information):
    medicaid_number = information[0]
    full_name = information[1] + ' ' + information[3] + ' ' + information[2]
    DOB = information[5] + '/' + information[6] + '/' + information[4]
    sex = information[7]
    telephone = information[8]
    address = information[9]
    return medicaid_number, full_name, DOB, sex, telephone, address


