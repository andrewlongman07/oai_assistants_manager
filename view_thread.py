from config.oai import client

def show_thread_messages(): 
    thread_id = input('inut thread id: ')
    thread = client.beta.threads.messages.list(thread_id)
    # print(thread)
   # Iterate through the ThreadMessage objects in the data array
    for thread_message in thread.data:
        # Each thread_message.content is a list of MessageContentText objects
        for message_content in thread_message.content:
            # Access the text value of each MessageContentText
            print(message_content.text.value)
            print("\n")
    return thread

if __name__ == "__main__": 
    show_thread_messages()