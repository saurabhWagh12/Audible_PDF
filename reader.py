import speech_recognition as SR
import pyttsx3
from PyPDF2 import PdfReader

listner = SR.Recognizer()
engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')

# Set the desired voice (change the index to select a different voice)
# Assuming index 1 corresponds to a female voice, you can adjust this based on your available voices.
engine.setProperty('voice', voices[1].id)

# Set the speech rate (words per minute)
engine.setProperty('rate', 150)  # Adjust the rate as needed

def talk(text):
    engine.say(text)
    engine.runAndWait()


pdf_file = 'Friends.pdf'

reader = PdfReader(pdf_file)

number_of_pages = len(reader.pages)
print("Number of pages", number_of_pages)
start_page = int(input("Enter the starting page number: "))
end_page = int(input("Enter the Ending page number or Enter -1 to read whole book from starting page specified: "))
if end_page==-1:
    end_page = number_of_pages
# print("Number of pages", number_of_pages)

if (start_page < 1 or start_page > number_of_pages )and end_page<= number_of_pages:
    print("Invalid starting page number.")
else:
    talk('Reading from page {} to page {}'.format(start_page, end_page))
    for page_number in range(start_page, end_page + 1):
        page = reader.pages[page_number - 1]
        text = page.extract_text()
        talk(text)
