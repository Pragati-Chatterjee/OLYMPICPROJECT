import streamlit as st
import pandas as pd
import preprocessor,helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df)

st.sidebar.title("Olympics Analysis")
st.sidebar.image("data:image/jpeg;base64,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")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    st.sidebar.header("Medal Tally")
    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox("Select Year",years)
    selected_country = st.sidebar.selectbox("Select Country", country)

    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    if selected_year != 'Overall' and selected_country == 'Overall':
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " overall performance")
    if selected_year != 'Overall' and selected_country != 'Overall':
        st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
    st.table(medal_tally)

if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0] - 1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(editions)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Edition", y="region")
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df, 'Event')
    fig = px.line(events_over_time, x="Edition", y="Event")
    st.title("Events over the years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df, 'Name')
    fig = px.line(athlete_over_time, x="Edition", y="Name")
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    st.title("No. of Events over time(Every Sport)")
    fig,ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', 'Sport', 'Event'])
    ax = sns.heatmap(x.pivot_table(index='Sport', columns='Year', values='Event', aggfunc='count').fillna(0).astype('int'),
                annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.yearwise_medal_tally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    st.title(selected_country + " excels in the following sports")
    pt = helper.country_event_heatmap(df,selected_country)
    fig, ax = plt.subplots(figsize=(20, 20))
    ax = sns.heatmap(pt,annot=True)
    st.pyplot(fig)

    st.title("Top 10 athletes of " + selected_country)
    top10_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top10_df)

if user_menu == 'Athlete wise Analysis':
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'],y=temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=60)
    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)