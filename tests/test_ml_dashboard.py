from ml_dashboard.ml_dashboard import DashboardState

def test_total_minutes_default():
    state = DashboardState()
    assert state.total_minutes == 90 + 60 + 120 + 45 + 80 + 150 + 100

def test_progress_percent_capped_at_100():
    state = DashboardState(weekly_goal=100)
    assert state.progress_percent == 100

