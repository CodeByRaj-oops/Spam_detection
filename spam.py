import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st
data=pd.read_csv('spam.csv')
data.drop_duplicates(inplace=True)

data['Category'] = data['Category'].map({
    'ham': 'not spam',
    'spam': 'spam'
})

mes=data['Message']
cat=data['Category']
(mes_train,mes_test,cat_train,cat_test)= train_test_split(mes,cat,test_size=0.2,random_state=42,stratify=cat)

cv=CountVectorizer(stop_words="english")
feature_mes=cv.fit_transform(mes_train)

model=MultinomialNB()
model.fit(feature_mes,cat_train)

feature_test=cv.transform(mes_test)
print(model.score(feature_test,cat_test))

def predict_message(message):
    input_message = cv.transform([message])
    result = model.predict(input_message)[0]
    return (result)

print(predict_message("Hey, are we still meeting at 5 pm today?"))

st.header("Spam Detection")
input_mess=st.text_input("enter message here")
if st.button('validate'):
    ot=predict_message(input_mess)
    st.markdown(ot)