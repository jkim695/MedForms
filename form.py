from fill_out_form import add_patient_info_to_jpg, doctor_log_in
from patient_code_to_info import patient_code_to_info, print_patient_info
from doctor_login import create_account, login
from accounts import accounts, patients

print(accounts)
print(patients)
create_account(accounts, 'BWen', '55555', 'Benjamin Wen', '3', '5', '666666666', patients)
doctor_log_in(accounts, 'BWen', '55555')
print(patients)
print(accounts)