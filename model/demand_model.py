import numpy as np
from sklearn.linear_model import LinearRegression

def prepare_data(df):
    print("\nSelect columns:")

    date_col = input("Enter DATE column name: ").lower()
    target_col = input("Enter DEMAND/SALES column name: ").lower()
    
    # Convert date to numeric
    df[date_col] = df[date_col].astype('category').cat.codes
    
    X = df[[date_col]]
    y = df[target_col]
    
    return X, y

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_demand(model, last_value, days):
    future = np.array(range(last_value, last_value + days)).reshape(-1, 1)
    predictions = model.predict(future)
    return predictions

def generate_insights(predictions):
    avg = np.mean(predictions)
    trend = predictions[-1] - predictions[0]

    if avg > 150 and trend > 0:
        return "📈 High and increasing demand → Increase inventory."
    elif avg > 150:
        return "⚠️ High demand → Maintain stock."
    elif trend > 0:
        return "🔼 Demand rising → Gradual increase needed."
    else:
        return "✅ Stable demand → Balanced inventory."
