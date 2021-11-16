#To study the performance of the student with the ID TRL_987
import csv
import plotly.graph_objects as og
import pandas as pd

df = pd.read_csv("data.csv")
student_df = df.loc[df["student_id"] == "TRL_987"]
print(student_df.groupby("level")["attempt"].mean())


fig = og.Figure(og.Bar(
    x = student_df.groupby("level")["attempt"].mean(), 
    y = ["level 1", "level 2", "level 3", "level 4"],
    orientation = "h"
))
fig.show()