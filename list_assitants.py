from config.oai import client

def list_assistants():
    my_assistants = client.beta.assistants.list(
        order="desc",
        limit="20",
    )

    # Check if there are assistants to display
    if not my_assistants.data:
        print("No assistants found.")
        return

    # Print the assistants with an index
    for index, assistant in enumerate(my_assistants.data, start=1):
        print(f"{index}: {assistant.id}")

    return my_assistants.data

if __name__ == "__main__":
    list_assistants()