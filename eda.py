import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from loguru import logger

def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        df = df[df["physical_activity"] < 1.0]
        return df
    
    except Exception as e:
        logger.error('path {} : {} does not exist', path, e)

def summarize(df):
    summary_df = df.groupby(['social_interaction_level', 'depression_label']).size().reset_index(name='count')
    summary_df['percent'] = summary_df.groupby('social_interaction_level')['count'].transform(lambda x: (x / x.sum() * 100).round(1))
    return summary_df

def numerical(df):
    numerical_columns = df.drop(columns=["depression_label"])
    numerical_columns = numerical_columns.select_dtypes('number')
    return numerical_columns

def melted_df(df, features):
    df_melted = df.melt(id_vars=['depression_label'], value_vars=features, 
                        var_name='Feature', value_name='Value')
    return df_melted


def plot_countplot(df):
    sns.countplot(x = "gender", data = df, hue = "gender")

def depression_plot(df):
    sns.countplot(x = "depression_label", data = df, hue = "gender")

def media_platform(df):
    sns.countplot(x = "platform_usage", data = df, hue = "depression_label")

def plot_scatter(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))

    sns.scatterplot(
        x="daily_social_media_hours", 
        y="sleep_hours", 
        hue="depression_label", 
        size="age", 
        sizes=(50, 500),
        alpha=0.6,
        palette={0: "#3498db", 1: "#e74c3c"}, 
        data=df
    )

    plt.ylim(3.5, 10.5)
    plt.xlim(-0.5, 10.5)

    plt.axvline(x=6, color='gray', linestyle='--', alpha=0.5)
    plt.text(6.2, 9.5, "Usage Threshold (>6 hrs)", color='gray', fontsize=10, rotation=270)

    plt.axhline(y=6, color='gray', linestyle='--', alpha=0.5)
    plt.text(0.5, 6.2, "Sleep Threshold (<6 hrs)", color='gray', fontsize=10)

    #HIGHLIGHT THE DANGER ZONE
    plt.fill_between(x=[6, 10], y1=0, y2=6, color='red', alpha=0.05, label="Danger Zone")

    plt.annotate(
        'The "Danger Zone"', 
        xy=(8, 4.5),           
        xytext=(2, 2.5),
        arrowprops=dict(
            facecolor='black', 
            shrink=0.05, 
            width=1.5, 
            headwidth=8,
            connectionstyle="arc3,rad=.2"
        ),
        fontsize=11, 
        fontweight='bold', 
        color='#c0392b'
    )


    # Labels and Legend
    plt.title("The Biological Tax: Threshold Mapping of Adolescent Risk", fontsize=16, fontweight='bold', pad=20)
    plt.xlabel("Daily Social Media Usage (Hours)", fontsize=12)
    plt.ylabel("Daily Sleep Duration (Hours)", fontsize=12)

    plt.legend()

    plt.tight_layout()
    plt.show()

def plot_scatterplot(df):
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))

    sns.scatterplot(
        x="daily_social_media_hours", 
        y="sleep_hours", 
        hue="depression_label", 
        size="addiction_level", 
        sizes=(50, 500),
        alpha=0.6,
        palette={0: "#3498db", 1: "#e74c3c"}, 
        data=df
    )

    plt.ylim(3.5, 10.5)
    plt.xlim(-0.5, 10.5)


    plt.axvline(x=6, color='gray', linestyle='--', alpha=0.5)
    plt.text(6.2, 9.5, "Usage Threshold (>6 hrs)", color='gray', fontsize=10, rotation=270)

    plt.axhline(y=6, color='gray', linestyle='--', alpha=0.5)
    plt.text(0.5, 6.2, "Sleep Threshold (<6 hrs)", color='gray', fontsize=10)

    # HIGHLIGHT THE DANGER ZONE
    plt.fill_between(x=[6, 10], y1=0, y2=6, color='red', alpha=0.05, label="Danger Zone")

    plt.annotate(
        'The "Danger Zone"', 
        xy=(8, 4.5),
        xytext=(2, 2.5),
        arrowprops=dict(
            facecolor='black', 
            shrink=0.05, 
            width=1.5, 
            headwidth=8,
            connectionstyle="arc3,rad=.2" # Adds a slight curve to the arrow
        ),
        fontsize=11, 
        fontweight='bold', 
        color='#c0392b'
    )


    # Labels and Legend
    plt.title("The Biological Tax: Threshold Mapping of Adolescent Risk", fontsize=16, fontweight='bold', pad=20)
    plt.xlabel("Daily Social Media Usage (Hours)", fontsize=12)
    plt.ylabel("Daily Sleep Duration (Hours)", fontsize=12)

    plt.legend()


    plt.tight_layout()
    plt.show()

