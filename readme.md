# Custom YOLO Model Finetuning

This project contains code to train an object detection model on a custom dataset.

### Dataset

- The dataset is private and cannot be shared.  
- The dataset contains 117 high quality images with respective annotations in the YOLO format.  
- The dataset contained images of tabular data and contains 3 classes of objects: `table`, `header`, `column`.

### Training

- I chose the YOLOv8 model by UltraLytics for training.
- Ultralytics YOLOv8 is a cutting-edge, SOTA model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. 
- This model uses Pytorch to train the model internally and provides very easy method of training custom models either by using CLI or the Python API.
- Out of the various pretrained variants of YOLOv8, the `YOLOv8n nano` model is apt one. Input size is `640` and contains `3.4 million` parameters.

- Firstly, I trained the base model for `25 epochs` with default parameters and found:
  - Precision: `0.871`
  - Recall: `0.895`
  - mAP50: `0.947`
  - mAP50-95: `0.737`

- Then second model was trained with some data augmentation steps added to the training like `HSV augmentation`, `image scaling`, `image translation`, etc.
  - Precision: `0.871`
  - Recall: `0.901`
  - mAP50: `0.948`
  - mAP50-95: `0.738`


### Installation and Inference
To run the code, first install the library 
Ultralytics:

```bash
pip install ultralytics
```

Extract the dataset in the dataset folder and run the train.ipynb.

Improvements
There are several ways using which we can further improve the accuracy of the model like:

By increasing the size of the dataset as 117 images are very less.
By increasing the number of epochs for training from 25 to say 100.
Can experiment with other models like Masked RNNs for object detection of YOLO NAS or YOLOx, etc.

Instead of training the YOLOv8 ‘nano’ model, the ‘large’ variant can be used for better and robust results.
Inference
For making an inference from the model, you can just run the last cell from the train.ipynb:

model.predict('filename.jpg')

Or run the tornado web server:

pip install tornado
python tornadoApp.py
python inference.py