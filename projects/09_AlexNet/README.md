# 🏆 AlexNet CNN Architecture – MNIST Dataset

## 📌 Overview
This project implements the **revolutionary AlexNet convolutional neural network architecture** for handwritten digit recognition using the **MNIST dataset**. AlexNet, developed by Alex Krizhevsky et al., won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC) in 2012 and sparked the deep learning revolution.

---

## 📂 Project Structure

```
09_AlexNet/
├── 09_AlexNet.ipynb  # Main notebook with AlexNet implementation
├── src/              # Optional scripts (not used in this project)
└── data/             # Dataset (ignored by .gitignore)
```

---

## 🧠 Key Concepts
- Deep convolutional neural network (8 layers)
- Local Response Normalization (LRN)
- Overlapping max pooling
- ReLU activation functions
- Dropout for regularization
- Large number of parameters (21.6M)
- Multiple convolutional stages
- Data augmentation and preprocessing

---

## ✅ Result Summary
- **Test accuracy achieved: 98.88%**
- **Total parameters: 21,622,154** (82.48 MB)
- Trained for 40 epochs with Adam optimizer
- Demonstrates the power of deep learning architectures

The model shows excellent convergence with high validation accuracy throughout training.

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow.keras` | AlexNet model implementation |
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
   jupyter notebook 09_AlexNet.ipynb
   ```

---

## 💡 Learnings

- AlexNet showed that deeper networks with more parameters can achieve breakthrough performance
- ReLU activation helps with vanishing gradient problems
- Dropout prevents overfitting in deep networks
- Local Response Normalization improves generalization
- Deep learning requires significant computational resources

## 🚀 Future Improvements

- Implement data augmentation techniques
- Experiment with different learning rates and optimizers
- Try batch normalization instead of LRN
- Compare with modern architectures like ResNet
- Apply AlexNet to larger image datasets like ImageNet