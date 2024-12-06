import os
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from dataset_paths import dataset_paths  # Replace with the correct import or hard-code paths

# Define the target column
target_column = "type"

def load_data(path):
    df = pd.read_csv(path)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

def evaluate_model(model, X_train, y_train, X_test, y_test):
    model.fit(X_train, y_train)
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)

    # Calculate metrics
    metrics_train = calculate_metrics(y_train, y_pred_train)
    metrics_test = calculate_metrics(y_test, y_pred_test)
    
    return metrics_train, metrics_test

def calculate_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='macro', zero_division=0)
    recall = recall_score(y_true, y_pred, average='macro', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='macro', zero_division=0)
    labels = sorted(y_true.unique())
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    return {'F1 Macro': f1, 'Precision': precision, 'Accuracy': accuracy, 'Recall': recall, 'Confusion Matrix': cm.tolist()}

def save_metrics_to_file(metrics, folder_path, filename):
    os.makedirs(folder_path, exist_ok=True)
    filepath = os.path.join(folder_path, filename)
    with open(filepath, 'w') as file:
        for key, value in metrics.items():
            file.write(f"{key}: {value}\n")

def save_general_statistics(X_train, y_train, X_test, y_test, folder_path):
    filepath = os.path.join(folder_path, "General_Statistics.txt")
    total_features = X_train.shape[1]
    total_instances = len(X_train) + len(X_test)
    train_counts = y_train.value_counts()
    test_counts = y_test.value_counts()
    
    with open(filepath, 'w') as file:
        file.write(f"Features Used: {total_features}\n")
        file.write(f"Total Instances: {total_instances}\n")
        for label in sorted(pd.concat([y_train, y_test]).unique()):
            file.write(f"Total {label} Instances: {(train_counts.get(label, 0) + test_counts.get(label, 0))}\n")
            file.write(f"Training {label} Instances: {train_counts.get(label, 0)}\n")
            file.write(f"Testing {label} Instances: {test_counts.get(label, 0)}\n")

def run_random_forest_for_each_dataset_type():
    base_folder = "Lorem/Ipsum/ML_Scores"  # Anonymized base folder path

    for key, path in dataset_paths.items():
        if "Train" in key:
            dataset_type, sampling_type = key.split('_')[1:3]
            test_key = f"{dataset_type}_Stratified_Test_Path"
            test_path = dataset_paths[test_key]

            X_train, y_train = load_data(path)
            X_test, y_test = load_data(test_path)

            rf_model = RandomForestClassifier()

            metrics_train, metrics_test = evaluate_model(rf_model, X_train, y_train, X_test, y_test)
            results_dir = os.path.join(base_folder, "RandomForest", dataset_type, sampling_type)

            save_metrics_to_file(metrics_train, results_dir, 'Training_Results.txt')
            save_metrics_to_file(metrics_test, results_dir, 'Testing_Results.txt')
            save_general_statistics(X_train, y_train, X_test, y_test, results_dir)

if __name__ == "__main__":
    run_random_forest_for_each_dataset_type()
