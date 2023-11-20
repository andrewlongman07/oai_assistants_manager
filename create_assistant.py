from config.oai import client
from list_models import list_models

def create_assistant():

    # metadata
    name = input('What would you like to call the assistant? ')
    instructions = input('Please add any system instructions for the assistant:')


    # tools
    tool_options = {
        1: {'type': 'code_interpreter'},
        2: {'type': 'tool_type_2'},  # Replace with actual tool type
        3: {'type': 'tool_type_3'}   # Replace with actual tool type
    }
    
    print("Select tools to add to the assistant (enter the numbers, comma-separated):")
    for option_number, tool in tool_options.items():
        print(f"{option_number}: {tool['type']}")

    selected_tools = []
    try:
        user_input = input("Enter your choices: ")
        selected_indices = [int(index.strip()) for index in user_input.split(',')]
        
        for index in selected_indices:
            if index in tool_options:
                selected_tools.append(tool_options[index])
            else:
                print(f"No tool found for selection {index}. Skipping.")

    except ValueError:
        print("Invalid input. Please enter numbers, comma-separated.")
        return []
    
    # model

    try:
        models = list_models()
        model_choice = int(input('Which model should power the assistant?'))
        chosen_model = models[model_choice - 1]
        print(f"chosen model: {chosen_model.id}")
    except ValueError: 
        print("Invalid input. Please enter a number.")

    assistant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=selected_tools,
        model=chosen_model.id
    )

    return assistant

if __name__ == "__main__":
    create_assistant()