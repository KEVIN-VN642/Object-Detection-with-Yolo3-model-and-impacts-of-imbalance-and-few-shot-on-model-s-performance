# Object-Detection-with-Yolo3-model-and-impacts-of-imbalance-and-few-shot-on-model-s-performance

Please take a look at files <b>presentation_slides.pptx</b> and <b>Software Descriptions.xlsx</b> for fully understand the results and project structure.

### Table of Contents
1. [Introduction](#intro)
2. [Software Riqurements](#software)
3. [Data](#data)
4. [How to understand codes](#code)
5. [Results and Findings](#results)

## 1. Introduction:<a id="intro"></a>
This project focus on understading deeply about the design ideas and implementation of object detection model (YOLO3) that include:
- Dealing with different data type format (for object detection)
- Data Generator
- Model architecture
- Model performance metric
- Loss function
- Training and tuning model
- Evaluation model
- Detailed implementation

I also researched the impacts of class imbalance and few-shot learning (training model with limited samples) on model performance. This project is my master post-graduate thesis at University of Glasgow. Since the data is from University Lab which is not allowed to download and publicize, I will only show the result I got during the research.

## 2. Software requirement:<a id="software"></a>
You need packages likes Keras, Tensorflow2.0, Numpy, Pandas, Matplotlib, Pillow, OpenCV in order to execute the code (training model and Evaluation model)
## 3. Data:<a id="data"></a>
The data used in this project is "Camera-trap" dataset, images in the dataset are high resolution with many objects in each image, the objects are at different sizes, many of them are small. Because of this, working with the dataset is much more challenging than normal dataset like COCO datasset or ImageNet and the model often has lower performance. Below is a sample image from the dataset:

![Sample Image](https://github.com/KEVIN-VN642/Object-Detection-with-Yolo3-model-and-impacts-of-imbalance-and-few-shot-on-model-s-performance/blob/main/yolo3/images/Sample%20Image.png)

## 4. How to understand code: <a id="code"></a>
Please find details in <b>Software Descriptions.xlsx</b> for fully understand project codes.

## 5. Results and findings:<a id="results"></a>
Please find presentation slide for full results. Here, I attach some figures to illustrate the work:

### 5.1 Model architecture:
![model architecture](https://github.com/KEVIN-VN642/Object-Detection-with-Yolo3-model-and-impacts-of-imbalance-and-few-shot-on-model-s-performance/blob/main/yolo3/images/model_architecture.png)

### 5.2 Loss function:
Loss function has three components: classification, regression and confidence losses.

![Loss function](https://github.com/KEVIN-VN642/Object-Detection-with-Yolo3-model-and-impacts-of-imbalance-and-few-shot-on-model-s-performance/blob/main/yolo3/images/Loss%20function.png)

### 4.3 Parameter tuning:
There are many parameters we could use to tune the model

![Parameter tuning](https://github.com/KEVIN-VN642/Object-Detection-with-Yolo3-model-and-impacts-of-imbalance-and-few-shot-on-model-s-performance/blob/main/yolo3/images/parameters%20tuning.png)

### 4.4 Model Performance before and after image augmentation & rebalance dataset:
The image augmentation technique is used to improve model performance (assume that we only work with given images, no collecting images from other sources). Substantial improvement when applying augmentation technique (external augmentation)

![results](https://github.com/KEVIN-VN642/Object-Detection-YOLO3-Imbalance-and-Fewshot-Learning/blob/main/yolo3/images/Result%20Table.png)







