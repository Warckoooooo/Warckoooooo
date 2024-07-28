import datetime

# Your birthdate
birthdate = datetime.date(2002, 09, 02)

# Calculate the number of days since birth
today = datetime.date.today()
days_old = (today - birthdate).days

# Read the README.md file
with open("README.md", "r") as file:
    readme_content = file.read()

# Replace the age placeholder with the actual age
updated_readme_content = readme_content.replace("I'm Ryan -  days old", f"I'm Ryan - {days_old} days old")

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(updated_readme_content)
