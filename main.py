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

def store_extracted(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted+"\n")

def load_previous_extracted():
    with open("data.txt", "r") as file:
        content = file.read()
        return content

def send_email(extracted):
    print("email sent")
    print(extracted)

if __name__== "__main__":
    previous_data = load_previous_extracted()
    while True:
        scraped_source = scrape(URL)
        extracted = extraction(scraped_source)
        if(extracted != "No upcoming tours" and extracted not in previous_data):
            store_extracted(extracted)
            send_email(extracted)
            break
        else:
            print("no email")