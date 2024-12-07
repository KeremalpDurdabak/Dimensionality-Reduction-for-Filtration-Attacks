import pandas as pd
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import os

train_base_path = r"Lorem/Ipsum/"
test_base_path = r"Lorem/Ipsum/"
save_base_path = r"Lorem/Ipsum/"
types = ['0vs1_3', '0vs1', '0vs2', '0vs3', '0vsAll']
n = 5

def apply_pca(X_train, X_test, n):
    pca = PCA(n_components=n, random_state=42)
    return pca.fit_transform(X_train), pca.transform(X_test)

def apply_ica(X_train, X_test, n):
    ica = FastICA(n_components=n, random_state=42)
    return ica.fit_transform(X_train), ica.transform(X_test)

def apply_autoencoder(X_train, X_test, n):
    input_dim = X_train.shape[1]
    autoencoder = Sequential([
        Dense(64, activation='relu', input_dim=input_dim),
        Dense(n, activation='relu'),
        Dense(64, activation='relu'),
        Dense(input_dim, activation='sigmoid')
    ])
    autoencoder.compile(optimizer='adam', loss='mse')
    autoencoder.fit(X_train, X_train, epochs=50, batch_size=32, verbose=0)
    encoder = Sequential(autoencoder.layers[:2])
    return encoder.predict(X_train), encoder.predict(X_test)

methods = {
    "PCA": apply_pca,
    "ICA": apply_ica,
    "Autoencoder": apply_autoencoder
}

for type_ in types:
    train_path = os.path.join(train_base_path, f'stratified_day_{type_}', f'stratified_train_day_{type_}.csv')
    test_path = os.path.join(test_base_path, f'stratified_day_{type_}', f'stratified_test_day_{type_}.csv')
    
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    
    X_train = train_data.drop('insider', axis=1)
    y_train = train_data['insider']
    X_test = test_data.drop('insider', axis=1)
    y_test = test_data['insider']
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    for method_name, method in methods.items():
        save_path = os.path.join(save_base_path, method_name, "day", type_)
        os.makedirs(save_path, exist_ok=True)
        X_train_transformed, X_test_transformed = method(X_train_scaled, X_test_scaled, n)
        
        train_df = pd.DataFrame(X_train_transformed, columns=[f'{method_name}_{i+1}' for i in range(n)])
        train_df['insider'] = y_train
        test_df = pd.DataFrame(X_test_transformed, columns=[f'{method_name}_{i+1}' for i in range(n)])
        test_df['insider'] = y_test
        
        train_df.to_csv(os.path.join(save_path, f'DAY_{method_name}_{type_}_Stratified_Train.csv'), index=False)
        test_df.to_csv(os.path.join(save_path, f'DAY_{method_name}_{type_}_Stratified_Test.csv'), index=False)
