
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title='Solar Radiation Dashboard', layout='wide')


st.header('Upload your CSV and Plot Data')

uplod_files = st.file_uploader('Choose File', type='csv')

if uplod_files is not None:
    df =pd.read_csv(uplod_files)
    st.subheader('Upload Data Preview')
    st.dataframe(df.head(5))

st.subheader('Grapho of Radiation Data')
if st.checkbox('Show Plot'):
    if df.shape[1]>=2:
        x_col = st.selectbox('Select X-axis Column', df.columns )
        y_col = st.selectbox('Select Y-axis Column', df.columns )

        fig, ax = plt.subplots(figsize=(8,2))
        ax.plot(df[x_col], df[y_col], marker='o', color='b')
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        ax.set_title(f'{x_col} Vs {y_col}')
        st.pyplot(fig)
    else:
        st.warning('Uploaded files must have at least 3 columns')
else:
    st.warning('Please Upload CSV files')