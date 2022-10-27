import gradio as gr
import numpy as np

def flip(im):
    #This is the output
    return None

with gr.Blocks(css="#warning {color: red}") as demo:
        box1 = gr.Textbox(value="Good Job")
        box2 = gr.Textbox(value="Failure", elem_id="warning")
        gr.Interface(
            flip, 
            gr.Image(source="webcam", streaming=True), 
            "image",
            live=True
        )
 
if __name__ == "__main__":
    demo.launch()