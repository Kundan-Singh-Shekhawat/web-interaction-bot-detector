import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("data/raw/sessions.csv")

# Basic inspection
print("First few rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nClass distribution:")
print(df["label"].value_counts())

# Features to visualize
features = [
    "avg_time_between_events",
    "events_per_minute",
    "repeat_ratio",
    "mouse_event_ratio",
    "scroll_event_ratio"
]

# Plot distributions
for feature in features:
    plt.figure(figsize=(6, 4))
    sns.histplot(
        data=df,
        x=feature,
        hue="label",
        bins=30,
        kde=True,
        stat="density",
        common_norm=False
    )
    plt.title(f"Distribution of {feature}")
    plt.xlabel(feature)
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()