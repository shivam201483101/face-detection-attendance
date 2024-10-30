import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment
from base64 import b64encode

# Set up email details
sender_email = "shivam8454038839@gmail.com"  # create sendgrid acount then create a sender email and  verify that,then use that email here,use webapi and chose pyython lang,not smtp
receiver_email = "payalpandey4114@gmail.com"
subject = "Attendance Report"
body = "Please find the attached attendance file."
sendgrid_api_key = "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"  

# Path to the attachment
filename = "Attendance" + os.sep + "Attendance_2024-10-30_13-18-46.csv"

# Prepare the attachment
with open(filename, 'rb') as f:
    file_data = f.read()
    encoded_file = b64encode(file_data).decode()

# Create the email message
message = Mail(
    from_email=sender_email,
    to_emails=receiver_email,
    subject=subject,
    plain_text_content=body
)

# Add the attachment to the message
attachment = Attachment(
    file_content=encoded_file,
    file_type='text/csv',
    file_name=os.path.basename(filename),
    disposition='attachment'
)
message.attachment = attachment

# Send the email
try:
    sg = SendGridAPIClient(sendgrid_api_key)
    response = sg.send(message)
    print(f"Email sent successfully, Status Code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
