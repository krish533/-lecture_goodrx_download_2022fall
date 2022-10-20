import pandas
from bs4 import BeautifulSoup

import os
import re


if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

file_name="./html_files/goodrx_zoloft_tablet_50mg_30_20221019155212.html"

base_name=print(os.path.basename(file_name))

print("good")
name = re.findall('goodrx_(.*)_(.*)_(.*)_(.*)_', base_name)[0][0]
form = re.findall('goodrx_(.*)_(.*)_(.*)_(.*)_', base_name)[0][1]
dosage = re.findall('goodrx_(.*)_(.*)_(.*)_(.*)_', base_name)[0][2]
quantity = re.findall('goodrx_(.*)_(.*)_(.*)_(.*)_', base_name)[0][3]

scrape_time=re.findall('\\d{14}',base_name)[0]


print(name)
print(form)
print(doseage)
print(quantity)
print(scrape_time)
