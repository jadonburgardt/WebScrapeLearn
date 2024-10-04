import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# Find elements by id
############################################################
# results = soup.find(id="ResultsContainer")
# print(results.prettify())

# find elements by HTML class name
############################################################
results = soup.find(id="ResultsContainer")

job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
  title_element = job_element.find("h2", class_="title")
  company_element = job_element.find("h3", class_="company")
  location_element = job_element.find("p", class_="location")

# extract text from HTML elements
  print(title_element.text.strip())
  print(company_element.text.strip())
  print(location_element.text.strip())
  print()

# RESULTS
###########################################
# Senior Python Developer
# Payne, Roberts and Davis
# Stewartbury, AA

# Energy engineer
# Vasquez-Davidson
# Christopherville, AA

# Legal executive
# Jackson, Chambers and Levy
# Port Ericaburgh, AA

# Fitness centre manager
# Savage-Bradley
# East Seanview, AP

# Product manager
# Ramirez Inc
# North Jamieview, AP

# ...
  
