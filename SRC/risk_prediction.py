"""Starter learner-risk prediction module."""

from sklearn.ensemble import RandomForestClassifier

def train_risk_model(X_train, y_train):
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)
    return model

def predict_risk(model, X):
    return model.predict(X)

def predict_risk_probability(model, X):
    if hasattr(model, "predict_proba"):
        return model.predict_proba(X)[:, 1]
    return None
