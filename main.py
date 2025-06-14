import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/tours"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extraction(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(extracted):
    print("email sent")
    print(extracted)

if __name__== "__main__":
    while True:
        scraped_source = scrape(URL)
        extracted = extraction(scraped_source)
        if(extracted != "No upcoming tours"):
            send_email(extracted)
            break
        else:
            print("no email")