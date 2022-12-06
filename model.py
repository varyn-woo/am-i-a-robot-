import torch
import image_data

class Detector:
    
    def __init__(self):
        self.data = {}
        self.model = torch.hub.load('ultralytics/yolov3', 'yolov3')

    def classify(self, img, img_name = None):
        # Inference
        results = self.model(img)
        if img_name is None:
            img_name = img

        # Results
        df = results.pandas().xyxy[0]
        objects = df.name.value_counts().to_dict()
        bounds = {}
        for _, row in df.iterrows():
            bound = {'xmin': row['xmin'],
                    'xmax': row['xmax'],
                    'ymin': row['ymin'],
                    'ymax': row['ymax']}
            if row['name'] not in bounds:
                bounds[row['name']] = [bound]
            else:
                bounds[row['name']].append(bound)
        
        img_data = image_data.ImageData(img_name, bounds, objects)
        self.data[img_name] = img_data
        return img_data