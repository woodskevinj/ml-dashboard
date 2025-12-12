# 📊 Personal ML / Dev Dashboard (Reflex)

A modern, interactive dashboard built entirely in **pure Python** using the **Reflex** framework (previously Pynecone).
This project demonstrates how to build clean internal tools without writing any frontend code, while still producing a polished React-based UI automatically.

The dashboard includes:

- KPI cards

- Weekly focus progress bar

- Example study session summaries

- Interactive task checklist

- Light/dark mode toggle

- Responsive layout

---

## 🚀 Features

### 🔧 Built with Pure Python

Reflex compiles Python component definitions into a full React/Next.js frontend — no HTML, CSS, or JS needed.

### 📈 Live Updating State

State changes (such as checking off tasks) automatically update the UI.

### 🎯 ML Journey Focus

This dashboard is structured around your real ML engineering workflow:

- Study blocks

- Project progress

- Task completion

- Weekly focus goals

---

## 📁 Project Structure

```bash
ml-dashboard/
│
├── ml_dashboard/
│   ├── __init__.py
│   ├── ml_dashboard.py        # Main dashboard UI & state logic
│
│
├── tests/
│   ├── test_ml_dashboard.py     # State logic tests (pytest)
│   └── conftest.py              # Ensures project root is importable
├── assets/                    # Static assets (images, icons, etc.)
|
|
├── .web/                      # Auto-generated Reflex frontend files
│
├── rxconfig.py                # Reflex project configuration
├── requirements.txt           # Python dependencies (includes Reflex)
├── venv/                      # Python virtual environment
│
└── README.md                  # Project documentation (this file)
```

## 🧱 requirements.txt

Because you installed Reflex via pip into a virtual environment, your `requirements.txt` should include at minimum:

```nginx
reflex
```

(You should **not** add Pydantic manually — Reflex installs and manages the correct version internally.)

If you want to pin a version:

```shell
reflex>=0.8.0
```

## 🛠️ Setup Instructions

### 1️⃣ Clone or create your project folder

```bash
mkdir ml-dashboard
cd ml-dashboard
```

### 2️⃣ Create and activate your virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
```

### 3️⃣ Install dependencies

Your `requirements.txt` should contain:

```nginx
reflex
```

Install them:

```bash
pip install -r requirements.txt
```

### 4️⃣ Initialize the Reflex project

```bash
reflex init
```

Select:

**✔️ Blank Reflex App**

This generates:

- `rxconfig.py`

- A package folder (e.g., `ml_dashboard/`)

- The default project skeleton

### 5️⃣ Replace the generated file with your dashboard

Open:

```bash
ml_dashboard/ml_dashboard.py
```

Replace its contents with our working dashboard code, which defines:

- `DashboardState`

- KPI cards

- Progress section

- Sessions summary

- Task list

- `index()` page

And registers it with:

```python
app = rx.App()
app.add_page(index, route="/", title="ML Dashboard")
```

### 6️⃣ Run the app

```bash
reflex run
```

Reflex will:

- Compile components

- Launch the backend on `http://0.0.0.0:8000`

- Serve the frontend at `http://localhost:3000/`

Open:

http://localhost:3000/

If you see a blank screen due to routing, ensure you are using `index()` as the root page.

---

## ⚠️ Notes / Tips

### ⚠️ Python 3.10 Warning

Reflex shows:

```vbnet
Warning: Reflex support for Python 3.10 is deprecated
```

The dashboard **still works**, but in future you should upgrade to **Python 3.11+** to avoid breakage.

### 🧹 Refreshing Frontend

If you see stale UI behavior:

- Hard reload: **Cmd + Shift + R**

- Open in incognito

- Delete `.web/` and rerun `reflex run` (Reflex rebuilds it automatically)

---

## 🧭 Pages & Navigation

This project is now a **multi-page Reflex application**, making it feel more like a real internal dashboard tool rather than a single static screen. Reflex automatically handles routing, rendering, and state updates across pages — all written in pure Python.

### Available Routes

| **Route** | **Page**           | **Description**                                                                                   |
| --------- | ------------------ | ------------------------------------------------------------------------------------------------- |
| /         | **Dashboard Home** | Main overview page: KPIs, weekly progress bar, sessions summary, task list, and navigation links. |
| /sessions | **Study Sessions** | A dedicated page showing your weekly study blocks and focus summaries.                            |
| /tasks    | **Tasks Page**     | Focused page for managing and toggling your development / ML tasks.                               |

---

## 📄 Page Structure Overview

### 🏠 Dashboard ( `/` )

