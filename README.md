# ✈️ Runway Planner

Runway Planner is a constraint-based AI scheduler designed for students with
variable, lab-heavy academic timetables.

Unlike fixed timetable apps, this system dynamically generates daily schedules
based on real constraints such as college end time, sleep requirements, energy
levels, and fatigue-aware rules inspired by aviation duty-time planning.

---

## 🚀 Features

- Constraint-based daily schedule generation
- Energy-aware task duration adjustment
- Fatigue-aware workload reduction (aviation-inspired)
- Guaranteed conflict-free planning
- Reward-gated leisure system (gaming unlocks after priority tasks)
- Stateful UI using Streamlit session management
- Explainable, deterministic scheduling logic (no black-box ML)

---

## 🧠 How It Works

The planner follows a rule-based planning pipeline:

1. Locks non-negotiable constraints (sleep, journaling, meals)
2. Respects fixed academic schedules
3. Detects late-duty fatigue based on college end time
4. Dynamically allocates career, exercise, and leisure blocks
5. Computes schedules backward from fixed sleep deadlines

This ensures realistic, sustainable schedules without time clashes.

---

## ✈️ Aviation-Inspired Design

The scheduler incorporates a fatigue-aware constraint inspired by
commercial aviation duty-time regulations.

If academic duties end late in the day, the system automatically
reduces workload to prevent over-scheduling, prioritizing safety and
sustainability over idealized plans.

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Datetime module

---

## ▶️ Run Locally

```bash
pip install streamlit
streamlit run app.py
