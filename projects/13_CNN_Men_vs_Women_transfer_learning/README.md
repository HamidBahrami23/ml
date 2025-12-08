# 🖼️ Transfer Learning VGG16 – Men vs Women Classification

## 📌 Overview
This project demonstrates transfer learning using VGG16 as a feature extractor for men vs women image classification.  
Features are extracted from frozen VGG16 layers and fed into a custom classifier, achieving excellent performance with minimal training.

---

## 📂 Project Structure

```
13_CNN_Men_vs_Women_transfer_learning/
├── notebook/
│   ├── 13_CNN_Men_vs_Women_transfer_learning.ipynb       # Main transfer learning notebook
│   ├── 13_CNN_Men_vs_Women_transfer_learning-dataaug.ipynb # Data augmentation variant
│   └── 13_using_my_saved_model.ipynb                     # Model inference notebook
├── src/
│   ├── namedatset.py             # Dataset utilities
│   └── namedatsetwomen.py        # Additional dataset scripts
```

---

## 🧠 Key Concepts
- Transfer learning with VGG16 as feature extractor
- Feature extraction from pre-trained ImageNet weights
- Frozen convolutional base, trainable classifier
- Custom classifier: Global average pooling → Dense(256) → Dropout → Dense(1)
- Data augmentation (horizontal flip, rotation, zoom)
- Binary classification with sigmoid activation
- Adam optimizer with default learning rate

---

## ✅ Result Summary
- **Base model**: VGG16 (frozen convolutional layers)
- **Input size**: 180x180 RGB images
- **Dataset**: 2000 train, 400 validation, 400 test images
- **Training epochs**: 10
- **Test accuracy achieved**: **0.895 (89.5%)**
- **Training time**: Fast convergence in few epochs

Confusion Matrix:

| Class | Performance |
|-------|-------------|
| Men   | Excellent classification |
| Women | Excellent classification |

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `tensorflow` / `keras` | VGG16 model, transfer learning |
| `matplotlib` | Training visualization |
| `numpy` | Feature processing |

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Launch the main notebook:
   ```bash
   jupyter notebook notebook/13_CNN_Men_vs_Women_transfer_learning.ipynb
   ```

---

## 💡 Learnings

- Transfer learning dramatically improves performance and reduces training time
- Feature extraction approach is computationally efficient
- Pre-trained models on ImageNet provide excellent general features
- Simple classifiers on extracted features can achieve high accuracy
- Data augmentation enhances generalization even with transfer learning

## 🚀 Future Improvements

- Fine-tune some VGG16 layers for potentially better performance
- Experiment with other pre-trained models (ResNet, EfficientNet)
- Implement end-to-end fine-tuning
- Add more regularization techniques
- Compare feature extraction vs. fine-tuning approaches