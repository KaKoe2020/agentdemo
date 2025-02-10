import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from tools import tools_registry
from utils import extract_json
from config import MODEL_CONFIG
import json


def summary_agent_loop(user_input, tool_result_list):
    load_dotenv()


    # Establish client connection
    model_name = os.getenv("OPENAI_MODEL_NAME")
    client = AzureOpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),  
    api_version = os.getenv("OPENAI_API_VERSION"),
    azure_endpoint = os.getenv("OPENAI_ENDPOINT")
    )

    def summary_call(*args):

        system_prompt = f"""
                            You are an agentic AI assistant.
                            Your purpose is to take the history chain and summarize it back to the user, based on their original prompt.
                            You also have the executed tools and their results as a python list of dictionaries to help summarize the results.
                            
                            The user's original prompt is: {user_input}.
                            
                            The executed tool results are: {tool_result_list}.
                                                      
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

    result = summary_call(user_input, tool_result_list)
    # result = json.loads(result)
    
    return result
