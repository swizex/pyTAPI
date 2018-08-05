# Custom Gmail email sender object

This object lets you send emails securely via Gmail SMTP servers.

Security:
* two Step Google app password
* SSL connection

## Sending basic Emails

Code snippet:
```python
gmail = pyTAPI.GoogleMail()  # declaring custom object

gmail.sender = '***@gmail.com'  # account the email will display as sender
gmail.login = '***@gmail.com'  # account that is used to send the email
gmail.password = '***'  # 2-step verification app password
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple recipients possible)
gmail.subject = 'SUBJECT'  # subject of the email
gmail.content = 'CONTENT'  # contents of the email

temp = gmail.send()  # send the email

print(temp)  # debugging purposes
```

Explanation:

Declaring the custom email sender object

```python
gmail = pyTAPI.GoogleMail()  # declaring custom object
```

Adding sender email address, this is used to display from who the email was sent

```python
gmail.sender = '***@gmail.com'  # account the email will display as sender
```

Adding the login username of the account that will be used to send the email

```python
gmail.login = '***@gmail.com'  # account that is used to send the email
```

Adding the Google app password of the account that will be used to send the email

```python
gmail.password = '***'  # 2-step verification app password
```

Adding the email address/s that we will be sending the email to

```python
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple recipients possible)
```

Adding the subject of the email

```python
gmail.subject = 'SUBJECT'  # subject of the email
```

Adding the contents of the email

```python
gmail.content = 'CONTENT'  # contents of the email
```

Sending the email

```python
temp = gmail.send()  # send the email
```

Debugging

```python
print(temp)  # debugging purposes
```

`temp` will be `sent mail successfully!` if email was sent successfully or `failed to send mail! Exception: ... Error on line x` if it fails to send the email.

## Sending HTML/CSS3 Emails

Code snippet:
```python
gmail = pyTAPI.GoogleMail()  # declaring custom object

gmail.sender = '***@***.***'  # account the email will display as sender
gmail.login = '***@gmail.com'  # account that is used to send the email
gmail.password = '***'  # 2-step verification app password
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple recipients possible)
gmail.subject = 'sent programmatically using the pyTAPI library!'  # subject of the email
gmail.content = '<h1>HTML VERSION YUHU</h1>'  # contents of the email (HTML)
gmail.plain = 'PLAIN VERSION'  # (plain version of the HTML content)

temp = gmail.sendhtml()  # send the email

print(temp)  # debugging purposes
```

Explanation:

Declaring the custom email sender object

```python
gmail = pyTAPI.GoogleMail()  # declaring custom object
```

Adding sender email address, this is used to display from who the email was sent

```python
gmail.sender = '***@gmail.com'  # account the email will display as sender
```

Adding the login username of the account that will be used to send the email

```python
gmail.login = '***@gmail.com'  # account that is used to send the email
```

Adding the Google app password of the account that will be used to send the email

```python
gmail.password = '***'  # 2-step verification app password
```

Adding the email address/s that we will be sending the email to

```python
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple recipients possible)
```

Adding the subject of the email

```python
gmail.subject = 'sent programmatically using the pyTAPI library!'  # subject of the email
```

Adding HTML contents into the email

```python
gmail.content = '<h1>HTML VERSION YUHU</h1>'  # contents of the email (HTML)
```

Adding a plaintext version of the HTML contents into the email

```python
gmail.plain = 'PLAIN VERSION'  # (plain version of the HTML content)
```

Sending email

```python
temp = gmail.sendhtml()  # send the email
```

Debugging

```python
print(temp)  # debugging purposes
```

`temp` will be `sent mail successfully!` if email was sent successfully or `failed to send mail! Exception: ... Error on line x` if it fails to send the email.

## Sending Custom HTML/CSS Emails

Code snippet:

```python
gmail = pyTAPI.GoogleMail()  # declaring custom object

gmail.sender = '****@***.***'  # account the email will display as sender
gmail.login = '***@gmail.com'  # account that is used to send the email
gmail.password = '***'  # 2-step verification app password
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple recipients possible)
gmail.subject = 'sent programmatically using the pyTAPI library!'  # subject of the email
gmail.content = '<div class="container"><h1>Bootstrap content!</h1></div>'  # contents of the email (HTML)
gmail.plain = 'PLAIN VERSION'  # (plain version of the HTML content)
gmail.style = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'
gmail.meta = '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
gmail.title = '<title>TITLE!</title>'

temp = gmail.sendcustomhtml()  # send the email

print(temp)  # debugging purposes
```

Explanation:

Declaring the custom email sender object

```python
gmail = pyTAPI.GoogleMail()  # declaring custom object
```

Adding sender email address, this is used to display from who the email was sent

```python
gmail.sender = '***@gmail.com'  # account the email will display as sender
```

Adding the login username of the account that will be used to send the email

```python
gmail.login = '***@gmail.com'  # account that is used to send the email
```

Adding the Google app password of the account that will be used to send the email

```python
gmail.password = '***'  # 2-step verification app password
```

Adding the email address/s that we will be sending the email to

```python
gmail.to = '***@gmail.com'  # email to (this is an array variable, multiple recipients possible)
```

Adding the subject of the email

```python
gmail.subject = 'sent programmatically using the pyTAPI library!'  # subject of the email
```

Adding HTML contents into the email

```python
gmail.content = '<div class="container"><h1>Bootstrap content!</h1></div>'  # contents of the email (HTML)
```

Adding a plaintext version of the HTML contents into the email

```python
gmail.plain = 'PLAIN VERSION'  # (plain version of the HTML content)
```

Adding custom CSS3 style to the email

```python
gmail.style = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">'
```

Adding meta tags into the email

```python
gmail.meta = '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
```

Adding HTML title to the email

```python
gmail.title = '<title>TITLE!</title>'
```

Sending email

```python
temp = gmail.sendcustomhtml()  # send the email
```

Debugging

```python
print(temp)  # debugging purposes
```

`temp` will be `sent mail successfully!` if email was sent successfully or `failed to send mail! Exception: ... Error on line x` if it fails to send the email.
