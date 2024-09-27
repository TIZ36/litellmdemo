import subprocess
from gloabl import *
from rich.console import Console
from litellm import completion
from rich.live import Live
from rich.markdown import Markdown
from embedding.ollama_embedding import OllamaEmbedding

query=''
console=Console()


ollama_embedding = OllamaEmbedding()
resp = ollama_embedding.embed("hello world")
print(resp)


# print("mem_id: ", mem_id)
while query != "exit":
    query = input(">>> please input your query: ")
    if query == "exit":
        break

    if query == "":
        continue

    if query == "clear":
        subprocess.run("clear")
        continue

    with Live(console=console, refresh_per_second=120) as live:
        markdown_contents = f"> Query: {query} \n\n"
        try:
            response = completion(
            model=ollama_chat_model,
            messages=[{"content": query, "role": "user"}],
            api_base=f"{ollama_api_base}",
                stream=True,
            )


            for item in response:  # Add a valid loop variable name after 'for'
                # Add your code here
                # print inline

                # print(item)
                v = item['choices'][0]['delta']['content'] 
                if v != None:
                    markdown_contents += f"{v}"
                    live.update(Markdown(markdown_contents))

        except Exception as e:
            print("Error: ", e)
            break

    print("\n")


