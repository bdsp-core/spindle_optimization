import numpy as np
import pandas as pd
import plotly.express as px

# file paths
fluid_p = '../data/fluid_cog_raw_data.csv'
df = pd.read_csv(fluid_p)

# parallel coordinates
slow = df[df.fc<13]
fast = df[df.fc>13]

df_plot=[df, slow, fast][0]
dms = ['fc','cycles', 'th', 'minT', 'merge','q', 'maxT']

fig = px.parallel_coordinates(df_plot, color="pearson_corr",
                              labels={"pearson_corr": "pearson r"},
                              dimensions=dms,
                              color_continuous_scale=px.colors.sequential.Rainbow) 
                 
fig.show()


