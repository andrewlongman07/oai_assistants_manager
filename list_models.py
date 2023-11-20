from config.oai import client

def list_models() : 
    models = client.models.list()
    for index, model in enumerate(models, start=1): 
        print(f"{index}: {model.id}")
    # print(models)
    return models.data


if __name__ == "__main__": 
    list_models()