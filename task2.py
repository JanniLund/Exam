# 2. String Manipulation and Regular Expressions (20%)

import re
# Is based on the fact that you can have one or two intials in both first and last name
reg = re.compile("([a-z][a-z]){1,5}@(hr|it|fin|mkt|ops)\.company\.com") 

def validate_email(email):
    if reg.match('jdoe@hr.company.com'):
        print(f"The email '{email}' is valid.")
        return True
    else: 
        print(f"The email '{email}' is invalid.")
        return False


# def get_department(email):
#     matches = reg.finditer(email) 
#     codeDict = {match.group(3) for match in matches}
#     return codeDict

email = ('jdoe@hr.company.com')

# def categorize_emails(email_list):








