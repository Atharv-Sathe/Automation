# Documentation 

## Introduction
This repository contains python scripts to automate small but repeatitive and tedious tasks.

## Current Utilities
1. **Automatic Certificate/Letter Generation**
2. **Automatic Email Sending**

## Folder Structure
1. **CSVs** : Contains all CSV files used in the scripts.
2. **DesGenAuto** : Contains all required files for creating certificates/letters for participants/members.
3. **SendEmails** : Contains all required files for sending emails to the participants/members.

## Work Flow
1. Add your CSV file in the CSVs folder.
2. Add your design and font files in the Desgins and Fonts folder under DesGenAuot directory.
3. Figure out the required x and y coordinates for the text to be written on the certificate/letter.
4. Update these coordinates in the DesGen.py script.
5. Run the script using the command `python DesGen.py`.
6. The required png files will be generated and saved to Generated as well as Attachments folder under DesGenAuto directory and SendEmails directory respectively.
7. Create the HTML Format emailing text for your email.
8. Update the "from" field in the SendMail.py script.
9. Run the script using the command `python SendMail.py`.
_**Note** : The script will ask you to login to your email account and give required permissions to create a `token.json` file for the first time._
10. The emails will be sent to the recipients, two mails per second at most.
11. Information about the sent emails will be saved under Logs directory in the log file.
12. After the completion of procedure DeleteAttachments.py and DelGen.py can be run to delete all files in the Generated and Attachments directory respectively.

For more information reach out to me at atharvsathe28704@gmail.com.

#### Regards
**_TheBug_**
