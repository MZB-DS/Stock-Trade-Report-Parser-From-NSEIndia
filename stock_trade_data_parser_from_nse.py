from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html as lh
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

options = Options()
options.headless = True

symbols=[] # In this python list include all of the stock names for which we want to parse trade data.

for z in tqdm(range(0,len(symbols))):
    stock=symbols[z]
    browser = webdriver.Firefox(executable_path = 'geckodriver',options=options) # Path of geckodriver file

    url='https://www1.nseindia.com/live_market/dynaContent/live_watch/get_quote/getHistoricalData.jsp?symbol={}&series=EQ&fromDate=undefined&toDate=undefined&datePeriod=1month'.format(stock)
    browser.get(url)
    html_source=browser.page_source
    browser.quit()
    soup = BeautifulSoup(html_source, 'html.parser')
    table = soup.find("table")
    
    # The first tr contains the field names.
    try:
        headings = [th.get_text().strip() for th in table.find("tr").find_all("th")]
    except:
        continue

    table_values_list=[]

    for row in table.find_all("tr")[1:]:
        dataset = dict(zip(headings, (td.get_text() for td in row.find_all("td"))))
        table_values=[]
        for values in dataset.values():
            table_values.append(str(values).strip().replace(",",""))

        table_values_list.append(table_values)

    stock_data = pd.DataFrame(table_values_list,columns=["Date","Symbol","Series","Open Price","High Price","Low Price","Last Traded Price","Close Price","Total Traded Quantity","Turnover (in Lakhs)"])
    stock_data = stock_data[["Date","Symbol","Open Price","High Price","Low Price","Close Price","Total Traded Quantity"]]
    Output_path = "" # Enter here the path where you will want to save the stock data 
    stock_data.to_csv("{}/{}_one_month.csv".format(Output_path,stock))
    time.sleep(1)
