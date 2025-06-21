import scraper
import data_manager
import emailer

URL = "https://programmer100.pythonanywhere.com/tours"

if __name__== "__main__":
    while True:
        extracted = scraper.extraction(URL)
        if(extracted != "No upcoming tours"):
            extracted_tuple = data_manager.format_date(extracted)
            previous_data = data_manager.load_previous_extracted(extracted_tuple)
            if(not previous_data):
                emailer.send_email(extracted)
                data_manager.store_extracted(extracted_tuple)
                break
            else:
                print("no email")