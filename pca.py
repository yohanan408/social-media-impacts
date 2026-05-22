import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from eda import load_data

df = load_data("Teen_Mental_Health_Dataset.csv")
features = ['daily_social_media_hours', 'sleep_hours', 'academic_performance', 
            'stress_level', 'anxiety_level', 'addiction_level', 'physical_activity']

x = df[features]
y = df['depression_label'].astype(str) # Convert to string for discrete coloring

# Standardize
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# PCA
pca = PCA(n_components=2)
components = pca.fit_transform(x_scaled)

pca_df = pd.DataFrame(data=components, columns=['PC1', 'PC2'])
pca_df['Depression'] = y.values

loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

fig = px.scatter(pca_df, x='PC1', y='PC2', color='Depression',
                 color_discrete_map={'0': 'lightblue', '1': 'red'},
                 title='PCA Biplot: The Digital Distress Map',
                 labels={'PC1': 'PC1: Digital Strain & Grades', 
                         'PC2': 'PC2: Physiological Recovery'},
                 template='plotly_white', opacity=0.7)

for i, feature in enumerate(features):
    fig.add_shape(type='line', x0=0, y0=0, x1=loadings[i, 0]*5, y1=loadings[i, 1]*5,
                  line=dict(color="black", width=2))
    fig.add_annotation(x=loadings[i, 0]*5.5, y=loadings[i, 1]*5.5, 
                       text=feature, showarrow=False, font=dict(color="black"))

fig.show()
