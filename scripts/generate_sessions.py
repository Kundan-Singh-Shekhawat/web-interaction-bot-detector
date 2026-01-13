import random
import pandas as pd

# Generate human sessions
def generate_human_session():
    return {
        "avg_time_between_events": random.uniform(0.5, 4.0),
        "std_time_between_events": random.uniform(0.2, 1.5),
        "events_per_minute": random.randint(10, 40),
        "session_duration": random.randint(60, 600),
        "unique_pages": random.randint(3, 15),
        "repeat_ratio": random.uniform(0.1, 0.4),
        "mouse_event_ratio": random.uniform(0.4, 0.8),
        "scroll_event_ratio": random.uniform(0.2, 0.6),
        "label": 0
    }

# Generate bot sessions
def generate_bot_session():
    return {
        "avg_time_between_events": random.uniform(0.05, 0.4),
        "std_time_between_events": random.uniform(0.01, 0.1),
        "events_per_minute": random.randint(60, 300),
        "session_duration": random.randint(30, 300),
        "unique_pages": random.randint(1, 4),
        "repeat_ratio": random.uniform(0.6, 0.95),
        "mouse_event_ratio": random.uniform(0.0, 0.05),
        "scroll_event_ratio": random.uniform(0.0, 0.1),
        "label": 1
    }

# Generate fast human
def generate_fast_human_session():
    return {
        "avg_time_between_events": random.uniform(0.3, 0.8),
        "std_time_between_events": random.uniform(0.1, 0.6),
        "events_per_minute": random.randint(40, 70),
        "session_duration": random.randint(60, 300),
        "unique_pages": random.randint(2, 8),
        "repeat_ratio": random.uniform(0.3, 0.6),
        "mouse_event_ratio": random.uniform(0.2, 0.5),
        "scroll_event_ratio": random.uniform(0.1, 0.4),
        "label": 0
    }

# Generate stealth bots
def generate_stealth_bot_session():
    return {
        "avg_time_between_events": random.uniform(0.3, 1.0),
        "std_time_between_events": random.uniform(0.1, 0.5),
        "events_per_minute": random.randint(20, 60),
        "session_duration": random.randint(120, 600),
        "unique_pages": random.randint(3, 10),
        "repeat_ratio": random.uniform(0.3, 0.6),
        "mouse_event_ratio": random.uniform(0.05, 0.2),
        "scroll_event_ratio": random.uniform(0.05, 0.3),
        "label": 1
    }


# Dataset generator

def generate_dataset(
    n_human=700,
    n_fast_human=300,
    n_bot=700,
    n_stealth_bot=300
):
    data = []

    for _ in range(n_human):
        data.append(generate_human_session())

    for _ in range(n_fast_human):
        data.append(generate_fast_human_session())

    for _ in range(n_bot):
        data.append(generate_bot_session())

    for _ in range(n_stealth_bot):
        data.append(generate_stealth_bot_session())

    return pd.DataFrame(data)

# Save in csv format

if __name__ == "__main__":
    df = generate_dataset()
    df.to_csv("data/raw/sessions.csv", index=False)
    print(df.head())