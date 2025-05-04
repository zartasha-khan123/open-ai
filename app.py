import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

#--------------------------------------agents ka setup---------------------------------------------#
load_dotenv()

set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise Exception("GEMINI_API_KEY is not set!")

#--------------------------------------agents ka instance---------------------------------------------#

agent = Agent(
    model=LitellmModel(model='gemini/gemini-2.0-flash',api_key=GEMINI_API_KEY),
    name='zartash agent',
    instructions='you are a helpful assistant',
)

#----------------------------agents ko chalaya-------------------------------------------
res = Runner.run_sync(agent,"what is the capital of Pakistan?")

print(res.final_output)

# #         res = Runner.run_sync(agent, user_input)