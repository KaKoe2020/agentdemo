import os 
import subprocess

def get_website_response_time(command):
    """Return a website ping response time."""
    cmd = command
    
    response = subprocess.run(command, capture_output=True, text=True, shell=True)
    
    return response

def purchase_item(item_id: str, quantity: int) -> str:
    """Simulate purchasing an item."""
    # Replace this with your actual purchasing logic.
    return f"Purchased {quantity} of item {item_id}"

# Function registry: maps function names to their implementations.
tools_registry = {
    get_website_response_time: "Used to help users get the response time of a website",
    purchase_item: "Helps users purchase something.",
}