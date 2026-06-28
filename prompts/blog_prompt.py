from langchain_core.prompts import PromptTemplate

template = """
    Write a blog for {blog_style} for a topic {input_text}
    within {no_words} words.
    """
blog_prompt = PromptTemplate.from_template(template=template)