def bar_plot(summary):
    fig = px.bar(summary, 
                x="social_interaction_level", 
                y="percent", 
                color="depression_label",
                text=summary['percent'].apply(lambda x: f'{x}%'),
                hover_data=['count'],
                title="Depression Risk: Percentage and Count by Social Level",
                category_orders={"social_interaction_level": ["low", "medium", "high"]},
                color_discrete_map={0: "darkblue", 1: "yellow"},
                template="plotly_white")

    fig.show()

def recovery_vs_arousal(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Plot 1: Sleep
    sns.kdeplot(data=df, x="sleep_hours", hue="gender", fill=True, ax=ax1)
    ax1.axvspan(0, 5, color='red', alpha=0.1) # Shading the danger zone
    ax1.set_title("The 'Recovery Gap' (Sleep)")

    # Plot 2: Usage
    sns.kdeplot(data=df, x="daily_social_media_hours", hue="gender", fill=True, ax=ax2)
    ax2.axvspan(6, 10, color='red', alpha=0.1) # Shading the high-usage zone
    ax2.set_title("The 'Arousal Surplus' (Social Media)")

    plt.tight_layout()
    plt.show()

def distribution(df, numerical_df):

    fig, axes = plt.subplots(3, 3, figsize=(15, 15))
    axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

    for i, column in enumerate(numerical_df.columns):
        
        sns.kdeplot(data = df, x = column, ax = axes[i], hue = "gender")

def plot_pair(df):
    sns.pairplot(df, hue = "depression_label")

def box_plot(df_melted):
    # Melting the dataframe makes it easier to plot all features at once with one command
    
    fig = px.box(df_melted, 
                x="Value", 
                y="Feature", 
                color="depression_label",
                points="all",
                notched=True,
                title="Impact of Lifestyle Factors on Depression Status",
                height=1000, 
                template="plotly_white")

    fig.update_layout(boxmode='group')
    fig.show()

def box(df):
    fig = px.scatter(df, 
                 x="daily_social_media_hours", 
                 y="sleep_hours", 
                 color="depression_label",
                 color_discrete_map={0: "blue", 1: "red"},
                 marginal_x="box",
                 marginal_y="box",
                 title="The High-Risk Zone: Sleep vs. Social Media",
                 labels={"daily_social_media_hours": "Daily Social Media (Hours)", 
                         "sleep_hours": "Sleep Duration (Hours)"},
                 template="plotly_white",
                 opacity=0.7)

    fig.update_xaxes(range=[-0.5, 10.5])
    fig.update_yaxes(range=[-0.5, 10.5])

    fig.show()

def run_pipeline(path):
    df = load_data(path)
    summary = summarize(df)
    plot_countplot(df)
    plot_scatterplot(df)
    bar_plot(summary)
    plot_scatter(df)
    numerical_df = numerical(df)
    depression_plot(df)
    media_platform(df)
    distribution(df, numerical_df)
    plot_pair(df)
    box(df)
    recovery_vs_arousal(df)
    df_melted = melted_df(df, features = ['daily_social_media_hours', 'sleep_hours', 'screen_time_before_sleep', 
            'academic_performance', 'physical_activity', 'stress_level', 'anxiety_level'])
    box_plot(df_melted)

if __name__ == "__main__":
    run_pipeline("Teen_Mental_Health_Dataset.csv")