import requests
from bs4 import BeautifulSoup

page = requests.get("http://pes.edu/events/")
print(page.status_code)
# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
# print(list(soup.children))
# print([type(item) for item in list(soup.children)])
event_list = soup.find_all(class_='col-md-8 col-sm-7')
date_list = soup.find_all(class_='date-block')
# print(date_list)

for event in event_list:
	# print('--------\n New Event Found \n--------')
	# print(event)
	print(event.find_all(class_='main-color-1-hover')[0].get_text())

print('\n')

for dateAndMonth in date_list:
	# print('--------\n Date and Month \n--------')
	month = dateAndMonth.find_all(class_='month')
	day = dateAndMonth.find_all(class_='day')
	print(month[0].get_text(),day[0].get_text())