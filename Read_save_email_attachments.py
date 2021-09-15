import win32com.client as win32 #pip install pypiwin32 to work with windows operating sysytm
import datetime
import os
import csv
import pathlib
import glob


# Format date to look like sent on date.
dateToday = datetime.datetime.today()
trailing_week = datetime.datetime.today() + datetime.timedelta(days= -6) # One week prior
FormatedDate=('{:04d}'.format(dateToday.year)+'-'+'{:02d}'.format(dateToday.month)+'-'+'{:02d}'.format(dateToday.day))
Formated_trailing_week = ('{:04d}'.format(trailing_week.year)+'-'+'{:02d}'.format(trailing_week.month)+'-'+'{:02d}'.format(trailing_week.day))

# Your path
path = r"C:\Users"

# Creating an object for the outlook application.
outlook = win32.Dispatch("Outlook.Application").GetNamespace("MAPI")
# Access inbox -- inbox is folder 6, other folders have different numbers.
inbox=outlook.GetDefaultFolder(6)
# For accessing items in the inbox
messages=inbox.Items

def save_attachments(sender,item):
    # To iterate through inbox emails using inbox.Items object.
    for message in messages:
        try:
            # Conditions can be on sender, subject, senton.date etc.
            if (str(message.Sender) == sender) and (str(message.senton.date()) >= Formated_trailing_week):
                #body_content = message.body
                # Creating an object for the message.Attachments.
                attachment = message.Attachments
                # To check which item is selected among the attacments.
                # To iterate through email items using message.Attachments object.
                for attachment in message.Attachments:
                    # To save the particular attachment at the desired location in your hard disk.
                    file_name = str(attachment)
                    attachment.SaveAsFile(os.path.join(path, file_name))
            else:
                pass
            message = messages.GetNext()
        except:
            message = messages.GetNext()
    return True


if __name__ == "__main__":
    save_attachments("sender_name", 1)
