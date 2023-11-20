from config.oai import client
from list_assitants import list_assistants

def delete_assistant() :
    assistants = list_assistants()
    # Ask the user which assistant to delete
    try:
        selected_index = int(input("Enter the index of the assistant to delete: "))
        if 1 <= selected_index <= len(assistants):
            # Logic to delete the selected assistant
            assistant_to_delete = assistants[selected_index - 1]            
            print(f"Assistant {assistant_to_delete.name} selected for deletion.")
            response = client.beta.assistants.delete(assistant_to_delete.id)
            print(response)
        else:
            print("Invalid selection. Please enter a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    
if __name__ == "__main__":
    delete_assistant()