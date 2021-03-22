import requests
from bs4 import BeautifulSoup

# Load the underlying html from the webpage
r = requests.get('http://www.ficpa.org/Content/Members/Member-Testimonials.aspx')
soup = BeautifulSoup(r.text, 'lxml')

# Identify the testimonials
testimonials = soup.find_all('div', class_='testimonial-wrapper')

