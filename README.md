# Object-Detection-with-Yolo3-model-and-impacts-of-imbalance-and-few-shot-on-model-s-performance



## 1. Introduction:
This project focus on understading deeply about the ideas and implementation of object detection model (YOLO3) that include:
- Dealing with different data type format (for object detection)
- Model architecture
- Model performance metric
- Loss function
- Training and tuning model
- Evaluation model
- Detailed implementation

I also researched the impacts of class imbalance and few-shot learning (training model with limited samples) on model performance. This project is my master post-graduate thesis at University of Glasgow. Since the data is from University Lab which is not allowed to download and publicize, I will only show the result I got during the research.

## 2. Software requirement:
You need packages likes Keras, Tensorflow2.0, Numpy, Pandas, Matplotlib, Pillow, OpenCV in order to execute the code (training model and Evaluation model)
## 3. Data:
The data used in this project is "Camera-trap" dataset, images in the dataset are high resolution with many objects in each image, the objects are at different sizes, many of them are small. Because of this, working with the dataset is much more challenging than normal dataset like COCO datasset or ImageNet and the model often has lower performance. Unfortunately, the dataset is from the University Lab and it was not allowed to download and publicize. 
