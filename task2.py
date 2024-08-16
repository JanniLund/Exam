# 2. String Manipulation and Regular Expressions (20%)

import re
# reg = re.compile("([a-z][a-z]){2,5}@[f-p]{2,4}(\.company\.com)") 
reg = re.compile("([a-z][a-z]){2,5} ") 
code = reg.match('jdoe@hr.company.com')
print(code)


# def validate_email(email):
#     while True:
#         if reg.match(email):

#             print(f"The inventory code '{email}' is valid.")
#         else: 
#             print(f"The inventory code '{emil}' is invalid.")


# def get_department(email):
#     matches = reg.finditer(email) 
#     codeDict = {match.group(3) for match in matches}
#     return codeDict

# email = ('jdoe@hr.company.com')

# def categorize_emails(email_list):








