# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Generate random weather data for demonstration purposes
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
temperature = np.random.randint(50, 90, size=len(dates))
humidity = np.random.randint(30, 70, size=len(dates))
wind_speed = np.random.randint(5, 20, size=len(dates))

# Create a DataFrame
weather_data = pd.DataFrame({'Date': dates, 'Temperature': temperature, 'Humidity': humidity, 'Wind_Speed': wind_speed})

# Feature engineering: Extract day of the year as a feature
weather_data['Day_Of_Year'] = weather_data['Date'].dt.dayofyear

# Target variable: Assume a simple linear trend for demonstration purposes
weather_data['Temperature_Next_5_Days'] = weather_data['Temperature'] + np.arange(1, len(dates) + 1) * 0.5

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    weather_data[['Day_Of_Year', 'Temperature', 'Humidity', 'Wind_Speed']],
    weather_data['Temperature_Next_5_Days'],
    test_size=0.2,
    random_state=42
)

# Train a RandomForestRegressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f'Mean Squared Error: {mse}')

# Data clustering for visualization
# Select features for clustering (temperature, humidity, wind_speed)
features_for_clustering = weather_data[['Temperature', 'Humidity', 'Wind_Speed']]

# Apply k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
weather_data['Cluster'] = kmeans.fit_predict(features_for_clustering)

# Reduce dimensionality for visualization
pca = PCA(n_components=2)
reduced_features = pca.fit_transform(features_for_clustering)
weather_data['PCA1'] = reduced_features[:, 0]
weather_data['PCA2'] = reduced_features[:, 1]

# Plot the clusters in 2D
plt.figure(figsize=(10, 6))
plt.scatter(weather_data['PCA1'], weather_data['PCA2'], c=weather_data['Cluster'], cmap='viridis')
plt.title('Weather Data Clustering')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.show()
