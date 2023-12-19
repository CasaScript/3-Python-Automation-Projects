# Assistant Robot

# Email Sender Script

This Python script allows you to send emails using the SMTP protocol with SSL encryption. It is specifically configured for Gmail but can be adapted for other email providers.

## Features

- Sends emails using Gmail's SMTP server.
- Secure password handling through environment variables.
- Clear error messages for common issues like authentication failure.

## Requirements

- Python 3
- A Gmail account (or another SMTP server)
- SSL support for secure email sending

## Setup

1. Clone the repository: git clone (reposotry-URL)
2. Install Python 3 if not already installed.

3. Set up an environment variable for your email password:
- On Unix/Linux/Mac:
  ```
  export EMAIL_PASSWORD='YourPasswordHere'
  ```
- On Windows (Command Prompt):
  ```
  set EMAIL_PASSWORD=YourPasswordHere
  ```

## Usage

1. Open the script in a text editor.
2. Modify the `sender_email` and `receiver_email` variables in the `main` function with your desired email addresses.
3. Run the script:

## Notes

- The script is currently set up for Gmail's SMTP server. If using another email service, update the SMTP server and port in the `send_email` function.
- Ensure that your email account permits access via SMTP. For Gmail, this may require setting up an App Password or enabling access for less secure apps (not recommended).

## Contributions

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request on the repository.

