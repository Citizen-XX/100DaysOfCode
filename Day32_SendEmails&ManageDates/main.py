import datetime as dt
from random import choice
from collections import defaultdict
import pandas as pd
import smtplib
import os

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv

birthdays = pd.read_csv("Day32_SendEmails&ManageDates/birthdays.csv")
birthday_rows = birthdays.iterrows()
birthdays_dict = {}

my_email = "guz.rom.fer@gmail.com"
my_password = "iybm ycey panx ldeh"
recipient_mail = "thlorient@gmail.com"

today = dt.datetime.now()
today_month_and_day = (today.month, today.day)

letter_templates_path = r"Day32_SendEmails&ManageDates\letter_templates"
random_letter = f"{letter_templates_path}\{choice(os.listdir(letter_templates_path))}"

for index, row in birthday_rows:
    month_and_day = (row.month, row.day)
    if month_and_day not in birthdays_dict:
        birthdays_dict[month_and_day] = list()
    birthdays_dict[month_and_day].append((row['name'], row.email))

if today_month_and_day in birthdays_dict:
    amount_of_birthdays = len(birthdays_dict[today_month_and_day])
    print(
        f"There's {amount_of_birthdays} birthdays today")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

    letters_to_send = list()

    with open(file=random_letter, mode='r') as template_letter:
        extracted_letter = "".join(template_letter.readlines())
        for birthday_person in birthdays_dict[today_month_and_day]:
            personalized_letter = extracted_letter.replace(
                "[NAME]", f"{birthday_person[0]}")
            letters_to_send.append(personalized_letter)

# 4. Send the letter generated in step 3 to that person's email address.

        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            # Transport Layer Security. It's a way of securing the connection to our email server. The message will be encrypted if intercepted.
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            for letter in letters_to_send:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=recipient_mail, msg=f"Subject: Happy Birthday!  \n\n{letter}")

else:
    print("No birthdays today, checking back tomorrow.")
