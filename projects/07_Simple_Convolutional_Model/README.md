# 🔢 Simple Convolutional Neural Network – MNIST Dataset

## 📌 Overview
This project implements a **basic Convolutional Neural Network (CNN)** for handwritten digit recognition using the **MNIST dataset**. The goal is to demonstrate the fundamentals of convolutional layers, pooling, and feature extraction for image classification.

---

## 📂 Project Structure

```
07_Simple_Convolutional_Model/
├── 07_Simple_Convolutional_Model.ipynb  # Main notebook with CNN implementation
├── src/                                 # Optional scripts (not used in this project)
└── data/                               # Dataset (ignored by .gitignore)
```

---

## 🧠 Key Concepts
- Convolutional layers for feature extraction
- Max pooling for downsampling
- ReLU activation functions
- Flattening for fully connected layers
- Softmax for multi-class classification
- Feature map visualization
- Basic CNN architecture principles

---

## ✅ Result Summary
- **Test accuracy achieved: 98.22%**
- Simple architecture with single convolutional layer
- Demonstrates effectiveness of CNNs for image classification

Confusion Matrix visualization and feature map analysis included in the notebook.

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow.keras` | CNN model building and training |
| `numpy` | Array operations |
| `matplotlib` | Visualization of feature maps and results |

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install tensorflow numpy matplotlib
   ```
2. Launch the notebook:
   ```bash
   jupyter notebook 07_Simple_Convolutional_Model.ipynb
   ```

---

## 💡 Learnings

- Convolutional layers automatically learn spatial features
- Pooling reduces computational complexity while preserving important features
- Even simple CNNs can achieve high accuracy on MNIST
- Feature map visualization helps understand what the network learns

## 🚀 Future Improvements

- Add more convolutional layers for deeper feature extraction
- Experiment with different activation functions and optimizers
- Implement data augmentation
- Compare with fully connected networks
- Try the model on other image datasets