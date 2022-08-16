# ------------------ Extra Hard Starting Project ------------------ #

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas as pd
import random
import smtplib

# ------------------ Email Setup ------------------ #

my_email = "terminhnator.1003@gmail.com"
password = "1Yz9j%R7Pr4@"

# ------------ Choose a random letter ------------- #

letter_of_choice = f"./letter_templates/letter_{random.randint(1,3)}.txt"

# ----------- Get the current datetime ------------ #

now = dt.datetime.now()
current_month = now.month
current_day = now.day

# ----------- Read Birthday Data ------------ #

data = pd.read_csv("birthdays.csv")
birthday_data = data.to_dict(orient="records")

# ---------------- Send Email --------------- #

PLACEHOLDER = "[NAME]"

for birthday in birthday_data:
    birthday_email = birthday["email"]
    birthday_name = birthday["name"]
    birthday_month = birthday["month"]
    birthday_day = birthday["day"]

    if birthday_month == current_month and birthday_day == current_day:

        with open(letter_of_choice, mode="r") as letter:
            letter_contents = letter.read()
            new_letter = letter_contents.replace(PLACEHOLDER, birthday_name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_email,
                                msg=f"Subject:Happy birthday\n\n{new_letter}"
                                )
