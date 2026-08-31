import json
import os


DATA_FILE = "buttons.json"


DEFAULT_BUTTONS = [
    {
        "name": "LOOK FIRST GAZE",
        "text": "=== LOOK FIRST GAZE ===",
    },
    {
        "name": "LOOK SECOND GAZE",
        "text": "=== LOOK SECOND GAZE ===",
    },
    {
        "name": "FIRE FALSE STAY",
        "text": "=== FIRE FALSE STAY ===",
    },
    {
        "name": "WATER FALSE MOVE",
        "text": "=== WATER FALSE MOVE ===",
    },
    {
        "name": "SPREAD 1",
        "text": "=== SPREAD 1 ===",
    },
    {
        "name": "SPREAD 2",
        "text": "=== SPREAD 2 ===",
    },
    {
        "name": "MOVE",
        "text": "=== MOVE ===",
    },
]


def load_buttons():
    if not os.path.exists(DATA_FILE):
        buttons = [button.copy() for button in DEFAULT_BUTTONS]
        save_buttons(buttons)
        return buttons

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            buttons = json.load(file)

        if not isinstance(buttons, list):
            raise ValueError("Invalid button data")

        valid_buttons = []

        for button in buttons:
            if not isinstance(button, dict):
                continue

            if "name" not in button or "text" not in button:
                continue

            valid_buttons.append(
                {
                    "name": str(button["name"]),
                    "text": str(button["text"]),
                }
            )

        return valid_buttons

    except (OSError, json.JSONDecodeError, ValueError):
        buttons = [button.copy() for button in DEFAULT_BUTTONS]
        save_buttons(buttons)
        return buttons


def save_buttons(buttons):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            buttons,
            file,
            indent=4,
            ensure_ascii=False,
        )