DATASENSE BOT
	
Goal:
	Build a chatbot that answers questions from structured business data using a downloaded local LLM model only (no online API).

DataSense Bot: 
	It is an offline AI chatbot that answers questions from business data using:
•	🧠 Local LLM (Ollama – Llama3)
•	🐍 Python + Pandas
•	🛢 MySQL Database
•	💬 Natural Language → Pandas Code Execution

	It converts user questions into executable Python code, runs the code, shows results, and logs them in a database.

 Features
✔ Works fully offline
✔ Converts natural language to Pandas code
✔ Executes code safely
✔ Handles missing data
✔ Logs every query + result in MySQL
✔ Supports business analytics questions

Tech Stack
	
Component	Tool
Language	Python
LLM	Ollama (Codellama)
Database	MySQL
Data	CSV (Sales Data)
Libraries	pandas, mysql-connector


Example Questions to Ask

•	What is the total sales?
•	Show number of orders by region.
•	How many orders had sales above 50,000?
•	Which region has the highest sales?.
•	What is the total quantity sold?
•	Show the top 5 customers by purchase amount.
•	How many unique products were sold?
•	What is the average sales per customer?
•	What is the minimum and maximum sales recorded?
•	What percentage of total sales came from the East region?

Output Example:

Code Generated:
result = dataframe['Sales'].sum()
summary = f"Total sales = {result}"
Result: 481000
Insight: Total sales = 481000
Logged to database

Expected Output
•	AI writes Pandas code
•	Code runs & answers your question
•	Summary line printed
•	All logs stored in MySQL

