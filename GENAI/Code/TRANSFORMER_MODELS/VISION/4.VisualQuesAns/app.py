import gradio as gr
from model import BLIPVQAModel

model = BLIPVQAModel()

def answer_question(image, question):
    return model.predict(image, question)

gr.Interface(
    fn=answer_question,
    inputs=[gr.Image(type="pil"), gr.Textbox(lines=1, placeholder="Ask a question...")],
    outputs="text",
    title="BLIP Visual Question Answering",
    description="Upload an image and ask a question about it."
).launch()
