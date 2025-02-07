import ollama

def list_models():
    models = ollama.list()
    models = models['models']
    response_model_name = []
    for model in models:
        response_model_name.append(model.model)
        print(f"model is {model.model}")
        print(f"model details {model.details}")
        print("------------------")
    return response_model_name

def list_running_models():
    models_running = ollama.ps()
    print(models_running)
 
if __name__ == "__main__":
    print("Enter ollama main")
    list_models()
    list_running_models()
    
