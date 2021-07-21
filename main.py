import random
import time
from datetime import datetime

while True:
    # Choosing a sentence from the sentences array.
    sentences = [
        "He walked into the airport, past the banks of monitors.",
        "Inside the front door about thirty nametags were laid out on a table.",
        "She says those bald patches make it look shanty Irish."
        ]
    sentence = str(random.choice(sentences))

    print("\nType the following:\n\n" + sentence + "\n\n")

    # Countdown
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Go!")

    if sentence == "He walked into the airport, past the banks of monitors.":
        numOfWords = 10
    elif sentence == "Inside the front door about thirty nametags were laid out on a table.":
        numOfWords = 13
    else:
        numOfWords = 10

    # Input from user and declaring start time
    startTime = datetime.utcnow()
    userInput = input("\n\nStart typing here: ")

    if userInput != sentence:
        print("Your input did not match the sentence!")
        break
    else:
        # Calculating response time
        response_time = datetime.utcnow() - startTime
        hours, remainder = divmod(float(response_time.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)

        timeTaken = round(seconds, 1)

        # Outputting the results
        print(f"Done! Took {timeTaken}s.")