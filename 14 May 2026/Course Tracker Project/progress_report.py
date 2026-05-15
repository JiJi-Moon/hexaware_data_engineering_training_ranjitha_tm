import pandas as pd
df = pd.read_csv("course_tracker_csv")
low_progress = df[df['completion_percentage'] < 50]
low_progress.to_csv("weekly_low_progress_report.csv", index=False)
print("pipeline executed successfully")
print("students flagged:", len(low_progress))
