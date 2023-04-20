from matplotlib.figure import figaspect
import streamlit as st
import pandas as pd # pip install pandas
from matplotlib import pyplot as plt #pip install matplotlib

st.set_option('deprecation.showPyplotGlobalUse', False)

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x ** 2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}

df= pd.DataFrame(data = data)

col = st.sidebar.selectbox("select a column ",df.columns)

mul = st.sidebar.multiselect("select a column ",df.columns)

plt.plot(df['num'],df[col],df[mul])

st.pyplot()