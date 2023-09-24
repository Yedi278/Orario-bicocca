from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import date
import sys

time = date.today()

day = time.day
month = time.month
year = time.year

url  = 'https://gestioneorari.didattica.unimib.it/PortaleStudentiUnimib/index.php?view=easycourse&form-type=corso&include=corso&txtcurr=2+-+PERCORSO+COMUNE&anno=2023&scuola=AreaScientifica-Fisica&corso=E3001Q&anno2%5B%5D=GGG%7C2&date=22-09-2023&periodo_didattico=&_lang=it&list=&week_grid_type=-1&ar_codes_=&ar_select_=&col_cells=0&empty_box=0&only_grid=0&highlighted_date=0&all_events=0&faculty_group=0#'
url2 = 'https://gestioneorari.didattica.unimib.it/PortaleStudentiUnimib/index.php?view=easycourse&form-type=corso&include=corso&txtcurr=2+-+PERCORSO+COMUNE&anno=2023&scuola=AreaScientifica-Matematica&corso=E3501Q&anno2%5B%5D=GGG%7C2&date=24-09-2023&periodo_didattico=&_lang=it&list=&week_grid_type=-1&ar_codes_=&ar_select_=&col_cells=0&empty_box=0&only_grid=0&highlighted_date=0&all_events=0&faculty_group=0#'

url =  url[:226] + str(day) + '-' + str(month) + str(year) + url[236:]
url2 = url2[:230] + str(day) + '-' + str(month) + str(year) + url2[240:]

a = sys.argv[1]
if   a == '1': link = url
elif a == '2': link = url2
else: 
    print("Input Error") 
    quit()

driver = webdriver.Firefox()
driver.get(link)