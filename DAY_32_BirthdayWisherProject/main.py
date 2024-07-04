##################### Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "juanvizuetevallejo@gmail.com"
PASSWORD = "gbbimjzyubriiivq"


def send_email(to_email, subject, body):
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        # Securing connection
        connection.starttls()
        # Login
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # Send mail
        connection.sendmail(
            from_addr=MY_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject:{subject}\n\n{body}"
            )

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
birthdays = pandas.DataFrame(pandas.read_csv('birthdays.csv'))
#print(birthdays)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays.iterrows()}
#print(birthdays_dict)
now = dt.datetime.now()
today_month = now.month
today_day = now.day
if (today_month,today_day) in birthdays_dict:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", mode="r") as letter_file:
        letter_content = letter_file.read()
        #print(letter_content)
        name = birthdays_dict[(today_month,today_day)]["name"]
        to_email = birthdays_dict[(today_month,today_day)]["email"]
        #print(name)
        bd_letter = letter_content.replace("[NAME]", name)
        send_email(to_email, f"Happy Birthday {name}!", bd_letter)





