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
    print(totalRating)

    # Overall performance 
    if totalRating.count('Excellent') == 4: 
        overallRating = 'Outstanding'
    elif totalRating.count('Poor') >= 2:  
        overallRating = 'Needs Improvement'
    elif totalRating.count('Good') + totalRating.count('Excellent') >= 3: # Because it was Good or better
        overallRating = 'Strong Performer'
    else:
        overallRating = 'Satisfactory'
    return overallRating

# Not all employees will have the same, so here the HR department can enter the information from the individual employee:
print(f'{"-"*30}\nThis is a evaluating program for performance rating of our employees! How was the employee performance:\n{"-"*30}')
sales = int(input('Sales Target Achievement:\nEnter: >'))
customer = int(input('Customer Satisfaction Score:\nEnter: >'))
attendance = int(input('Attendance Record:\nEnter: >'))
peer = int(input('Peer Feedback Score:\nEnter: >'))
# The dictionary with the information of the employee:
data = {
    'salesTarget': sales, 
    'CustomerSatisfaction': customer, 
    'attendance': attendance, 
    'peerFeedback': peer, 
    }

# Main code to execute the functions and output the rating result
overallRating = evaluate_performance(data)
print(f"{'-'*30}\nThe employee's overall performance in the month has been: {overallRating}\n{'-'*30}")








