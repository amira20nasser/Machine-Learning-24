import os
from numpy import resize
from skimage import color
from skimage.feature import hog
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from PIL import Image
import pandas as pd

def extract_features(folder_path):
    features = []
    labels = []
    class_names = os.listdir(folder_path)
    for class_name in class_names:
        class_folder = os.path.join(folder_path, class_name)
        for image_name in os.listdir(class_folder):
                image_path = os.path.join(class_folder, image_name)
                image = Image.open(image_path).convert('L')
                image = resize(image, (128, 64))
                fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8),
                                    cells_per_block=(2, 2), visualize=True)
                # if image.ndim >= 2:
                #     image = image [ :,:,None]

                # fd, hog_image = hog(image, orientations=9, pixels_per_cell=(8, 8),
                #                         cells_per_block=(2, 2), visualize=True,multichannel=True)
                features.append(fd)
                labels.append(class_name)
    return features, labels


train_folder = "train"
test_folder = "test"
train_features, train_labels = extract_features(train_folder)
train_df = pd.DataFrame(train_features)
train_df['label'] = train_labels
print(train_df.head(2))

test_features, test_labels = extract_features(test_folder)
test_df = pd.DataFrame(test_features)
test_df['label'] = test_labels
print(test_df.head(2))



# Train SVM model
X_train = train_df.drop(columns=['label'])
X_test = test_df.drop(columns=['label'])
y_train =  train_df['label']
y_test = test_df['label']

from sklearn.model_selection import GridSearchCV
param_grid = {
    'C': [0.1, 1, 10, 100,12],
    'gamma': [0.001, 0.01, 0.1, 1,2,3],
    'kernel': ['rbf', 'linear', 'poly']
}

grid_search = GridSearchCV(SVC(), param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
best_svm_model = grid_search.best_estimator_
svm_model = SVC(kernel='rbf',C=100,gamma=0.01).fit(X_train,y_train)
# Test the trained model
y_pred = best_svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Test GRID:", accuracy)

# Test Train Model
print(X_train.shape)
y_pre = svm_model.predict(X_train)
accuracy = accuracy_score(y_train, y_pre)
print("Accuracy Train:", accuracy)
# Test the trained model
y_pred = svm_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Test:", accuracy)




