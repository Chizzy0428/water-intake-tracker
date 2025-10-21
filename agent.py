import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# Retrieve API key securely from Streamlit secrets
OPENAI_API_KEY = st.secrets["openai"]["api_key"]

# Initialize the LLM
llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.5)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self,intake_ml):

        prompt = f"you are a hydration assistant. the user has consumed {intake_ml}ml of water today provide hydration status and suggest if they need to drink more water."

        response = llm.invoke([HumanMessage(content=prompt)])

        return response.content




