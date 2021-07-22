import random
import time
from datetime import datetime

while True:

    # Choosing a sentence from the sentences array.
    sentences = [
        "He walked into the airport past the banks of monitors",
        "Inside the front door about thirty nametags were laid out on a table",
        "She says those bald patches make it look shanty Irish"
        ]
    sentence = str(random.choice(sentences))
    sentenceArray = sentence.split()
    words = len(sentenceArray)

    print("\nType the following:\n\n" + sentence + "\n\n")

    # Countdown
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Go!")

    # Input from user and declaring start time
    startTime = datetime.utcnow()
    userInput = input("\n\nStart typing here: ")

    if userInput != sentence:
        print("Your input did not match the sentence!")
    else:
        # Calculating response time
        response_time = datetime.utcnow() - startTime
        hours, remainder = divmod(float(response_time.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)

        timeTaken = round(seconds, 1)
        minute = seconds / 60
        wpm = round(words / minute)

        # Outputting the results
        print(f"Done! Took {timeTaken}s. Your WPM is {wpm}")
