import json

def extract_json(response_text: str):
    """
    Attempt to extract JSON from the response text.
    
    Returns:
        The parsed JSON object if successful; None otherwise.
    """
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return None