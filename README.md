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
├── assets/                    # Static assets (images, icons, etc.)
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

## 👨‍💻 Author

### Kevin Woods

Applied ML Engineer

AWS Certified AI Practitioner

AWS Machine Learning Certified Engineer – Associate

- 🔗 [GitHub: woodskevinj](https://github.com/woodskevinj)
