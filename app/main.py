import sys
from litellm import completion

api_base="http://10.3.30.81:11434"

query=''
while query != "exit":
    query = input(">>> pleae input your query: ")
    if query == "exit":
        break

    response = completion(
        model="ollama/llama3:8b",
        messages=[{"content": query, "role": "user"}],
        api_base=f"{api_base}",
        stream=True,
    )

    for item in response:  # Add a valid loop variable name after 'for'
        # Add your code here
        # print inline

        print(item['choices'][0]['delta']['content'], end='')

    print("\n")