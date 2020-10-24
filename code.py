import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
 
n = ToastNotifier()
def getdata(url):
	r = requests.get(url)
	return r.text

htmldata = getdata("https://weather.com/en-IN/weather/today/l/476c2eca987c2a2b6621816c276d5f260a902e812e821b15c982ba54e7766b37")
soup = BeautifulSoup(htmldata, 'html.parser')
    

actual_temp = soup.select("#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section > div > div._-_-node_modules-\@wxu-components-src-organism-CurrentConditions-CurrentConditions--dataWrapperInner--2h2vG > div._-_-node_modules-\@wxu-components-src-organism-CurrentConditions-CurrentConditions--primary--3xWnK > span")
chances_rain = soup.select('#WxuCurrentConditions-main-b3094163-ef75-4558-8d9a-e35e6b9b1034 > div > section')
aqi_elem = soup.select("#WxuAirQuality-sidebar-aa4a4fb6-4a9b-43be-9004-b14790f57d73 > section > div > div:nth-child(1) > svg > text")
temp_felt = soup.select("#WxuTodayDetails-main-fd88de85-7aa1-455f-832a-eacb037c140a > section > div._-_-node_modules-\@wxu-components-src-organism-TodayDetailsCard-TodayDetailsCard--hero--HySn3 > div._-_-node_modules-\@wxu-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTemp--2GFqN > span._-_-node_modules-\@wxu-components-src-organism-TodayDetailsCard-TodayDetailsCard--feelsLikeTempValue--2aogo")
air_quality = soup.select("#WxuAirQuality-sidebar-aa4a4fb6-4a9b-43be-9004-b14790f57d73 > section > div > div:nth-child(2) > div > div > span")
humidity = soup.select("#todayDetails > section > div.TodayDetailsCard--detailsContainer--1tqay > div:nth-child(3) > div.WeatherDetailsListItem--wxData--23DP5 > span")
temp = actual_temp[0]
temp_rain = chances_rain[0]
aqi = aqi_elem[0]
temp_felt = temp_felt[0]
air_quality = air_quality[0]
humidity = humidity[0]

result = "Khopoli Maharashtra"+"\ncurrent_temp : " + temp.text  + "\n" + "Humidity : " + humidity + "\n" + temp_rain.text[65:] + "\n"+"Air Quality Index : " + aqi.text +" ("+air_quality.text+")"
n.show_toast("Live Weather Update", result)


