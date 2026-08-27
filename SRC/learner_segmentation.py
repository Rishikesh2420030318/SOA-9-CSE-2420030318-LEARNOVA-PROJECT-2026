"""Learner segmentation using K-Means."""

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def segment_learners(features, n_clusters=3):
    numeric = features.select_dtypes(include="number").copy()
    scaler = StandardScaler()
    X = scaler.fit_transform(numeric)

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )
    labels = model.fit_predict(X)

    result = features.copy()
    result["cluster"] = labels
    return result, model, scaler
