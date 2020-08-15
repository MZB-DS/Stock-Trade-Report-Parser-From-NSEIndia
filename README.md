# Stock-Trade-Report-Parser-From-NSEIndia
This repository contains the python code for pulling historical trade data for any and any number of stocks for the last one month directly from the website: 'nseindia.com'. The pulled data will contain day level ["Open Price","High Price","Low Price","Last Traded Price","Close Price","Total Traded Quantity","Turnover (in Lakhs)"].

## How to use this code
1. Include all the stock name of the stocks you want to pull the trade data in python's list: symbols.
2. Mention proper path of the ```geckodriver``` file.
3. Only certain columns are kept while importing to the csv file. You can choose the columns you want to include from the line 43 and mention those in line 44.
4. Provide proper directory where you want to save all the stock csv files.
5. Execute ```stock_trade_data_parser_from_nse.py```.

## Future Features
Adding feature to pull one week and 3 months historical data.

## Dependencies
- Python3 any version
- Selenium webdriver for your preferred browser. Install from here: https://www.selenium.dev/downloads/
- Python packages: selenium==3.141.0(For working with web browser), time, bs4(For html parsing), tqdm(For displaying progress bar), warnings

```pip3 install selenium==3.141.0 time bs4 tqdm warnings```
