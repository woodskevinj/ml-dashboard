import reflex as rx


# ---------- State ----------

class DashboardState(rx.State):
    """App state for the ML / Dev dashboard."""

    # Weekly goal for focus minutes.
    weekly_goal: int = 600

    # Minutes per day (no lists, just simple ints).
    mon_minutes: int = 90
    tue_minutes: int = 60
    wed_minutes: int = 120
    thu_minutes: int = 45
    fri_minutes: int = 80
    sat_minutes: int = 150
    sun_minutes: int = 100

    # Simple task flags.
    task1_done: bool = False
    task2_done: bool = True
    task3_done: bool = False
    task4_done: bool = False

    # ---- Computed vars ----

    @rx.var
    def total_minutes(self) -> int:
        return (
            self.mon_minutes
            + self.tue_minutes
            + self.wed_minutes
            + self.thu_minutes
            + self.fri_minutes
            + self.sat_minutes
            + self.sun_minutes
        )

    @rx.var
    def progress_percent(self) -> int:
        if self.weekly_goal <= 0:
            return 0
        pct = int(self.total_minutes * 100 / self.weekly_goal)
        return min(100, max(0, pct))

    @rx.var
    def open_tasks(self) -> int:
        return sum(
            [
                not self.task1_done,
                not self.task2_done,
                not self.task3_done,
                not self.task4_done,
            ]
        )

    @rx.var
    def done_tasks(self) -> int:
        return sum(
            [
                self.task1_done,
                self.task2_done,
                self.task3_done,
                self.task4_done,
            ]
        )

    # ---- Events ----

    def toggle_task1(self):
        self.task1_done = not self.task1_done

    def toggle_task2(self):
        self.task2_done = not self.task2_done

    def toggle_task3(self):
        self.task3_done = not self.task3_done

    def toggle_task4(self):
        self.task4_done = not self.task4_done


# ---------- UI helpers ----------

def kpi_card(label: str, value, subtext: str = "") -> rx.Component:
    """Reusable KPI/stat card."""
    return rx.card(
        rx.vstack(
            rx.text(label, size="2", weight="medium", color="gray"),
            rx.heading(value, size="6"),
            rx.text(subtext, size="1", color="gray"),
            spacing="1",
            align_items="flex-start",
        ),
        size="3",
        width="100%",
    )


def kpi_row() -> rx.Component:
    """Top KPIs row."""
    return rx.grid(
        kpi_card(
            "Deep-work minutes (week)",
            DashboardState.total_minutes.to_string(),
            "Target: " + DashboardState.weekly_goal.to_string() + " mins",
        ),
        kpi_card(
            "Study sessions",
            "7",
            "Mon–Sun focus blocks",
        ),
        kpi_card(
            "Tasks open",
            DashboardState.open_tasks.to_string(),
            "Things left for today",
        ),
        kpi_card(
            "Tasks done",
            DashboardState.done_tasks.to_string(),
            "Completed items",
        ),
        columns="4",
        spacing="4",
        width="100%",
    )


def progress_section() -> rx.Component:
    """Progress bar toward weekly goal."""
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading("Weekly Focus Progress", size="4"),
                rx.spacer(),
                rx.text(
                    DashboardState.progress_percent.to_string() + "% of goal",
                    size="2",
                    color="gray",
                ),
                align_items="center",
                width="100%",
            ),
            rx.progress(
                value=DashboardState.progress_percent,
                height="10px",
                radius="full",
            ),
            rx.text(
                DashboardState.total_minutes.to_string()
                + " / "
                + DashboardState.weekly_goal.to_string()
                + " minutes logged",
                size="2",
                color="gray",
            ),
            spacing="3",
            width="100%",
        ),
        size="3",
        width="100%",
    )


def sessions_section() -> rx.Component:
    """Simple 'sessions' summary without tables/foreach."""
    return rx.card(
        rx.vstack(
            rx.heading("Study Sessions (Example Week)", size="4"),
            rx.vstack(
                rx.hstack(
                    rx.text("Mon", weight="medium", width="60px"),
                    rx.text("90 min · Customer Churn EDA"),
                ),
                rx.hstack(
                    rx.text("Tue", weight="medium", width="60px"),
                    rx.text("60 min · Reflex docs + experiments"),
                ),
                rx.hstack(
                    rx.text("Wed", weight="medium", width="60px"),
                    rx.text("120 min · VisionSense API tests"),
                ),
                rx.hstack(
                    rx.text("Thu", weight="medium", width="60px"),
                    rx.text("45 min · ML theory / reading"),
                ),
                rx.hstack(
                    rx.text("Fri", weight="medium", width="60px"),
                    rx.text("80 min · UrbanShift uplift ideas"),
                ),
                rx.hstack(
                    rx.text("Sat", weight="medium", width="60px"),
                    rx.text("150 min · MLE-Agent refactor"),
                ),
                rx.hstack(
                    rx.text("Sun", weight="medium", width="60px"),
                    rx.text("100 min · Paper writing / review"),
                ),
                spacing="2",
                width="100%",
            ),
            spacing="3",
            width="100%",
        ),
        size="3",
        width="100%",
    )


