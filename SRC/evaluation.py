"""Evaluation helpers for Learnova."""

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, mean_absolute_error,
    mean_squared_error, r2_score
)
import math

def classification_metrics(y_true, y_pred, y_probability=None):
    result = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, zero_division=0),
        "recall": recall_score(y_true, y_pred, zero_division=0),
        "f1": f1_score(y_true, y_pred, zero_division=0)
    }
    if y_probability is not None:
        result["roc_auc"] = roc_auc_score(y_true, y_probability)
    return result

def regression_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    return {
        "mae": mean_absolute_error(y_true, y_pred),
        "rmse": math.sqrt(mse),
        "r2": r2_score(y_true, y_pred)
    }
