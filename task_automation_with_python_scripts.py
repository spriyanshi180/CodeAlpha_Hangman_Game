import re

# Step 1: Open and read the content of input file
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Use regex to find all email addresses
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)

# Step 3: Remove duplicates (optional)
unique_emails = list(set(emails))

# Step 4: Save the emails to a new file
with open("emails_extracted.txt", "w") as output_file:
    for email in unique_emails:
        output_file.write(email + "\n")

print("✅ Email extraction complete. Check 'emails_extracted.txt'")