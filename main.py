import schedule
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

website = 'https://www.coingecko.com/'   #website url

response = requests.get(website)  #get request

#print(response.status_code)  #return 200 if works fine.

soup = BeautifulSoup(response.content, 'html.parser')

#print(soup)  #return the entire html code 

information = soup.find('table', {'class':'table-scrollable'}).find('tbody').find_all('tr')


#Empty lists
name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []


#testing if show the correct information

#print(information[0].find('td',{'class':'td-market_cap'}).get_text().strip())   #market cap
#print(information[0].find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()) #name
#print(information[0].find('td', {'class':'td-price price text-right pl-0'}).get_text().strip())  #price
#print(information[0].find('td', {'class':'td-change1h'}).get_text().strip())  #change 1h 
#print(information[0].find('td', {'class':'td-change24h'}).get_text().strip())  #change 24h 
#print(information[0].find('td', {'class':'td-change7d'}).get_text().strip())  #change 7 days 
#print(information[0].find('td', {'class':'td-liquidity_score'}).get_text().strip())  #24h volume 


def main():
	for x in information:
		#name
		try:
			name.append(x.find('a',{'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
		except:
			name.append('n/a')  #if we have missing data, just append 'n/a' to our list

		#price
		try:
			price.append(x.find('td', {'class':'td-price price text-right pl-0'}).get_text().strip())
		except:
			price.append('n/a')  #if we have missing data, just append 'n/a' to our list

		#change 1h
		try:
			change_1h.append(x.find('td', {'class':'td-change1h'}).get_text().strip())
		except:
			change_1h.append('n/a')  #if we have missing data, just append 'n/a' to our list

		#change 24h
		try:
			change_24h.append(x.find('td', {'class':'td-change24h'}).get_text().strip())
		except:
			change_24h.append('n/a')  #if we have missing data, just append 'n/a' to our list

		#change 7days
		try:
			change_7d.append(x.find('td', {'class':'td-change7d'}).get_text().strip())
		except:
			change_7d.append('n/a')  #if we have missing data, just append 'n/a' to our list

		#24h volume
		try:
			volume_24h.append(x.find('td', {'class':'td-liquidity_score'}).get_text().strip())
		except:
			volume_24h.append('n/a')  #if we have missing data, just append 'n/a' to our list

		#market cap
		try:
			market_cap.append(x.find('td',{'class':'td-market_cap'}).get_text().strip())
		except:
			market_cap.append('n/a')  #if we have missing data, just append 'n/a' to our list


	#create data frame with pandas

	crypto_data_df = pd.DataFrame({'Coin': name, 'Price':price, 'Change 1h':change_1h, 'Change 24h':change_24h, 
									'Change 7d':change_7d, 'Volume 24h':volume_24h, 'Market Cap': market_cap})

	#export to excel
	crypto_data_df.to_excel('crypto_data.xlsx', index=False)
	print("Successfully...") 





schedule.every(10).seconds.do(main)  #10 seconds
#schedule.every(2).hour.do(main)  #every 2 hours run the main function
#schedule.every(20).minutes.do(main) #every 20 minutes run the main function

while 1:
	schedule.run_pending()
	time.sleep(1)



