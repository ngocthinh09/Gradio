# Gradio Demo: Object Detect with YOLO

This is a lightweight web application that performs object detection using the YOLOv8 nano model. It provides an interactive user interface allowing users to upload images and adjust confidence thresholds easily.

## 📁 Directory Structure

```text
yolo_gradio_app/
├── core/
│   └── model_handler.py     # YOLO model initialization and prediction logic
├── utils/
│   └── image_utils.py       # Helper functions (e.g., loading sample images)
├── ui/
│   └── app_ui.py            # Gradio web interface layout and event handlers
├── app.py                   # Main entry point to launch the application
└── requirements.txt         # Python dependencies
```

## 🚀 How to Run

1. **Install the required dependencies:**

    Make sure you have Python installed. Open your terminal and run:
    ```bash
    pip install -r requirements.txt
    ```

2. **Launch the application:**
    
    Execute the main script:
    ```bash
    python app.py
    ```

3. **View the app:**

    Open your web browser and navigate to the local URL provided in the terminal (typically http://127.0.0.1:7860).

## 💡 About Gradio
[Gradio](https://www.gradio.app/docs) is an open-source Python library designed to quickly build interactive web interfaces for machine learning models. It eliminates the complexity of building a full stack application; Gradio automatically generates both the front-end UI and the back-end server. This means you don't need any experience with HTML, CSS, or JavaScript — you just provide the Python function containing your model's "brain", and Gradio handles the rest