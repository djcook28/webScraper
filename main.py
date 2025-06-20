import scraper
import data_manager
import emailer

URL = "https://programmer100.pythonanywhere.com/tours"

if __name__== "__main__":
    previous_data = data_manager.load_previous_extracted()
    while True:
        extracted = scraper.extraction(URL)
        extracted_tuple = tuple(extracted.split(", "))
        if(extracted != "No upcoming tours" and extracted_tuple not in previous_data):
            emailer.send_email(extracted)
            data_manager.store_extracted(extracted_tuple)
            break
        else:
            print("no email")