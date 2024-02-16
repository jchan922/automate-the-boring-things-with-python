import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('test@test.com', 'password')
conn.select_folder('INBOX', readonly=True)
# search for emails
UIDs = conn.search(['SINCE 20-Aug-2015'])
rawMessage = conn.fetch([12345], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[12345][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

# get string of body text
message.text_part
message.html_part == None
message.text_part.get_payload().decode('UTF-8')

conn.list_folders()
conn.select_foler('INDOX', readyonly=False)
UIDs = conn.search(['ON 24-Aug-2015'])
conn.delete_messages(UIDs)