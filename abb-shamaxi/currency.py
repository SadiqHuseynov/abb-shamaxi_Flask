import requests
import xml.etree.ElementTree as ET

url = "https://www.cbar.az/currencies/17.10.2023.xml"
response = requests.get(url)

usd_value = None
eur_value = None
rub_value = None

if response.status_code == 200:
    xml_data = response.text
    root = ET.fromstring(xml_data)

    valutes = root.findall(".//Valute")
    
    for valute in valutes:
        code = valute.get("Code")
        value = valute.find("Value").text
        
        if code == 'USD':
            usd_value = float(value)
        elif code == 'EUR':
            eur_value = float(value)
        elif code == 'RUB':
            rub_value = float(value)

