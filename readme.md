# Agentic AI Demo Repo

Sample agentic workflow that leverages AzureOpenAI for the LLMs.

# Primary Scripts


## main.py
Serves as the primary calling script/insertion point. Receives basic user prompt and triggers necessary functions/agents.

## tools_agent.py
Agent that is provided a list of available tools, descriptions, and the user's prompt with the goal of selecting which tools may be applicable to solving the prompt.

## exec_agent.py
Agent that is provided with the user's original prompt, the applicable tools, and the source code/function for selected tools. The agent then generates the applicable arguments for each tool, then executes the tool calls.

## summary_agent.py
Retrieves results of the tool executions and pieces together the prompt chain/history to provide a summary of the prompt results. 

# Helper Scripts

## config.py
AzureOpenAI configuration and environment details to make necessary calls. i.e. temperature, API key, etc.

## tools
The functions/tool integrations that are made available to the model, including source code details for any custom functions.
