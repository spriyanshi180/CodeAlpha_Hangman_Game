import re
import os

print("Current working directory:", os.getcwd())

# Try opening the file
try:
    with open("input.txt", "r") as file:
        content = file.read()

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)
    unique_emails = list(set(emails))

    with open("emails_extracted.txt", "w") as output_file:
        for email in unique_emails:
            output_file.write(email + "\n")

    print("✅ Email extraction complete. Check 'emails_extracted.txt'")
except FileNotFoundError:
    print("❌ File 'input.txt' not found! Make sure it's in the same folder as this script.")