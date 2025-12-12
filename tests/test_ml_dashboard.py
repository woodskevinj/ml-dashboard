from ml_dashboard.ml_dashboard import DashboardState

def test_total_minutes_default():
    state = DashboardState()
    assert state.total_minutes == 645   # 90 + 60 + 120 + 45 + 80 + 150 + 100

def test_progress_percent_capped_at_100():
    # With a small weekly_goal, progress should be capped at 100
    state = DashboardState(weekly_goal=100)
    assert state.progress_percent == 100

def test_progress_percent_zero_goal_returns_zero():
    # Avoid division by zero: weekly_goal <= 0 should give 0%
    state = DashboardState(weekly_goal=0)
    assert state.progress_percent == 0

def test_progress_percent_negative_goal_returns_zero():
    # Negative goals are treated as 0% progress
    state = DashboardState(weekly_goal=-500)
    assert state.progress_percent == 0

def test_progress_percent_large_goal_less_than_100():
    # With a large goal, percentage should be < 100 and computed correctly
    state = DashboardState(weekly_goal=1000)
    # tota_minutes is 645, so expected = int(645 * 100 / 1000) = 64
    assert state.progress_percent == 64


# ----------- toggle_taskX tests -----------

def test_toggle_task1_flips_state():
    state = DashboardState()
    # default is False
    assert state.task1_done is False

    state.toggle_task1()
    assert state.task1_done is True

    state.toggle_task1()
    assert state.task1_done is False


def test_toggle_task2_flips_state():
    state = DashboardState()
    # default is True
    assert state.task2_done is True

    state.toggle_task2()
    assert state.task2_done is False

    state.toggle_task2()
    assert state.task2_done is True


def test_toggle_task3_flips_state():
    state = DashboardState()
    # default is False
    assert state.task3_done is False

    state.toggle_task3()
    assert state.task3_done is True

    state.toggle_task3()
    assert state.task3_done is False


def test_toggle_task4_flips_state():
    state = DashboardState()
    # default is False
    assert state.task4_done is False

    state.toggle_task4()
    assert state.task4_done is True

    state.toggle_task4()
    assert state.task4_done is False