import scraper
import data_manager

URL = "https://programmer100.pythonanywhere.com/tours"

def send_email(extracted):
    print("email sent")
    print(extracted)

if __name__== "__main__":
    previous_data = data_manager.load_previous_extracted()
    while True:
        extracted = scraper.extraction(URL)
        if(extracted != "No upcoming tours" and extracted not in previous_data):
            data_manager.store_extracted(extracted)
            send_email(extracted)
            break
        else:
            print("no email")