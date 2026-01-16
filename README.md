# ✈️ Runway Planner

Runway Planner is a constraint-based AI scheduler designed for students with
variable, lab-heavy academic timetables.

Unlike fixed timetable apps, this system dynamically generates daily schedules
based on real constraints such as college end time, sleep requirements, and
energy levels.

---

## 🚀 Features

- Constraint-based daily schedule generation
- Energy-aware task duration adjustment
- Guaranteed conflict-free planning
- Reward-gated leisure system (gaming unlocks after priority tasks)
- Stateful UI using Streamlit session management
- Human-in-the-loop scheduling logic

---

## 🧠 How It Works

The planner uses rule-based logic to:
1. Lock non-negotiable constraints (sleep, journaling, meals)
2. Respect fixed academic schedules
3. Allocate career, exercise, and leisure blocks dynamically
4. Compute schedules backward from sleep time to avoid clashes

This approach ensures explainable and deterministic planning behavior.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Datetime module

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
