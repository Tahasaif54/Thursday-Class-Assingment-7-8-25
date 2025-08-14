# 🧠 OpenAI Agents SDK – Assignment Solutions

This repository contains my completed solutions for three assignments based on the **OpenAI Agents SDK**, demonstrating **guardrails**, **dynamic instructions**, and a **smart customer support bot** with advanced features.

---

## 📂 Assignments Overview

### 1️⃣ Output Guardrail Functionality
**File:** `Assignment 1/guardrails_functions/output_guardrails.py`  
**Objective:**  
Extend the existing guardrails example to include **output guardrails**.

**Features Implemented:**
- Blocks **non-math** queries using input guardrails.
- Filters agent responses to **avoid political topics** and **political figures**.
- Provides a safe fallback message when blocked.

✅ **Tested Scenarios:**  
✔ Non-math query → blocked with a friendly warning.  
✔ Math query → processed normally.  
✔ Political question → blocked with a safe response.  

---

### 2️⃣ Dynamic Instructions for Multi-Hotel Assistant
**File:** `Assignment 2/my_agent/hotel_assistant.py`  
**Objective:**  
Convert static instructions into **dynamic instructions** so a single agent can handle multiple hotels.

**Features Implemented:**
- Stores and retrieves details for **multiple hotels**.
- Uses **context awareness** to respond with the correct hotel info.
- Returns dynamic responses based on hotel name detected in user query.

✅ **Tested Scenarios:**  
✔ Asking for Hotel A’s booking details returns Hotel A info.  
✔ Asking for Hotel B’s facilities returns Hotel B info.  
✔ Switching between hotels works seamlessly.

---

### 3️⃣ Smart Customer Support Bot
**Files:**  
- `my_agents/bot_agent.py`  
- `my_agents/human_agent.py`
- `my_agents/input_guardrail_agent.py`  
- `tools/order_status_tool.py`
- `data_schemas/check_guardrail_output.py`
- `data_schemas/order_status_schema.py`
- `confg/confg.py`
- `main.py`
- `.env`

**Objective:**  
Build a **customer support bot** that answers FAQs, tracks orders, applies guardrails, and escalates to a human agent.

**Features Implemented:**
- **BotAgent** for FAQs + order tracking.
- **HumanAgent** for escalations (handoff).
- `@function_tool` for **get_order_status(order_id)**:
  - Uses `is_enabled` to activate only for order queries.
  - Uses `error_function` for friendly error messages.
- **Guardrails** for blocking/rephrasing offensive input.
- **Handoff** triggered for:
  - Complex queries.
  - Negative sentiment.
- **ModelSettings**:
  - `tool_choice="auto"`.
  - (Metadata optional – tested without for final version).

✅ **Tested Scenarios:**  
✔ Order status query → returns correct status.  
✔ Offensive input → blocked with safe message.  
✔ Complex request → escalates to HumanAgent.  
✔ FAQ query → handled instantly.  
✔ Order not found → returns friendly error.

---

## 📜 References
- [Anthropic Design Patterns](https://www.anthropic.com/engineering/building-effective-agents)  
- [OpenAI Agents – Running Agents](https://openai.github.io/openai-agents-python/running_agents/)  
- [Handoffs](https://openai.github.io/openai-agents-python/handoffs/)  
- [Guardrails](https://openai.github.io/openai-agents-python/guardrails/)  
- [Guardrails Reference](https://openai.github.io/openai-agents-python/ref/guardrail/)  
- [Lifecycle](https://openai.github.io/openai-agents-python/ref/lifecycle/)  
- [Agents Reference](https://openai.github.io/openai-agents-python/ref/agent/)  
- [Model Settings](https://openai.github.io/openai-agents-python/ref/model_settings/#agents.model_settings.ModelSettings)  

---

## 🚀 How to Run
```bash
# Install dependencies
uv add openai-agents python-dotenv

# Add API KEY in .env File
add GEMINI_API_KEY="YOUR_API_KEY_HERE" IN .env file 

# Run Guardrails assignment
cd "Assignment 1"
uv run main.py

# Run Dynamic Hotel Assistant
cd "Assignment 2"
uv run main.py

# Run Smart Customer Support Bot
cd "Assignment 3"
uv run main.py
````

---

## 📌 Notes

* All scenarios have been tested and produce expected results.
* Metadata usage is optional; final implementation works without it.
* Logs show function calls, guardrail triggers, and handoff events.

---

### 📝 Submission Details

| **Submitted by** | **Taha Saif** |
|------------------|--------------|
| **Student Roll No** | 465829 |
| **Slot** | Thursday Evening — 7:00 PM to 10:00 PM |
| **Date** | 15 August 2025 |

