import streamlit as st
import pandas as pd
import scraping as scr
import function as func
import plotly.graph_objects as go
import plotly.express as px


def plot_label_distribution(df):
  # Count the number of occurrences of each label
  label_counts = df['Label'].value_counts()
  # Create a bar chart to visualize the label distribution
  fig1 = px.bar(x=label_counts.index, y=label_counts.values, labels={'x': 'Label', 'y': 'Count'},
                title='Label Distribution')

  # Calculate the percentage of each label
  label_ratios = label_counts / len(df) * 100
  # Create a pie chart to visualize the label ratios
  fig2 = px.pie(values=label_ratios.values, names=label_ratios.index, title='Label Ratios')
  col1, col2 = st.columns(2)

  with col1:
    st.plotly_chart(fig1, use_container_width=True)
  with col2:
    st.write('')
    st.dataframe(label_counts, use_container_width=True)

  col1, col2 = st.columns(2)
  with col1:
    st.plotly_chart(fig2, use_container_width=True)
  with col2:
    st.write('')
    st.dataframe(label_ratios, use_container_width=True)
  return label_ratios, label_counts

#function create df from link
def create_df(url=None):
  list_comments = scr.crawl_youtube_comments(url)

  #using the best model to analyze (CNN) (if you want to change model, replace the name)
  model = ['Simple Neutral Net','Long Short Term Memory (LSTM)', 'Convolutional Neutral Net (CNN)']
  polarity = func.predict(model[2], list_comments)
  polarity = [sentiment[0] for sentiment in polarity]
  label = []
  for _ in polarity:
    if _ <= 0.45:
      label.append("Negative")
    elif _ >= 0.55:
      label.append("Positive")
    else:
      label.append("Neutral")
  result = pd.DataFrame({'Comments': list_comments,'Polarity': polarity, 'Label': label})

  st.markdown("## All result")
  st.dataframe(result, use_container_width=True)
  #down csv
  down_csv(result)

  st.markdown('## Detail')
  label_ratios, label_counts = plot_label_distribution(result)
  label_detail = st.selectbox(
   'Label query',
   ('Positive','Negative', 'Neutral'))
  st.text("")
  if label_detail == 'Positive':
    st.write(f'Total number of {label_detail}: {label_counts.iloc[0]}')
    st.dataframe(result.query("Label == 'Positive'"), use_container_width=True)
  if label_detail == 'NeuTral':
    st.write(f'Total number of {label_detail}: {label_counts.iloc[2]}')
    st.dataframe(result.query("Label == 'Neutral'"),use_container_width=True)
  if label_detail == 'Negative':
    st.write(f'Total number of {label_detail}: {label_counts.iloc[1]}')
    st.dataframe(result.query("Label == 'Negative'"), use_container_width=True)

  


# convert dataframe to csv file
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

#download file csv
def down_csv(csv):
  csv = convert_df(csv)
  st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

# show page
def renderPage():
  #st.title("😊😐 Sentiment Analysis 😕😡")
  st.title("Sentiment Analysis Of Social Media Momments 🤖")
  st.divider()
    # st.markdown("### User Input Text Analysis")
  st.subheader("Commercial Experience Insights")
  st.text("")
  st.markdown("In this section, the main idea relies on an emotion analysis model, which analyze the emotion rate from a comments on Youtube video.")
  st.text("")
  #input link
  url = st.text_input('User Input', placeholder='Input URL HERE')

  if url:
    create_df(url)

  