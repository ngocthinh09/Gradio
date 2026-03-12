import cv2
import numpy as np
from PIL import Image
import torch
from ultralytics import YOLO

class YOLOv8:
    def __init__(self, model_path='yolov8n.pt'):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        try:
            self.model = YOLO(model_path)
            print(f"YOLO model loaded successfully on {self.device}.")
        except Exception as e:
            print(f"Error loading YOLO model: {e}")
            self.model = None
            
    def detect(self, image, confidence_threshold=0.25):
        if self.model is None:
            return image, "Model not loaded. You need to 'pip install ultralytics' and ensure the model file is in the correct path."
        
        try:
            if (isinstance(image, Image.Image)):
                image_np = np.array(image)
            else:
                image_np = image
            
            if len(image_np.shape) == 2 and image_np.shape[2] == 3:
                image_rgb = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
            else:
                image_rgb = image_np
                
            result = self.model(image_rgb, conf=confidence_threshold)
            annotated_iamge = result[0].plot()
            
            detections = result[0].boxes
            detection_info = []
            
            if detections is not None:
                for i, box in enumerate(detections):
                    class_id = int(box.cls[0])
                    confidence = float(box.conf[0])
                    class_name = self.model.names[class_id]
                    detection_info.append(f"{class_name}: {confidence:.2f}")
                    
            if detection_info:
                info_text = f"Found {len(detection_info)} objects:\n- " + "\n- ".join(detection_info)
            else:
                info_text = "Not found any objects with this confidence threshold."
                
            return annotated_iamge, info_text
        except Exception as e:
            print(f"Error during detection: {e}")
            return image, "Error during detection. Please check the console for details."
            