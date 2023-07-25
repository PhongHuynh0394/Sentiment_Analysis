import streamlit as st
import function as f

def generate_result(result, typeresult=''):
  result = round(result, 3)
  if result <= 0.45:
    if typeresult == 'text':
      st.markdown('# Negative 🥹')
      st.markdown(f'#### {result}')
    else:
      st.image('https://i.pinimg.com/564x/d8/ba/74/d8ba74b94d10b185ef0ed0bd82f6d395.jpg')
  elif result >= 0.55:
    if typeresult == 'text':
      st.markdown('# Positive 🥰')
      st.markdown(f'#### {result}')
    else:
      st.image('https://i.pinimg.com/564x/ac/75/8d/ac758d4580ef6e8684d2ac9756e92f55.jpg')
  else:
    if typeresult == 'text':
      st.markdown('# Neutral 😶')
      st.markdown(f'#### {result}')
    else:
      st.image('https://i.pinimg.com/736x/5b/79/ee/5b79eed7338f4bc04357365395b980a5.jpg')


#reccommend to input
def rec_input(type):
  # st.markdown('_Reccommend text to input:_')
  txt1 = 'It was the best of times'
  txt2 = 'It was the age of foolishness'
  txt3 = 'It was the spring of hope'
  txt = None

  genre = st.radio(
    "Reccommend text to input:",
    (txt1, txt2, txt3))

  if genre == txt1:
    txt = txt1
  elif genre == txt2:
    txt = txt2
  else: 
    txt = txt3
  
  userText = st.text_area('User Input', txt)
  
  if st.button('Predict'):
    # user type something
    if(userText != ''):
      st.balloons()
      col1, col2 = st.columns(2)
      with col1:
        result = f.predict(type, [userText]).tolist()
        generate_result(result[0][0],'text')
      with col2:
        result = f.predict(type, [userText]).tolist()
        generate_result(result[0][0],'')
    else:
      st.error("You didn't type anything", icon="🚨")
      
# show page
def renderPage():
    #st.title("😊😐 Sentiment Analysis 😕😡")
    st.title("Sentiment Analysis Of Social Media Comments 🤖")
    st.divider()
  
    st.subheader("User Input Text Analysis")
    st.text("")
    st.text("""Analyzing text data given by the user and find sentiments within it. \n
              Positive: Polarity >= 0.55 \n
              Neutral: Polarity in range 0.45 and 0.55 \n
              Negative Polarity <= 0.45\n
              Closer to 1 mean more positive and conversely """)
     
    st.text("")

    #choose type of model to analyze
    type = st.selectbox(
     'Choose models',
     ('Simple Neutral Net','Long Short Term Memory (LSTM)', 'Convolutional Neutral Net (CNN)'))
    st.text("")
  
    # reccommend if u don't want to input text
    rec_input(type)
    
    st.text("")