def diagnostics_codes(file_path):
    result_dict = {}
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            # Split the line at the first space
            try:
                key, value = line.strip().split(' ', 1)
                try:
                    if key[1] != '0' and key[1] != '1' and key[1] != '2' and key[1] != '3' and key[1] != '4' and key[1] != '5' and key[1] != '6' and key[1] != '7' and key[1] != '8' and key[1] != '9':
                        result_dict[tempkey] = result_dict[tempkey] + ' ' + value
                    else:
                        result_dict[key] = value
                        tempkey = key
                except IndexError:
                    result_dict[tempkey] = result_dict[tempkey] + ' ' + value 
            except ValueError:
                result_dict[tempkey] = result_dict[tempkey] + ' ' + value
    return result_dict

# Example usage
file_path = 'codes/diagnostic_codes.txt'  
result_dict = diagnostics_codes(file_path)
print(result_dict)

