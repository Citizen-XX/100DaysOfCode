import smtplib
import datetime as dt
from random import choice

today = dt.datetime.now()
day_of_week = today.weekday()

my_email = "guz.rom.fer@gmail.com"
my_password = "iybm ycey panx ldeh"
recipient_mail = "thlorient@gmail.com"

# connection = smtplib.SMTP(host="smtp.gmail.com")
# # Transport Layer Security. It's a way of securing the connection to our email server. The message will be encrypted if intercepted.
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs=recipient_mail, msg="Subject: Emailing Test \n\nWhat's good my Gigga?")
# connection.close()

# with smtplib.SMTP(host="smtp.gmail.com") as connection:
#     # Transport Layer Security. It's a way of securing the connection to our email server. The message will be encrypted if intercepted.
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=recipient_mail, msg="Subject: Emailing Test \n\nWhat's good my Gigga?")

with open(file="Day32_SendEmails&ManageDates\quotes.txt", mode="r") as file:
    all_quotes = file.readlines()
# print(choice(all_quotes))

if day_of_week == 1:
    motivational_quote = choice(all_quotes)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        # Transport Layer Security. It's a way of securing the connection to our email server. The message will be encrypted if intercepted.
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=recipient_mail, msg=f"Subject: Motivational Quote  \n\n{motivational_quote}")