def task_list() -> rx.Component:
    """Interactive task checklist using only simple bool vars."""
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading("Today’s Tasks", size="4"),
                rx.spacer(),
                rx.text(
                    DashboardState.open_tasks.to_string()
                    + " open · "
                    + DashboardState.done_tasks.to_string()
                    + " done",
                    size="2",
                    color="gray",
                ),
                align_items="center",
                width="100%",
            ),
            rx.vstack(
                # Task 1
                rx.hstack(
                    rx.checkbox(
                        is_checked=DashboardState.task1_done,
                        on_change=DashboardState.toggle_task1,
                    ),
                    rx.text(
                        "Finish SHAP explainability notebook",
                        size="2",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                # Task 2
                rx.hstack(
                    rx.checkbox(
                        is_checked=DashboardState.task2_done,
                        on_change=DashboardState.toggle_task2,
                    ),
                    rx.text(
                        "Refine customer churn README",
                        size="2",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                # Task 3
                rx.hstack(
                    rx.checkbox(
                        is_checked=DashboardState.task3_done,
                        on_change=DashboardState.toggle_task3,
                    ),
                    rx.text(
                        "Add tests to VisionSense API",
                        size="2",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                # Task 4
                rx.hstack(
                    rx.checkbox(
                        is_checked=DashboardState.task4_done,
                        on_change=DashboardState.toggle_task4,
                    ),
                    rx.text(
                        "Sketch next AI agent architecture",
                        size="2",
                    ),
                    spacing="2",
                    align_items="center",
                ),
                spacing="2",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        size="3",
        width="100%",
    )


# ---------- Page layout ----------

def index() -> rx.Component:
    """Home dashboard page."""
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.container(
                rx.vstack(
                    # Header
                    rx.vstack(
                        rx.text("Applied ML Journey", size="2", color="gray"),
                        rx.heading("Personal ML / Dev Dashboard", size="7"),
                        rx.text(
                            "Track focus time and tasks – all in pure Python with Reflex.",
                            size="2",
                            color="gray",
                        ),
                        spacing="2",
                        align_items="flex-start",
                    ),
                    # Simple nav
                    rx.hstack(
                        rx.link("Home", href="/"),
                        rx.link("Sessions", href="/sessions"),
                        rx.link("Tasks", href="/tasks"),
                        spacing="4",
                        padding_y="0.5rem",
                    ),
                    # Main content
                    kpi_row(),
                    progress_section(),
                    rx.grid(
                        sessions_section(),
                        task_list(),
                        columns="2",
                        spacing="4",
                        width="100%",
                    ),
                    spacing="6",
                    width="100%",
                ),
                max_width="1200px",
                padding_y="2rem",
            ),
        ),
        min_height="100vh",
        bg="gray.1",
        padding_x="1rem",
    )


def sessions_page() -> rx.Component:
    """Dedicated page for study sessions."""
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.container(
                rx.vstack(
                    rx.vstack(
                        rx.text("Applied ML Journey", size="2", color="gray"),
                        rx.heading("Study Sessions", size="7"),
                        rx.text(
                            "Overview of your focused work blocks for the week.",
                            size="2",
                            color="gray",
                        ),
                        spacing="2",
                        align_items="flex-start",
                    ),
                    rx.hstack(
                        rx.link("← Back to Dashboard", href="/"),
                        rx.spacer(),
                        rx.link("Tasks", href="/tasks"),
                        spacing="4",
                        width="100%",
                    ),
                    sessions_section(),
                    spacing="6",
                    width="100%",
                ),
                max_width="900px",
                padding_y="2rem",
            ),
        ),
        min_height="100vh",
        bg="gray.1",
        padding_x="1rem",
    )


def tasks_page() -> rx.Component:
    """Dedicated page for task management."""
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.container(
                rx.vstack(
                    rx.vstack(
                        rx.text("Applied ML Journey", size="2", color="gray"),
                        rx.heading("Today’s Tasks", size="7"),
                        rx.text(
                            "Manage your ML / dev tasks and track completion.",
                            size="2",
                            color="gray",
                        ),
                        spacing="2",
                        align_items="flex-start",
                    ),
                    rx.hstack(
                        rx.link("← Back to Dashboard", href="/"),
                        rx.spacer(),
                        rx.link("Sessions", href="/sessions"),
                        spacing="4",
                        width="100%",
                    ),
                    task_list(),
                    spacing="6",
                    width="100%",
                ),
                max_width="900px",
                padding_y="2rem",
            ),
        ),
        min_height="100vh",
        bg="gray.1",
        padding_x="1rem",
    )


# ---------- App wiring ----------

app = rx.App()
app.add_page(index, route="/", title="ML Dashboard")
app.add_page(sessions_page, route="/sessions", title="Study Sessions")
app.add_page(tasks_page, route="/tasks", title="Tasks")

# def index() -> rx.Component:
#     return rx.box(
#         rx.color_mode.button(position="top-right"),
#         rx.center(
#             rx.container(
#                 rx.vstack(
#                     rx.vstack(
#                         rx.text("Applied ML Journey", size="2", color="gray"),
#                         rx.heading("Personal ML / Dev Dashboard", size="7"),
#                         rx.text(
#                             "Track focus time and tasks – all in pure Python with Reflex.",
#                             size="2",
#                             color="gray",
#                         ),
#                         spacing="2",
#                         align_items="flex-start",
#                     ),
#                     kpi_row(),
#                     progress_section(),
#                     rx.grid(
#                         sessions_section(),
#                         task_list(),
#                         columns="2",
#                         spacing="4",
#                         width="100%",
#                     ),
#                     spacing="6",
#                     width="100%",
#                 ),
#                 max_width="1200px",
#                 padding_y="2rem",
#             ),
#         ),
#         min_height="100vh",
#         bg="gray.1",
#         padding_x="1rem",
#     )


# # ---------- App wiring ----------

# app = rx.App()
# app.add_page(index, route="/", title="ML Dashboard")