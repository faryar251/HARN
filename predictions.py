import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
import pandas as pd
from tensorflow import keras
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from keras.preprocessing import image
from PIL import Image
import streamlit as st
st.set_page_config(layout="wide")

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://wallpaperbat.com/img/161069-neural-network-wallpaper.gif");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
#Function to load uploaded image
def load_image(image_file):
	img = Image.open(image_file)
	return img
# Function to check the image
@st.cache(ttl=48*3600)
def check():

    lr = keras.models.load_model('weights.hdf5')
    #Prediction Pipeline
    class Preprocessor(BaseEstimator, TransformerMixin):
        def fit(self,img_object):
            return self
        
        def transform(self,img_object):
            img_array = image.img_to_array(img_object)
            expanded = (np.expand_dims(img_array,axis=0))
            return expanded

    class Predictor(BaseEstimator, TransformerMixin):
        def fit(self,img_array):
            return self
        
        def predict(self,img_array):
            probabilities = lr.predict(img_array)
            predicted_class = ['P_Deficiency', 'Healthy', 'N_Deficiency', 'K_Deficiency'][probabilities.argmax()]
            return predicted_class

    full_pipeline = Pipeline([('preprocessor',Preprocessor()),
                            ('predictor',Predictor())])
    return full_pipeline

def output(full_pipeline,img):
   a=  img
   #a = img.decode('utf-8', 'ignore') 
   a= a.resize((224,224))
   predic = full_pipeline.predict(a)
   return(predic)

def main():
   # giving a title
    set_bg_hack_url()
    col1, col2 = st.columns(2)

    with col1:
        st.title('H.A.R.N.')
        st.subheader('Image Classification Using CNN for identifying Plant Nutrient Deficiencies')
        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        # code for Prediction
        prediction = ''

        # creating a button for Prediction

        if st.button('Predict'):
            if image_file is not None:
                # To See details
                with st.spinner('Loading Image and Model...'):
                    full_pipeline = check()
                file_details = {"filename":image_file.name, "filetype":image_file.type,"filesize":image_file.size}
                st.write(file_details)
                img = load_image(image_file)
                w=img.size[0]
                h=img.size[1]
                if w>h:
                    w=600
                    st.image(img,width=w)
                else:
                    w=w*(600.0/h)
                    st.image(img,width=int(w))
                with st.spinner('Predicting...'):
                    prediction = output(full_pipeline,img)
                st.success(prediction)
if __name__ == '__main__':
    main()