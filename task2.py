# # 2. String Manipulation and Regular Expressions (20%)

import re
### Part 1
# Is based on the fact that you can have one or two intials in both first and last name
reg = re.compile("([a-z][a-z]){1,5}@(hr|it|fin|mkt|ops)\.company\.com") 

# The function is checks if the email address is in the correct format after the company standards
def validate_email(email):
    if reg.match(email):
        print(f"The email '{email}' is valid.") # message 
        return True # returning True when it is valid
    else: 
        print(f"The email '{email}' is invalid.")  # message 
        return False # returning False when it otherwise

### Part 2
# This function take the email if valid and returns the department code. If not, it returns None 
def get_department(email):
    if validate_email(email):
        match = reg.match(email)
        departmentCode = match.group(2)
        return departmentCode
    return None

### Part 3 
# This function makes a dictionary with the department codes as keys. It takes email from the list and if the departmentCode from part2 equals the key the it will be append to the dictionary
def categorize_emails(email_list):
    categorize = {'hr': [], 'it': [], 'fin':[], 'mkt': [], 'ops': []}
    for email in email_list:
        code = get_department(email)
        if code:
            categorize[code].append(email)
    return categorize

# A string with the name email
email = 'jdoe@hr.company.com'
# Call the first function, that tells if the emails is valid or not
validate_email(email)
# A variable which contains the result of our second function (the department code)
department = get_department(email)
# Output of the emails department code
print(f"{'-'*70}\nThe emails department code is: {department}\n{'-'*70}")

# A list of email as need in Part 3 
email_list = ['jdoe@hr.company.com', 'jaha@it.company.com', 'clda@fin.company.com', 'jl@ops.company.com', 'lpa@mkt.company.com', 'Svend@mkt.company.com']
# A variable which contains the result of our thrid function (the categorize email dictionary)
categorize = categorize_emails(email_list)
# Output of the company's emails categorized
print(f"{'-'*70}\nThe company's emails categorized:\n {categorize}\n{'-'*70}")


