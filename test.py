import pyTAPI

gmail = pyTAPI.GoogleMail()  # declaring custom object

gmail.sender = '***@gmail.com'  # account the email will display as sender
gmail.login = '***@gmail.com'  # account that is used to send the email
gmail.password = '***'  # password of the account that is used to send the email
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple senders possible)
gmail.subject = 'SUBJECT'  # subject of the email
gmail.content = 'CONTENT'  # contents of the email

temp = gmail.send()  # send the email

print(temp)  # debugging purposes
