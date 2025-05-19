 Overview
This Python script utilizes regular expressions (regex) to validate user inputs across various fields, ensuring that the data conforms to expected formats. The script prompts the user to enter information and provides immediate feedback on the validity of each input.

 Features
The script validates the following input types:

Email Address: Checks if the email follows the standard format (e.g., user@example.com).

Phone Number: Validates formats such as (123) 456-7890, 123-456-7890, or 123.456.7890.

URL: Ensures the URL starts with http:// or https:// and contains a valid domain.

Currency Amount: Confirms the amount is prefixed with a dollar sign and includes up to two decimal places (e.g., $22.62).

Hashtags: Validates that hashtags start with # and are followed by alphanumeric characters (e.g., #Python).

 How It Works
Email Validation: The script uses a regex pattern to match typical email formats, ensuring the presence of an @ symbol and a valid domain.

Phone Number Validation: A regex pattern checks for common phone number formats, allowing optional parentheses and various separators like dashes or periods.
Stack Abuse
+1
Abstract API
+1

URL Validation: The script verifies that the URL begins with http:// or https:// and contains a valid domain structure.

Currency Amount Validation: A regex pattern ensures the amount starts with a dollar sign and includes up to two decimal places, with optional commas for thousands.

Hashtag Validation: The script checks that hashtags start with # and are followed by alphanumeric characters, ensuring they are properly formatted.

 Usage
Run the script, and it will prompt you to enter:

Your email address

Your phone number

A URL
Python in Plain English
+1
Mailtrap
+1

A currency amount

A hashtag

After each input, the script will display a message indicating whether the entered data is correctly formatted.
