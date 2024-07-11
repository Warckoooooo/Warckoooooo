from datetime import datetime
from dateutil.relativedelta import relativedelta
import re

# Define my birth date
birth_date = datetime(2002, 9, 2)

# Calculate my age in days
today = datetime.today()
age_in_days = (today - birth_date).days

# Read the content of README.md
with open("README.md", "r") as file:
    readme_content = file.read()

# Update the age in README.md
updated_content = re.sub(r'Hi 👋, I\'m Ryan - \d+ days old', f"Hi 👋, I'm Ryan - {age_in_days} days old", readme_content)

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(updated_content)
