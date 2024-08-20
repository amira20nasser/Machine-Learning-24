## Introduction

This report presents the results of applying a Support Vector Machine (SVM) classifier to a dataset for image classification. The goal is to evaluate the performance of the SVM model on both training and testing datasets.

## Feature Extraction

The dataset consists of images organized into classes, where each class represents a different category. Features are extracted from these images using the Histogram of Oriented Gradients (HOG) technique.

## Model Training

The SVM model is trained using the extracted features from the training dataset. Grid search is employed to find the optimal hyperparameters for the SVM model, including the regularization parameter (C), the kernel coefficient (gamma), and the kernel type (rbf, linear, poly). The best parameters obtained from the grid search are utilized to train the final SVM model: `{'C': 100, 'gamma': 0.01, 'kernel': 'rbf'}`.

## Model Evaluation

The trained SVM model is evaluated on both the training and testing datasets. The accuracy scores are calculated to assess the model's performance.

## Results

- **Training Accuracy:** 1.0
- **Testing Accuracy:** 0.7778

## Conclusion

The SVM model demonstrates 77% testing accuracy.
