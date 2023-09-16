def medications(file_path):
    result_dict = {}
    with open(file_path, 'r') as file:
        lines = file.read().split('\n')
        for i in range(0, 111719, 1):
            # Split the line at the first space
            key = 'NBC-' + lines[i]
            value = (lines[i+111719], lines[i+223438])
            result_dict[key] = value
    return result_dict

# Example usage
file_path = 'codes/medications.txt'  
result_dict = medications(file_path)
print(result_dict)

