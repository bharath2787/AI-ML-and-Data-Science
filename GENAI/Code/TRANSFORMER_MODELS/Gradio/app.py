import gradio as gr

def test(num1, num2):
    print("hello")
    return "test"

def add_numbers(num1, num2):
    return int(num1)+int(num2)

demo = gr.Interface(
    fn = add_numbers,
    inputs=[gr.Textbox(label="Number 1"), gr.Textbox(label="Number 2")],
    outputs=gr.Textbox(label="Sum"),
    title="Simple Addition Demo",
    description="Enter two numbers and see their sum."
)

demo.launch()


# When you click the flag button in a Gradio demo running locally, 
# by default, it downloads a CSV file containing the flagged input/output data along with any comments entered.

# This CSV is basically a simple log of the feedback users gave, 
# which you can review later to see what kind of issues or mistakes happened during use.