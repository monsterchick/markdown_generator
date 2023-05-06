import os
import openai
from dotenv import load_dotenv
from read_data import ReadData
from Prompt import Prompt

# Title of Table
title = ReadData().get_data()[0]

# Data to insertread_config().get_data()[0]
data = ReadData().get_data()[1]

# instruction sent to gtp
prompt = Prompt().get_prompt().replace("{title}",title).replace("{data}",data)

# load .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user","content":prompt}])

print(completion.choices[0].message.content)