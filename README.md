# Daily-Birthday-Reminder

A simple Python script to automate daily text message reminders for friends and family's birthdays. This script uses Twilio's SMS API to send notifications.

## Features

- Easy to use: Add birthdays in a simple dictionary format.
- Automated: Set it up once, and it runs daily to check if there's a birthday.
- Customizable: Easily modify the message content or add more functionality.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- A [Twilio](https://www.twilio.com/) account for sending SMS.
- Twilio credentials: Account SID, Auth Token, and a Twilio Phone Number.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cargonriv/daily-bday-reminder.git
```

2. Navigate to the project directory:
```bash
cd daily-bday-reminder
```

3. Install the required package:
```bash
pip install twilio
```

## Setup
1. Open `main.py` in a text editor.
2. Replace `YOUR_TWILIO_ACCOUNT_SID`, `YOUR_TWILIO_AUTH_TOKEN`, `YOUR_TWILIO_PHONE_NUMBER`, and `YOUR_PHONE_NUMBER` with your actual Twilio details and phone number.
3. Add the `birthdays` in the birthdays dictionary with the format `'Name': 'MM-DD'`.

## Usage
Run the script manually to test:
```bash
python main.py
```

## Automating the Script
To send reminders automatically every day, set up a task scheduler:

- Windows: Use Task Scheduler to run the script daily.
- Linux/Mac: Set up a cron job. For example, to run at 8 AM daily, add this to your crontab:
```bash
0 8 * * * /usr/bin/python3 /path/to/main.py
```

## Contributing
Contributions to the Daily-Birthday-Reminder project are welcome:

1. Fork the project.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Contact
Your Name - cargonriv@pm.me

Project Link: https://github.com/cargonriv/daily-bday-reminder