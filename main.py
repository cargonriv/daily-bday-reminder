#!/usr/bin/env python3

import datetime

from twilio.rest import Client

from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, YOUR_NUMBER

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
twilio_number = TWILIO_NUMBER
your_number = YOUR_NUMBER

# Birthdays in the format: 'Name': 'MM-DD'
birthdays = {
    'Alice': '12-17',
    'Bob': '01-15',
    # Add more birthdays here
}

# Current date
current_date = datetime.datetime.now().strftime("%m-%d")

# Twilio client
client = Client(account_sid, auth_token)

# Check each birthday
for name, birthday in birthdays.items():
    if birthday == current_date:
        message = client.messages.create(
            body=f"Reminder: It's {name}'s birthday today!",
            from_=twilio_number,
            to=your_number
        )
        print(f"Sent reminder for {name}'s birthday via SMS.")
