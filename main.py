from utils.data_loader import load_data
from model.demand_model import prepare_data, train_model, predict_demand, generate_insights

def main():
    print("=== UNIVERSAL AI SCM SYSTEM ===\n")
    
    # Load dataset
    df = load_data()
    
    # Prepare data
    X, y = prepare_data(df)
    
    # Train model
    model = train_model(X, y)
    
    # Input prediction
    days = int(input("\nEnter number of future days: "))
    
    last_value = X.iloc[-1, 0]
    
    predictions = predict_demand(model, last_value, days)
    
    print("\n📊 Predictions:")
    for i, p in enumerate(predictions, 1):
        print(f"Day {i}: {round(p, 2)}")
    
    # AI Insight
    insight = generate_insights(predictions)
    
    print("\n🤖 AI Insight:")
    print(insight)

if __name__ == "__main__":
    main()