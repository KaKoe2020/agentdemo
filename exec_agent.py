import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from tools import tools_registry
from utils import extract_json
from config import MODEL_CONFIG
import json


def exec_agent_loop(user_input, source_code):
    load_dotenv()


    # Establish client connection
    model_name = os.getenv("OPENAI_MODEL_NAME")
    client = AzureOpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),  
    api_version = os.getenv("OPENAI_API_VERSION"),
    azure_endpoint = os.getenv("OPENAI_ENDPOINT")
    )

    def exec_execution_call(*args):

        system_prompt = f"""
                            You are an agentic AI assistant.
                            Your purpose is to evaluate the user's initial prompt, the python functions available to you, 
                            and determine a response that will execute the python function that is most useful to the user.
                            
                            The user's original prompt is: {user_input}
                            
                            The function's source code you need to provide input for is: {source_code}
                            
                            Important Instructions: Be sure that you only respond with the function's input argument, nothing else.                             
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

    result = exec_execution_call(user_input, source_code)
    # result = json.loads(result)
    
    return result
