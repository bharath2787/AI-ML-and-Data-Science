from langchain_core.prompts import PromptTemplate

# 1. Define the prompt template
template = PromptTemplate(
    template="Write a short story about a {animal} who learns to {skill}.",
    input_variables=["animal", "skill"],  # These must match the placeholders
    validate_template=True  # Optional but recommended
)
# 2. Fill in the variables using .invoke()
filled_prompt = template.invoke({
    "animal": "cat",
    "skill": "cook"
})
# 3. Print or use the generated prompt string
print(filled_prompt)
