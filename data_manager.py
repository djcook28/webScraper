def load_previous_extracted():
    with open("data.txt", "r") as file:
        return file.read()

def store_extracted(extracted):
    with open("data.txt", "a") as file:
        file.write(extracted+"\n")