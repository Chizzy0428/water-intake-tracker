import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=OPENAI_API_KEY,model="gpt-4", temperature=0.5)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self,intake_ml):

        prompt = f"you are a hydration assistant. the user has consumed {intake_ml}ml of water today provide hydration status and suggest if they need to drink more water."

        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content




