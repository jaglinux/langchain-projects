import sys
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from ollama_main import list_models

def chat(model_name, chat_input="hi"):
    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = ChatPromptTemplate.from_template(template)
    model = OllamaLLM(model=model_name)
    chain = prompt | model

    out = chain.invoke({"question": chat_input})
    print(out)

if __name__ == '__main__':
    models = list_models()
    print(models)
    if len(models):
        for i,j in enumerate(models):
            print(f"Press {i} to run {j}")
        model_choice = int(input())
        if model_choice >= 0 and model_choice < len(models):
            while True:
                print("Enter your question")
                print("To exit, type bye")
                chat_input = input()
                if chat_input == "bye":
                    print("bye...EXITing")
                    sys.exit(0)
                chat(models[model_choice], chat_input)
        else:
            print("wrong choice entered...EXITing")
    else:
        print("no local models running...EXITing")
