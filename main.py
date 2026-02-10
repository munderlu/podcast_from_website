from tts import *

asyncio.run(generate_and_merge(return_file("test.txt"), "wikipedia-eintrag.mp3"))