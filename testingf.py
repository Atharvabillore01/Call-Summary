from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import whisper
import os
Open_AI_Key = os.environ["OPENAI_API_KEY"] 
from dotenv import load_dotenv
load_dotenv()
def summsumm(file):
  print("working")
  model = whisper.load_model("base")
  result = model.transcribe(file,fp16=False)
  textt = result["text"]
  prompt = ChatPromptTemplate.from_template("summarize the text  {topic}")
  model = ChatOpenAI(model="gpt-4")
  output_parser = StrOutputParser()

  chain = prompt | model | output_parser
  print(chain.invoke({"topic": textt}))
  