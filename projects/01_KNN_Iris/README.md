# 🌼 KNN Classification – Iris Dataset

## 📌 Overview
This project applies **K-Nearest Neighbors (KNN)** to classify flower types in the well-known **Iris dataset**.  
The goal is to understand how KNN works on a simple dataset and explore model evaluation and hyperparameter tuning.

---

## 📂 Project Structure


01_KNN_Iris/
├── notebooks/
│ └── 01_KNN_Iris.ipynb # Main notebook
├── src/ # Optional scripts (not used in this project)
└── data/ # Dataset (ignored by .gitignore)

---

## 🧠 Key Concepts
- Train/test splitting
- Feature scaling using `StandardScaler`
- Distance-based learning (KNN)
- Model evaluation using:
  - Accuracy
  - Confusion Matrix
  - Classification Report (Precision/Recall/F1)
- Hyperparameter Tuning (finding best **K**)

---

## ✅ Result Summary
- Best value of **K (number of neighbors): `9`**
- Test accuracy achieved: **0.9556 (≈ 96%)**

Confusion Matrix:

| Setosa | Versicolor | Virginica |
|--------|------------|-----------|
| ✅ perfect | ✅ perfect | 🔸 some misclassifications |

---

## 🔧 Tech Stack
| Library | Usage |
|---------|--------|
| `pandas` / `numpy` | Data manipulation |
| `scikit-learn` | KNN model, scaling, evaluation |
| `matplotlib` | Visualization |

---

## ▶️ How to Run
```bash
pip install -r requirements.txt


Open notebook:

jupyter notebook notebooks/01_KNN_Iris.ipynb

---

##💡 Learnings

Scaling is critical in KNN.

Higher K reduces noise but too large K → model becomes too general.

Visualization of K vs accuracy reveals the “elbow point”.

##🚀 Future Improvements

Try KNN on different datasets

Compare with other algorithms (SVM / Decision Tree / Logistic Regression)

