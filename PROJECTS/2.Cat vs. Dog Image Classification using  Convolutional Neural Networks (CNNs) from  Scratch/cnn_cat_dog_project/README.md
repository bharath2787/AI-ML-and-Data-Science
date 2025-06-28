# Cat vs Dog Classifier 

An end-to-end deep learning project that classifies images as cats or dogs using a Convolutional Neural Network (CNN). The project includes:

- Data preprocessing and splitting
- CNN model training using Keras
- Saving and loading the trained model
- Streamlit-based drag-and-drop UI for prediction

##  Setup

 - install docker from https://www.docker.com/get-started/ 
 - Download the project 
 - Open a terminal in the projects's root directory
 - run the commands one by one from the "runcommands.txt" file

### Install dependencies

```bash
pip install tensorflow streamlit pillow
```

### Train the model (locally)

Place the original Kaggle dataset images in `data/train/` (flat folder), then run:

```bash
python cnn_train.py
```
### Train the model(if using docker)

docker build -t cnn-gpu-image .

docker run --gpus all -it --rm ^
  -v "D:\\0.LatestDSCourse\\DS_course\\TransferLearning\\dataset\\PetImages:/tf/code/dataset/PetImages" ^
  -v "D:\\0.LatestDSCourse\\DS_course\\1.NDemo\\Projects\\CNN\\cnn_cat_dog_project\\models:/tf/models" ^
  cnn-gpu-image


### Launch the UI

```bash
streamlit run app.py
```

## 📁 Folder Structure

```
cnn_cat_dog_project/
│
├── app.py              # Streamlit UI
├── cnn_train.py        # Model training script
├── README.md
└── data/
    └── train/          # Place Kaggle images here (cat.0.jpg, dog.0.jpg, ...)
```


