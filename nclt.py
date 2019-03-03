import requests 
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

##https://nclt.gov.in/pdf-cause-list?field_bench_target_id=5366&field_bench_court_target_id_entityreference_filter=5386

html_content = requests.get('https://nclt.gov.in/exposed-pdf-cause-list-page', verify= False).content

soup = BeautifulSoup(html_content, 'html.parser') 

soup = soup.find('select', {"name":"field_bench_target_id"})

for record in soup.find_all('option'):
    if not 'Any' in str(record):
        banch_name = record.text.strip()
        banch_value = record.get('value')

        payload = {'format': 'html',
                   'nid': banch_value, 
                   'type':'court_list'}
        html_page = requests.post('https://nclt.gov.in/custom-ajax.php', data=payload, verify=False).content

        soup = BeautifulSoup(html_page, 'html.parser')
        print('Branch Started => %s |  %s'%(banch_name, banch_value))
        print('')
        for sub_cat in soup.find_all('option'):
            court_name = sub_cat.text
            if not 'Any' in court_name:
                court_value = sub_cat.get('value')
                print('court  => %s |  %s'%(court_name, court_value))
                url = 'https://nclt.gov.in/pdf-cause-list?field_bench_target_id=%s&field_bench_court_target_id_entityreference_filter=%s'%(banch_value,court_value)
                print(url)
                print('')

        print('**'*20)
        print('')

