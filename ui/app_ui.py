import gradio as gr
from core.model_handler import YOLOv8
from utils.image_utils import load_image_from_url

def create_ui():
    model_handler = YOLOv8()
    
    def process_detection(image, confidence):
        if image is None:
            return None, "Please upload image before"
        return model_handler.detect(image, confidence)
    
    def clear_all():
        return None, None, ""
    
    with gr.Blocks(title="Object Detection Simple") as demo:
        gr.Markdown("# Object Detection with YOLO")
        gr.Markdown("Please upload image to detect objects")
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("## Input")
                input_image = gr.Image(label="Upload image", type="pil", height=300)
                
                confidence_slider = gr.Slider(
                    minimum=0.1, maximum=1.0, value=0.5, step=0.01,
                    label="Confidence Threshold",
                    info="Adjust confidence threshold of detection"
                )
                
                url_input = gr.Textbox(
                    label="Image URL",
                    placeholder="Enter image URL and press 'Load Image From URL'",
                    interactive=True
                )

                with gr.Row():
                    detect_btn = gr.Button("Detect Objects", variant="primary", size="lg")
                    load_image_btn = gr.Button("Load Image From URL", variant="secondary")
                    clear_btn = gr.Button("Clear", variant="secondary")
                    
            with gr.Column(scale=1):
                gr.Markdown("## Output")
                output_image = gr.Image(label="Detection Result", height=300)
                detection_info = gr.Textbox(
                    label="Detection Info", lines=8, max_lines=10, interactive=False
                )
        
        detect_btn.click(
            process_detection,
            inputs=[input_image, confidence_slider],
            outputs=[output_image, detection_info]            
        )
        
        load_image_btn.click(
            load_image_from_url,
            inputs=[url_input],
            outputs=[input_image]
        )
        
        clear_btn.click(
            clear_all,
            outputs=[input_image, output_image, detection_info]
        )
        
        input_image.change(
            process_detection,
            inputs=[input_image, confidence_slider],
            outputs=[output_image, detection_info]
        )
    
    return demo
