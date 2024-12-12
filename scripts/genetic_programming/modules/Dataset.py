import pandas as pd
from sklearn.utils import resample

class Dataset:
    feature_count = None
    feature_names = None
    X_train_full = None
    y_train_full = None
    X_train = None
    y_train = None
    unique_labels = None

    @classmethod
    def load_dataset(cls, train_path):
        # Load the dataset from the specified path
        train_data = pd.read_csv(train_path)
        cls.feature_count = train_data.shape[1] - 1
        feature_columns = [f'F{i}' for i in range(cls.feature_count)]
        train_data.columns = feature_columns + ['type']
        cls.X_train_full, cls.y_train_full = train_data.drop('type', axis=1), train_data['type']
        cls.unique_labels = cls.y_train_full.unique()

    @classmethod
    def stratified_sample(cls, tau):
        samples_per_label = tau // len(cls.unique_labels)
        sampled_data_features = []
        sampled_data_labels = []

        for label in cls.unique_labels:
            label_data = cls.X_train_full[cls.y_train_full == label]
            label_target = cls.y_train_full[cls.y_train_full == label]

            # Resample to achieve the desired number of samples per label
            if len(label_data) < samples_per_label:
                # Oversample if fewer instances than needed
                resampled_data, resampled_target = resample(label_data, label_target, 
                                                            replace=True, 
                                                            n_samples=samples_per_label)
            else:
                # Undersample if more instances than needed
                resampled_data, resampled_target = resample(label_data, label_target, 
                                                            replace=False, 
                                                            n_samples=samples_per_label)
            
            sampled_data_features.append(resampled_data)
            sampled_data_labels.append(resampled_target)

        # Concatenate all sampled subsets
        cls.X_train = pd.concat(sampled_data_features, ignore_index=True)
        cls.y_train = pd.concat(sampled_data_labels, ignore_index=True)
