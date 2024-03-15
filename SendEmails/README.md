# SendMail

This script sends emails with attachments to a list of recipients provided in a CSV file. It uses the Gmail API to send the emails and includes rate limiting to avoid exceeding the Gmail API's sending limits.

## Dependencies

The script requires the following Python packages:

- base64
- os
- pandas
- email.message
- google.oauth2.credentials
- google_auth_oauthlib.flow
- google.auth.transport.requests
- googleapiclient.discovery
- googleapiclient.errors
- mimetypes
- threading
- time
- concurrent.futures
- logging

You can install the required packages using pip:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas
```

## How to Use
1. Prepare a CSV file with the names, registration numbers, and emails. The CSV file should have columns named 'Name', 'Registration Number', and 'Email'.

2. Update the get_details function in the script to read your CSV file:
```python
csv = pd.read_csv('path_to_your_csv_file.csv')
```
3. Update the 'from' field in the script to your email address:
4. Adjust the email message and subject as required.
5. Update the file paths to fit your directory structure. (log file, attachments directory)
6. Run the script using the command `python SendMail.py`.

## Function Descriptions
`get_credentials()`: This function handles the OAuth2 authentication flow for the Gmail API. It reads the credentials from a file named 'token.json', or prompts the user to log in if the file doesn't exist or the stored credentials are invalid.

`msg_text()`: This function returns the HTML content of the email.

`gmail_send_attachment(name, regNo, email)`: This function sends an email with an attached certificate to the given email address. It creates an EmailMessage object, adds the email content and attachment, and sends the email using the Gmail API.

`get_details()`: This function reads the names, registration numbers, and emails from the CSV file, and uses a thread pool to send emails to all recipients concurrently.

## Optimization and Constraints
The script uses a thread pool to send emails concurrently, which significantly speeds up the process when sending emails to a large number of recipients.

However, the Gmail API has a limit on the number of emails that can be sent per second. To avoid exceeding this limit, the script uses a semaphore to limit the number of emails sent per second to two. This is done by acquiring the semaphore before sending an email, and releasing it after a delay of 0.5 seconds.

## Error Handling
If an error occurs while sending an email, the script will log the error message and continue with the next email. The error messages are logged to a file named 'testLog.txt' in the './Logs' directory.