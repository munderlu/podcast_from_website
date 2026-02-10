from tts import *
from telegram import *

FILE_NAME = "test2.txt"
OUTPUT_NAME = "test.mp3"

#asyncio.run(generate_and_merge(return_file(FILE_NAME), OUTPUT_NAME))

#send_file(OUTPUT_NAME)

send_text("Ich kann automatisch text verschicken.")