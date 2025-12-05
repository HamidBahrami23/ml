# 🧠 LeNet-5 CNN Architecture – MNIST Dataset

## 📌 Overview
This project implements the **classic LeNet-5 convolutional neural network architecture** for handwritten digit recognition using the **MNIST dataset**. LeNet-5, introduced by Yann LeCun in 1998, was one of the first successful CNNs for digit recognition.

---

## 📂 Project Structure

```
08_LeNet_5/
├── 08_LeNet_5.ipynb  # Main notebook with LeNet-5 implementation
├── src/              # Optional scripts (not used in this project)
└── data/             # Dataset (ignored by .gitignore)
```

---

## 🧠 Key Concepts
- Classic LeNet-5 architecture with 7 layers
- Convolutional layers with tanh activation
- Average pooling instead of max pooling
- Sigmoid activation for pooling layers
- Multiple convolutional and pooling stages
- Fully connected layers for classification
- Local Response Normalization

---

## ✅ Result Summary
- **Test accuracy achieved: 97.81%**
- **Total parameters: 61,706** (much smaller than modern architectures)
- Trained for 40 epochs with Adam optimizer
- Demonstrates the power of early CNN architectures

Training history shows steady improvement in both accuracy and loss over epochs.

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow.keras` | LeNet-5 model implementation |
| `numpy` | Array operations |
| `matplotlib` | Training history visualization |

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install tensorflow numpy matplotlib
   ```
2. Launch the notebook:
   ```bash
   jupyter notebook 08_LeNet_5.ipynb
   ```

---

## 💡 Learnings

- LeNet-5 was revolutionary for its time with hierarchical feature learning
- Average pooling was common in early CNNs
- The architecture scales well despite being relatively simple
- Understanding historical architectures helps appreciate modern developments

## 🚀 Future Improvements

- Experiment with different activation functions (ReLU vs tanh)
- Compare max pooling vs average pooling
- Try modern optimizers and learning rate schedules
- Implement data augmentation
- Apply LeNet-5 to other image classification tasks