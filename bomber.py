import smtplib
import os
import schedule
import datetime
from customers import customers, bills_due

myMail = os.environ.get('MAIL')
myPass = os.environ.get('PASS')


def daily_debt_check(customers):

    bills_due(customers)

    for customer in customers:
        if customer.debt:
            mail_customer(customer)
    for customer in customers:
        print(customer.debt)


def mail_customer(customer):
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls() #encryption required
    smtpObj.login(myMail, myPass)
    ##############
    time = datetime.datetime.now()
    #############
    smtpObj.sendmail(myMail, myMail, f'''Subject: test.\n
                    This is a test-email for customer {customer._id}


                                                {time}''')

    smtpObj.quit()


schedule.every().day.at("08:00").do(daily_debt_check, customers)


while True:
    schedule.run_pending()

