
import whisper
from langchain_openai import OpenAI
from testt import *
from testingf import *
import os
from dotenv import load_dotenv
load_dotenv()
Open_AI_Key = os.environ["OPENAI_API_KEY"] 



def email_summary(file,emaill):
    model = whisper.load_model("base")
    result = model.transcribe(file,fp16=False)
    textt = result["text"]
    print(textt)
    sending_email(textt,emaill,file)
    
    


