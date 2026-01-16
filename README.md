# Runway Planner

Runway Planner is a scheduling tool powered by AI. It helps students manage their busy, lab-heavy class schedules.

Unlike fixed timetable apps, this system creates daily schedules on the fly. It considers real factors like college end time, sleep needs, energy levels, and rules about fatigue inspired by aviation duty-time planning.

## Features

- Daily schedule generation based on constraints
- Task duration adjustments that consider energy levels
- Workload reduction based on fatigue (inspired by aviation)
- Conflict-free planning
- Leisure system tied to rewards (activities unlock after priority tasks)
- User-friendly interface using Streamlit session management
- Clear scheduling logic (no black-box machine learning)

## How It Works

The planner uses a rule-based approach:

1. Locks in non-negotiable constraints like sleep, journaling, and meals
2. Follows fixed academic schedules
3. Recognizes late-duty fatigue based on when college ends
4. Allocates time for career, exercise, and leisure
5. Works backwards from fixed sleep deadlines to create schedules

This leads to realistic, sustainable schedules with no time clashes.

## Aviation-Inspired Design

The scheduler includes a fatigue-aware constraint modeled after commercial aviation duty-time regulations.

If academic activities finish late, the system automatically lessens the workload to prevent over-scheduling. It prioritizes safety and sustainability over idealized plans.

## Tech Stack

- Python
- Streamlit
- Datetime module

## Run Locally

```bash
pip install streamlit
streamlit run app.py
```
