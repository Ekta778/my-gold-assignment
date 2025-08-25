# my-gold-assignment

# Simplify Money - Gold Investment Workflow (Assignment)

This is a backend simulation of Simplify Money's Kuberi AI workflow.

## APIs

### 1. `/ask`
- Input: `{"user": "Ekta", "question": "Should I invest in gold?"}`
- Output: Returns gold investment insights + a nudge to buy gold.

### 2. `/purchase`
- Input: `{"user": "Ekta", "amount": 10}`
- Output: Confirms gold purchase and stores it in SQLite DB.

## Run Locally
```bash
uvicorn app:app --reload
