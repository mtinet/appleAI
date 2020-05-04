from imageai.Detection.Custom import CustomObjectDetection
import os

execution_path = os.getcwd()

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(detection_model_path="detection_model-ex-028--loss-8.723.h5")
detector.setJsonPath(configuration_json="apple_dataset/json/detection_config.json")
detector.loadModel()

detections = detector.detectObjectsFromImage(input_image="image.jpg", minimum_percentage_probability=60, output_image_path="image-new.jpg")

for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
