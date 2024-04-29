import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

YOUTUBE_VIDEO = "https://www.youtube.com/watch?v=BrsocJb-fAo"

from langchain_openai.chat_models import ChatOpenAI
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

response = model.invoke("What do you think about Capitalism")

print(response.content)