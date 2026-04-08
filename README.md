# 🧠 AI-Based Supply Chain Management System (SCM)

## 📌 Project Overview
This project focuses on integrating Generative AI concepts into Supply Chain Management (SCM).  
It predicts future product demand using machine learning and generates intelligent insights to support decision-making.

The system is designed to work with **any CSV dataset**, making it flexible and scalable.

---

## 🎯 Objectives
- Predict future demand using historical data  
- Automate supply chain decision-making  
- Generate AI-based insights for inventory planning  
- Support multiple datasets dynamically  

---

## ⚙️ Features
- 📊 Works with any dataset (dynamic column selection)  
- 🤖 Machine Learning-based demand prediction  
- 📈 AI-generated insights for SCM decisions  
- 🔄 Handles real-world datasets (Kaggle supported)  
- 🧩 Modular code structure  

---

## 🏗️ Project Structure
AI_SCM_project/
│
├── main.py                  # Main program
│
├── model/
│   └── demand_model.py      # ML model & AI logic
│
├── utils/
│   └── data_loader.py       # Data loading & preprocessing
│
├── data/
│   └── *.csv                # Dataset files
│
└── requirements.txt

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
Required Libraries:
pandas
numpy
scikit-learn

## 📦 Requirements
python main.py
🧪 Usage Steps
- Place your dataset inside the data/ folder
- Run the program
-Enter:
  -Dataset file name
  -Date column name
  -Demand/Sales column name
Enter number of future days
View predictions and AI insights
📊 Example Input
Enter dataset file name: demand.csv  
Enter DATE column name: date  
Enter DEMAND column name: target_demand  
Enter number of future days: 10  
📈 Output
Predicted demand values for future days
AI-generated insights like:
Increase inventory
Maintain stock
Adjust supply chain
🧠 Technologies Used
Python
Pandas
NumPy
Scikit-learn (Linear Regression)
🚀 Future Enhancements
📊 Graph visualization
🤖 Integration with real Generative AI (LLMs)
📦 Multi-product forecasting
🌐 Web-based dashboard
☁️ Cloud deployment
💡 Conclusion

This project demonstrates how AI can improve Supply Chain Management by predicting demand and generating intelligent recommendations. It highlights the practical application of machine learning in real-world business problems.

👩‍💻 Author

Arpita Patil
AI/ML Engineering Student

📌 Note

This is a mini-project for academic purposes and can be extended into a full-scale industry-level system.


---
