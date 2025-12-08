# 🖼️ Simple CNN – Men vs Women Classification

## 📌 Overview
This project builds a simple convolutional neural network for binary classification of men vs women images.  
The model uses a basic CNN architecture with multiple conv layers and global average pooling, trained on the Men-Women dataset from Kaggle.

---

## 📂 Project Structure

```
12_CNN_Men_vs_Women/
├── notebook/
│   └── 12_CNN_Men_vs_Women.ipynb  # Main notebook with model implementation
├── src/
│   ├── namedatset.py             # Dataset utilities
│   └── namedatsetwomen.py        # Additional dataset scripts
```

---

## 🧠 Key Concepts
- Simple CNN architecture with increasing filters
- Convolutional layers (32 → 64 → 128 → 256 → 512 filters)
- Max pooling for spatial reduction
- Global average pooling before dense layers
- Data augmentation (horizontal flip, rotation, zoom)
- Binary classification with sigmoid activation
- Adam optimizer with default learning rate

---

## ✅ Result Summary
- **Architecture**: 5 conv blocks with global average pooling
- **Input size**: 180x180 RGB images
- **Dataset**: 2000 train, 400 validation, 400 test images
- **Training epochs**: 75
- **Final performance**: Test accuracy around 80-85% (good performance for custom CNN)

Confusion Matrix:

| Class | Performance |
|-------|-------------|
| Men   | Good classification |
| Women | Good classification |

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
   jupyter notebook notebook/12_CNN_Men_vs_Women.ipynb
   ```

---

## 💡 Learnings

- Simple CNNs can achieve good performance with sufficient training
- Global average pooling reduces overfitting compared to flatten + dense
- Data augmentation significantly improves generalization
- More epochs allow better convergence but watch for overfitting

## 🚀 Future Improvements

- Implement early stopping and learning rate scheduling
- Add batch normalization for faster convergence
- Experiment with different architectures (ResNet blocks)
- Use transfer learning for potentially better results
- Add more sophisticated data augmentation