import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
# connect to smtp server
conn.ehlo()
# begin encryption
conn.starttls()
# login with username and password
conn.login('from@test.com', 'password')
# send email
conn.sendmail(
	'from@test.com', 
	'to@test.com', 
	'Subject: So long...\n\nDear Test,\nSo long, and thanks for all the fish.\n\nTest')
# disconnect
conn.quit()