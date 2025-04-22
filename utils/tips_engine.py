# --- utils/tips_engine.py ---
import numpy as np


def get_water_saving_tips():
    tips = [
        "Fix leaking taps to save up to 200 liters/day.",
        "Turn off the tap while brushing to save 6 liters per minute.",
        "Use a bucket instead of a hose for washing cars.",
        "Install low-flow showerheads to cut water usage by 30%.",
        "Collect rainwater for gardening.",
    ]
    return np.random.choice(tips)