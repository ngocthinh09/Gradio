from ui.app_ui import create_ui

if __name__ == "__main__":
    demo = create_ui()
    demo.launch(
        theme="soft",
        share=True,
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
        debug=True
    )