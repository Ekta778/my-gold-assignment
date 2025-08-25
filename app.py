from fastapi import FastAPI, Request
import sqlite3

app = FastAPI()

# --- Database Setup (SQLite) ---
def init_db():
    conn = sqlite3.connect("gold.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS purchases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT,
                    amount INTEGER)""")
    conn.commit()
    conn.close()

init_db()

# --- API 1: Chatbot for Gold ---
@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    user = data.get("user", "Guest")
    question = data.get("question", "").lower()

    # Hardcoded answer (like Simplify app)
    if "gold" in question:
        answer = (
            "Gold is a popular investment in India.\n"
            "- Digital Gold: invest from ₹10, no storage issues.\n"
            "- Gold ETFs: tax-friendly & liquid.\n"
            "Tip: Digital Gold is best for beginners!"
        )
        nudge = "Do you want to invest ₹10 in digital gold via Simplify Money?"
        return {"answer": answer, "nudge": nudge}
    else:
        return {"answer": "I can only help with gold investments."}

# --- API 2: Purchase Flow ---
@app.post("/purchase")
async def purchase_gold(request: Request):
    data = await request.json()
    user = data.get("user", "Guest")
    amount = data.get("amount", 10)  # Default ₹10

    conn = sqlite3.connect("gold.db")
    c = conn.cursor()
    c.execute("INSERT INTO purchases (user, amount) VALUES (?, ?)", (user, amount))
    conn.commit()
    conn.close()

    return {"message": f"Gold purchase of ₹{amount} successful for {user}!"}
