from bs4 import BeautifulSoup
import requests

URL = "https://kurs.kz/index.php?mode=astana"
request = requests.get(URL)

soup = BeautifulSoup(request, 'html.parser')
parsed_text = soup.find_all('span')
print(parsed_text) 
# <th class="text-center currency hidden-xs"><span>5.89</span><span>5.98</span></th>