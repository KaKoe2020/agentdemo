from tools_agent import tool_agent_loop
from exec_agent import exec_agent_loop
from summary_agent import summary_agent_loop
import tools
import inspect


if __name__ == "__main__":
    # user prompt
    user_input = input("Prompt: ")
        
    # determine which tools are available for the task
    tool_result = tool_agent_loop(user_input)
    
    # determine command/execution syntax
    tool_result_list = []
    
    for i in tool_result.keys():
        tool = getattr(tools, i)
        source_code = inspect.getsource(tool)
        exec_command = exec_agent_loop(user_input, source_code)
        # execute tools
        output = tool(exec_command)
        tool_result_list.append({"tool": i, "output": output})
    
    # summarize findings and format
    
    summary = summary_agent_loop(user_input, tool_result_list)
    print(summary)
    
    