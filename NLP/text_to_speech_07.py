from gtts import gTTS
import os
speect_txt = " Naan tha ramu meena"
rec_text=gTTS(text=speect_txt,lang='ta',slow=True)
rec_text.save('rec_text.mp3')
os.system("start rec_text.mp3")
