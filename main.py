import pyttsx3
import fitz #pymupdf

SPEED_RATE = 200
PDF_NAME = 'love.pdf'

with fitz.open(PDF_NAME) as book:
    full_text = ""

    audio_reader = pyttsx3.init()
    audio_reader.setProperty("rate", SPEED_RATE)

    for page in book:
        content = page.getText()
        full_text += content

    print(full_text)
    audio_reader.save_to_file(full_text, "audiobook.mp3")
    audio_reader.runAndWait()
