# 🚀 02\_CNN\_Hoda: Persian/Arabic Digit Classification

## 📌 Overview

This project implements a **Convolutional Neural Network (CNN)** for the classification of **Persian and Arabic handwritten digits (0-9)** using the **HODA dataset**. The goal is to build, train, and evaluate a robust deep learning model to accurately recognize these characters, which serves as a regional equivalent to the classic MNIST challenge.

## 💾 Dataset

### HODA (Handwritten Optical Digit Assistant) Dataset

  * **Description:** A large dataset of normalized handwritten digits (0-9) primarily used for research on Persian and Arabic optical character recognition (OCR).
  * **Format:** The raw data is provided in **MATLAB (.mat)** format.
  * **Source:** [Hoda Dataset on Kaggle](https://www.kaggle.com/datasets/invalizare/hoda-mat)

## 📂 Project Structure

```
02_CNN_Hoda/
├── notebooks/
│   └── 01_CNN_Hoda.ipynb  # Main data preprocessing, model building, and training notebook
├── data/                  # Contains the raw 'Data_hoda_full.mat' file
└── README.md
```

-----

## 🧠 Key Concepts & Methodology

The project follows a standard deep learning pipeline:

1.  **Data Loading:** Reading the data from the `.mat` file using `scipy.io`.
2.  **Image Preprocessing:**
      * **Resizing:** All images are resized to a fixed $(30 \times 30)$ dimension using `cv2.resize`.
      * **Splitting:** Data is split into **Train (90%), Validation (5%), and Test (5%)** sets using stratified sampling.
      * **Reshaping:** Images are reshaped to the CNN input format: $(N, 30, 30, 1)$.
      * **Normalization:** Pixel values are scaled to $[0, 1]$ by dividing by $255.0$.
      * **One-Hot Encoding:** Labels are converted using `to_categorical` for multi-class classification.
3.  **CNN Architecture:** A simple Sequential model is used, consisting of:
      * `Conv2D` (32 filters, $3 \times 3$ kernel, ReLU)
      * `MaxPooling2D` ($2 \times 2$)
      * `Flatten`
      * **`Dense` Hidden Layer (128 neurons, ReLU)**
      * `Dense` Output Layer (10 neurons, Softmax)
4.  **Training:** The model is compiled with the **Adam optimizer** and **Categorical Cross-Entropy loss**.

-----

## ✅ Result Summary

The model achieved excellent performance on the Hoda dataset after training for 5 epochs.

| Metric | Train (Last Epoch) | Validation | Test Set |
| :--- | :--- | :--- | :--- |
| **Accuracy** | 99.81% | **99.47%** | **99.50%** |
| Loss | 0.0057 | 0.0239 | 0.0299 |

The model demonstrates strong **generalization ability** with the Test Accuracy aligning closely with the Validation Accuracy.

-----

## 🔧 Tech Stack

| Library | Usage |
| :--- | :--- |
| **TensorFlow / Keras** | Core deep learning framework for model definition, compilation, and training. |
| **scipy.io** | Loading the MATLAB (`.mat`) format dataset. |
| **NumPy** | Fundamental array and mathematical operations (reshaping, stacking, splitting). |
| **OpenCV (`cv2`)** | Image resizing operation. |
| **scikit-learn** | `train_test_split` for robust data partitioning. |
| **Matplotlib** | Data visualization (e.g., displaying sample images). |

## ▶️ How to Run

1.  **Prerequisites:** Ensure you have Python and necessary libraries installed (preferably in a virtual environment).

2.  **Install Dependencies:**

    ```bash
    pip install numpy opencv-python tensorflow scipy scikit-learn matplotlib
    ```

3.  **Data Setup:** Download the `Data_hoda_full.mat` file and place it in the designated `data/` directory, or update the file path in the notebook.

4.  **Execute:** Open and run the Jupyter Notebook:

    ```bash
    jupyter notebook notebooks/01_CNN_Hoda.ipynb
    ```

-----

## 🚀 Future Improvements

  * **Regularization:** Introduce **Dropout** layers to further mitigate potential overfitting.
  * **Data Augmentation:** Implement techniques like rotation, shifting, and zooming to increase the effective size of the training data and improve robustness.
  * **Advanced Architectures:** Experiment with deeper or pre-trained models (e.g., LeNet variations).
  * **Optimization:** Implement **Learning Rate Scheduling** or early stopping callbacks during training.