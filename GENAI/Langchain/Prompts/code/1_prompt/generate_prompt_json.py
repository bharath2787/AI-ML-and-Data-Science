from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
You are an expert educator. Convert the blog titled "{blog_title}" into a beginner-friendly explanation.

Audience Level: {audience_level}  
Tone: {tone_input}  
Target Format: {output_format}

Guidelines:
1. Simplify jargon using everyday language or analogies.  
2. Where applicable, include code snippets or diagrams to explain concepts.  
3. Highlight real-world applications or use-cases.  
4. If certain parts of the blog are ambiguous or missing, clearly state: "Details not provided."

Ensure the explanation is accessible to someone new to the topic and matches the selected tone and format.
""",
    input_variables=["blog_title", "audience_level", "tone_input", "output_format"],
    validate_template=True
)

template.save("explain_blog_template.json")
