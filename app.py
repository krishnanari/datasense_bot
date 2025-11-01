import pandas as pd
from llm_engine import ask_llm
from database import init_db, log_query

# Initialize database
init_db()

# Load dataset
df = pd.read_csv(r"C:\Users\USER\datasense_bot\data\business_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.fillna(0)

print("\n🤖 DataSense Bot — Local Mode (Codellama + Pandas)\n")

while True:
    user_input = input("\nAsk a question (or type exit): ")

    if user_input.lower() == "exit":
        print("👋 Bye!")
        break

    prompt = f"""
You are a pandas expert AI.

Convert the user question into EXACT python pandas code.

RULES:
- Use dataframe = df
- Only output these TWO LINES, nothing else:
  result = ...
  summary = f"..."
- Do NOT:
  - print
  - return
  - import anything
  - read files
  - add comments or explanation
- Date column rule: dataframe['Date'].dt.year / month only
- Allowed columns: OrderID, Customer, Product, Category, Quantity, Price, Sales, Date, Region
- If question unclear → result = dataframe['Sales'].sum()

User question: {user_input}
"""

    raw = ask_llm(prompt).strip()
    raw = raw.replace("```python", "").replace("```", "").strip()

    # Extract ONLY result= and summary= lines
    lines = raw.splitlines()
    code_lines = []
    for line in lines:
        if "result" in line or "summary" in line:
            code_lines.append(line.strip())
        if len(code_lines) == 2:
            break

    code = "\n".join(code_lines)

    print("\n🧠 LLM Generated Code:\n", code)

    namespace = {"df": df, "dataframe": df, "result": None, "summary": ""}

    try:
        exec(code, namespace)

        result = namespace.get("result", None)
        summary = namespace.get("summary", "")

        if result is None:
            result = "⚠️ No result generated"

        if summary == "":
            summary = f"Answer: {result}"

        print("\n📊 Result:", result)
        print("💡 Insight:", summary)

        log_query(user_input, code, str(result))
        print("✅ Logged to database")

    except Exception as e:
        print("\n❌ Error executing:", e)
        log_query(user_input, code, f"Error: {e}")
