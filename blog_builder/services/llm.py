from langchain_deepseek import ChatDeepSeek
from prompts.blog_prompt import blog_prompt

llm =  ChatDeepSeek(
    model = "deepseek-v4-pro",
    temperature = 0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)


# Respuesta por batch
#response = model.invoke(messages)
#print(response.content)

#for chunk in model.stream(messages):
#    print(chunk.content, end="", flush=True)

def generate_blog(input_text, no_words, blog_style):
    prompt = blog_prompt.format(
        blog_style=blog_style,
        input_text=input_text,
        no_words=no_words
    )
    #print('>> Stream iniciado')
    for chunk in llm.stream(prompt):
        #print(f">>> chunk: {repr(chunk.content)}")
        if chunk.content:
            yield chunk.content
    #print(">>> Stream terminado")
