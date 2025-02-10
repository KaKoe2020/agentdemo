import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from tools import tools_registry
from utils import extract_json
from config import MODEL_CONFIG
import json


def tool_agent_loop(user_input):
    load_dotenv()

    # Establish client connection
    model_name = os.getenv("OPENAI_MODEL_NAME")
    client = AzureOpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),  
    api_version = os.getenv("OPENAI_API_VERSION"),
    azure_endpoint = os.getenv("OPENAI_ENDPOINT")
    )

    def tool_selection_call(*args):
        """
        Uses the Azure OpenAI Chat API to generate a reply based on the conversation history.
        The engine parameter should match your Azure deployment name.
        """
        
        system_prompt = f"""
                            You are an agentic AI assistant. 
                            Your purpose is to evaluate the potential tools at your disposal and determine which, if any, might be useful to the user's prompt.
                            The tools shown to you are in JSON format, with the following structure:
                            
                            "tool name": "tool description"    
                            
                            You can access the following tools: {tools_registry}
                            
                            Important Instructions: Be sure that you only respond with the names of the tools and their description that you feel are useful, in a Python dictionary format.
                            
                        """
                    
        chat_prompt = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
            
            ]

        
        response = client.chat.completions.create(
            model=model_name, 
            messages= chat_prompt
            )
        
        return response.choices[0].message.content

    result = tool_selection_call(user_input, tools_registry)
    result = json.loads(result)
    
    return result