The main page includes:

- Weekly KPI cards

- Progress bar toward weekly focus goal

- Overview of sessions

- Task list

- Mini navigation bar (Home, Sessions, Tasks)

This page acts as the central hub for your ML productivity tracking.

---

## 📚 Study Sessions Page ( `/sessions` )

This page provides a more focused view of:

- Each daily study block

- Minutes logged

- High-level study summaries

Useful for reviewing your week, planning improvements, or evaluating consistency.

It also includes simple navigation back to the Dashboard or Tasks page.

---

## 📝 Tasks Page ( `/tasks` )

A clean, dedicated view for:

- Reviewing daily ML / dev tasks

- Toggling tasks complete/incomplete

- Tracking overall productivity (open vs done tasks)

Like the other pages, it includes navigation back to the Dashboard and Sessions pages.

---

## 🔗 Navigation Experience

Navigation is done using Reflex’s built-in `<rx.link>` component, allowing for seamless client-side page transitions without reloading the entire app.

Example snippet used on the dashboard:

```python
rx.hstack(
    rx.link("Home", href="/"),
    rx.link("Sessions", href="/sessions"),
    rx.link("Tasks", href="/tasks"),
    spacing="4",
    padding_y="0.5rem",
)
```

This gives your app a lightweight “navbar” experience without adding frontend code or modifying templates.

---

## 🌐 App Routing Setup (for reference)

The pages are registered in `ml_dashboard/ml_dashboard.py` like so:

```python
app = rx.App()
app.add_page(index, route="/", title="ML Dashboard")
app.add_page(sessions_page, route="/sessions", title="Study Sessions")
app.add_page(tasks_page, route="/tasks", title="Tasks")
```

This explicitly maps page functions to routes, ensuring `/` renders the home dashboard even if Reflex defaults change in the future.

---

## 📌 Next Steps

Here are clean upgrade paths for when you want to expand the dashboard:

### 1️⃣ Add dynamic charts

Reflex supports Recharts (`line_chart`, `bar_chart`, etc.).
Once the app is stable, we can reintroduce live charts.

### 2️⃣ Add a real backend or database

Reflex can store persistent state with:

```bash
reflex db init
reflex db migrate
```

### 3️⃣ Create additional pages

Add pages like:

- `/projects`

- `/study`

- `/goals`

- `/dashboard/v2`

Just define new functions and register them with:

```python
app.add_page(my_page, route="/my-route")
```

### 4️⃣ Connect real ML metrics

Plug in:

- GitHub commit counts

- Study logs from a CSV

- Results from ML experiments

- ECS / Docker deployment stats

- Local GPU/CPU usage

All accessible directly from Python state.

---

## 🧪 Unit Tests

This project includes a lightweight **pytest** test suite to validate application logic in the `DashboardState` class.

Following a **Test-Driven Development (TDD)** mindset, core behaviors such as computed properties and state mutation events are covered by automated tests.

Unit tests currently validate:

- Weekly total minutes calculation

- Progress percentage (including capping at 100%)

- Task completion counters (`open_tasks`, `done_tasks`)

- Event methods (e.g., `toggle_taskX`) — coming next

Tests live inside the `tests/` directory:

```bash
ml-dashboard/
│
├── ml_dashboard/
│   ├── ml_dashboard.py
│   └── __init__.py
│
├── tests/
│   ├── test_ml_dashboard.py     # State logic tests (pytest)
│   └── conftest.py              # Ensures project root is importable
```

---

## 📦 Installing Test Dependencies

`pytest` is included in `requirements.txt`:

```bash
reflex==0.8.22
pytest
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Running the Test Suite

From the project root (with your virtual environment active):

```bash
python -m pytest
```

You should see an output similar to:

```bash
====================================== test session starts ======================================
collected 2 items

tests/test_ml_dashboard.py ..                                                              [100%]

======================================= 2 passed in 1.78s ======================================
```

---

## 🧩 Example Test (Current)

```python
from ml_dashboard.ml_dashboard import DashboardState

def test_total_minutes_default():
    state = DashboardState()
    assert state.total_minutes == 90 + 60 + 120 + 45 + 80 + 150 + 100

def test_progress_percent_capped_at_100():
    state = DashboardState(weekly_goal=100)
    assert state.progress_percent == 100

```

---

## 👨‍💻 Author

### Kevin Woods

Applied ML Engineer

AWS Certified AI Practitioner

AWS Machine Learning Certified Engineer – Associate

- 🔗 [GitHub: woodskevinj](https://github.com/woodskevinj)
