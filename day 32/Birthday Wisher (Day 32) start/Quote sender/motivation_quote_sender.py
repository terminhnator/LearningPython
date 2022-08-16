import smtplib
import datetime as dt
from random import *

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(day_of_week)

with open("quotes.txt", mode="r") as quotes_file:
    data = quotes_file.readlines()
    print(data)

if now.weekday() == 3:
    quote = choice(data)
    print(quote)

    my_email = "terminhnator.1003@gmail.com"
    password = "1Yz9j%R7Pr4@"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="terminhnator@yahoo.com",
            msg=f"Subject:Your weekly motivational email\n\n{quote}"
        )
