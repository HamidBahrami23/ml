# 🖼️ Custom VGGNet – Men vs Women Classification

## 📌 Overview
This project implements a custom VGG-like convolutional neural network for binary classification of men vs women images.  
The model uses a VGG-inspired architecture with increasing convolutional layers and max pooling, trained on a subset of the Men-Women dataset from Kaggle.

---

## 📂 Project Structure

```
11_VGGNet/
├── notebook/
│   └── 11_VGGNet.ipynb  # Main notebook with model implementation
└── src/                # Optional scripts (not used in this project)
```

---

## 🧠 Key Concepts
- Custom CNN architecture inspired by VGGNet
- Convolutional layers with increasing filters (64 → 128 → 256 → 512)
- Max pooling for downsampling
- Data augmentation (horizontal flip, rotation, zoom)
- Binary classification with sigmoid activation
- Adam optimizer with low learning rate (0.0001)

---

## ✅ Result Summary
- **Architecture**: Custom VGG-like with 5 conv blocks
- **Input size**: 224x224 RGB images
- **Dataset**: 2000 train, 400 validation, 400 test images
- **Training epochs**: 40
- **Final performance**: Model struggled with convergence, accuracy around 50% (random guessing level)

Confusion Matrix:

| Class | Performance |
|-------|-------------|
| Men   | Poor classification |
| Women | Poor classification |

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow` / `keras` | CNN model, training |
| `matplotlib` | Visualization |
| `numpy` | Data manipulation |

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the notebook:
   ```bash
   jupyter notebook notebook/11_VGGNet.ipynb
   ```

---

## 💡 Learnings

- Custom CNN architectures require careful hyperparameter tuning
- Learning rate and model complexity are critical for convergence
- Data augmentation helps but isn't sufficient for poor model design
- Transfer learning approaches often perform better than training from scratch

## 🚀 Future Improvements

- Implement transfer learning with pre-trained models (VGG16, ResNet)
- Use larger datasets or better data preprocessing
- Experiment with different architectures (ResNet, EfficientNet)
- Add regularization techniques (dropout, batch normalization)
- Fine-tune hyperparameters systematically