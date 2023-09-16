from patient_code_to_info import patient_code_to_info, print_patient_info

patients = {}
accounts = {} 

def create_account(accounts, username, password, name, address, telephone, provider_id, patients):
    # Check if the username already exists
    if username in accounts:
        print("Username already exists. Please choose a different username.")
        return
    else:
        accounts[username] = (password, name, address, telephone, provider_id, patients)
    return accounts


def login(accounts, username, password):
    # Check if the username exists and the password is correct
    if username in accounts and accounts[username][0] == password:
        return True
    else:
        print("Invalid username or password.")

def add_patients(patients, medicaid, first_name, last_name, middle_initial, year, month, day, sex, telephone, address):
    code, information = patient_code_to_info(medicaid, first_name, last_name, middle_initial, year, month, day, sex, telephone, address)
    patients[code] = information
    return patients
    

