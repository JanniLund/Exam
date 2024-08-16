# 1. Functions and Flow Control - a) Employee Performance Rating (15%)

# Function that evaluate how the employee have performed overall
def evaluate_performance(data):
    # Evaluating Sales Target Achievemen
    if data['salesTarget'] < 80:  
        salesRating = 'Poor'
    elif data['salesTarget'] < 100: 
        salesRating = 'Average'
    elif data['salesTarget'] < 120:
        salesRating = 'Good'
    else:
        salesRating = 'Excellent'

    # Evaluating Customer Satisfaction Score
    if data['CustomerSatisfaction'] < 6:  
        customerRating = 'Poor'
    elif data['CustomerSatisfaction'] < 8: 
        customerRating = 'Average'
    elif data['CustomerSatisfaction'] < 10:
        customerRating = 'Good'
    else:
        customerRating = 'Excellent'

    # Evaluating Attendance Record
    if data['attendance'] < 20:  
        attendanceRating = 'Poor'
    elif data['attendance'] < 25: 
        attendanceRating = 'Average'
    elif data['attendance'] < 28:
        attendanceRating = 'Good'
    else:
        attendanceRating = 'Excellent'

    # Evaluating Peer Feedback Score
    if data['peerFeedback'] < 4:  
        peerRating = 'Poor'
    elif data['peerFeedback'] < 7: 
        peerRating = 'Average'
    elif data['peerFeedback'] < 9:
        peerRating = 'Good'
    else:
        peerRating = 'Excellent'
    
    totalRating = [salesRating, customerRating, attendanceRating, peerRating]

    # Overall performance 
    if totalRating.count('Excellent') == 4: 
        overallRating = 'Outstanding'
    elif totalRating.count('Poor') == 2:  
        overallRating = 'Needs Improvement'
    elif totalRating.count('Good' or 'Excellent') == 3:
        overallRating = 'Strong Performer'
    else:
        overallRating = 'Satisfactory'
    return overallRating


data = {}
print(f'{"-"*30}\nThis is a evaluating program for performance rating of our employees! How was the employee performance:\n{"-"*30}')
sales = int(input('Sales Target Achievement:\n1. Less than 80%\n2. 80% to 100%\n3. 100% to 120%\n4. Above 120%\nEnter: >'))
customer = int(input('Customer Satisfaction Score:\n1. Less than 6\n2. 6 to 7\n3. 8 to 9\n4. 10\nEnter: >'))
attendance = int(input('Attendance Record:\n1. Less than 20 days\n2. 20 to 24 days\n3. 25 to 27 days\n4. 28 and more days\nEnter: >'))
peer = int(input('Peer Feedback Score:\n1. Less than 4\n2. 4 to 6\n3. 7 to 8\n4. 9 to 10\nEnter: >'))
data = {
    'salesTarget': sales, 
    'CustomerSatisfaction': customer, 
    'attendance': attendance, 
    'peerFeedback': peer, 
    }

# Main code to execute the functions and output the rating result
overallRating = evaluate_performance(data)
print(f"{'-'*30}\nThe employee's overall performance in the month has been: {overallRating}\n{'-'*30}")








