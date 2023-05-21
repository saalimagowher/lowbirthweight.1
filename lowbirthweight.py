# libraries
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from PIL import Image
# data loading
df=pd.read_csv('birthweight.csv')
# update variable
df.lwt=df.lwt/2.205
# subset to remove level
df=df[ (df['ptl'] < 3) & (df['ftv'] < 6)]
#changing to factor
df['low']=df['low'].astype(object)
df['race']=df['race'].astype(object)
df['smoke']=df['smoke'].astype(object)
df['ptl']=df['ptl'].astype(object)
df['ht']=df['ht'].astype(object)
df['ui']=df['ui'].astype(object)
df['ftv']=df['ftv'].astype(object)
# mutate condition
df['low']=np.where((df['low']==0),'No','Yes')
           
df['smoke']=np.where((df['smoke']==0),'No','Yes')

df['ht']=np.where((df['ht']==0),'No','Yes')

df['ui']=np.where((df['ui']==0),'No','Yes')

df['race']=np.where((df['race']==1),'White',
           np.where((df['race']==2),'Black',
           'Other'))

st.title('Low Birth Weight Analysis')
def home():
    st.subheader("Welcome to low birth weight data presentation")
    image = Image.open('baby.png')
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        st.image(image, caption='Birthweight') 
    with col3:
        st.write("")
def data():
    st.header('Header of Dataframe')
    st.write(df.head())
def per():
    st.header("Age,Race & Birthweight")
    fig = px.scatter(df, x='age', y='bwt', facet_col='race', color='race')
    st.plotly_chart(fig,use_container_width=True)
    a=df.groupby(['age','race'])['bwt'].aggregate(['count','mean','median','min', 'max'])
    st.dataframe(a,width=1000)
          
def hl():
    tab1, tab2 = st.tabs(["Weight", "Other"])

    with tab1:
        st.header("Weight, Hypertension,Smoke & Birthweight")
        fig = px.scatter(df, x='lwt', y='bwt', color='smoke', facet_col='ht')
        st.plotly_chart(fig,use_container_width=True)
        lsh=df.groupby(['lwt','smoke', 'ht'])['bwt'].aggregate(['count','mean','median','min', 'max'])
        st.dataframe(lsh,width=1000)
    
    
    with tab2:   
        options=st.selectbox('select the variable', ['first trimister visit', 'preterm labor', 'uterine infection'])
        if options == 'first trimister visit':
            ftv_plot()
        elif options == 'preterm labor':
            ptl_plot()
        else:
            ui_plot()

    
def ftv_plot():
    st.subheader("Birthweight based on first trimister visit")
    fig = px.box(df, x='ftv', y='bwt', color='ftv')
    st.plotly_chart(fig,use_container_width=True)
    ftv= df.groupby("ftv")["bwt"].agg({'count','mean','median','min', 'max'})
    st.dataframe(ftv,width=1000) 
          
def ptl_plot():
    st.subheader("Birthweight based on preterm labour")
    fig = px.box(df, x='ptl', y='bwt', color='ptl')
    st.plotly_chart(fig,use_container_width=True)
    ptl= df.groupby("ptl")["bwt"].agg({'count','mean','median','min', 'max'})
    st.dataframe(ptl,width=1000)
    
def ui_plot():
    st.subheader("Birthweight based on uterine infection")
    fig = px.box(df, x='ui', y='bwt', color='ui')
    st.plotly_chart(fig,use_container_width=True)
    ui= df.groupby("ui")["bwt"].agg({'count','mean','median','min', 'max'})
    st.dataframe(ui,width=1000)
    
    
def rep():
    st.header("REPORT")
    st.write(" Not a low birth weight:")
    st.write("1. Irrespective of age distribution of birth weight is above the low weight in white mothers compare to black and other")
    st.write(" 2.Birth weight of a baby is likely to increase when the weight of mother increase.")
    st.write(" 3. Mother's who don't have hypertension likely to have increased birth weight of a baby.")
    st.write(" 4. Mother's who don’t smoke likely to have normal to high birth weight of a baby.")
    st.write(" 5. Birth weight of baby is more when mother has no uterine infection.")
    st.write(" 6. Mother who visits a single physician is  likely to have a more birth weight compare to mother who does not visits to a                   physician.")

    st.write(" Low birth weight:")
    st.write("1. The mother  who smoke likely to have decrease in birth weight of baby compare to mothers who don't smoke.")
    st.write("2. Birth weight of baby is likely  low when the mother has experienced once or twice a preterm labor compare to no preterm                   labors")
    st.write("3. We can see that there is a decrease in birth weight when the mother has uterine irritability during pregnancy.")
    
st.sidebar.title('Navigation')
side = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Header', 'Personal Info', "Health Info", "Report"])
if side == 'Home':
 home()
elif side == 'Data Header':
 data()
elif side == 'Personal Info':
 per()
elif side == 'Health Info':
 hl()
elif side == 'Report':
 rep()

