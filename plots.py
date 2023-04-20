import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns = ['a','b','c']
)

chart = alt.Chart(data).mark_circle().encode(
    x = 'a' , y = 'b' , tooltip = ['a','b']
)

# st.graphviz_chart("""
# digraph{
# watch -> like
# like -> share
# share -> subscribe
# share -> watch
# }
# """)

city = pd.DataFrame ({
    'awesome cities ' : ['Chicago ', 'Minneapolis ', 'Louisville', 'Topeka '],
    'lat ' : [41.868171 , 44.979840 , 38.257972 , 39.030575 ],
    'lon ' : [-87.667458 , -93.272474 , -85.765187 , -95.702548 ]
})

st.plotly_chart()

st.altair_chart(chart,use_container_width = True)

st.set_option('deprecation.showPyplotGlobalUse', False)
#for disabling the warning due to new terms in pyplot

plt.scatter(data['a'],data['b'])
plt.title('Scatter')
st.map(city)
st.pyplot()

st.line_chart(data)

st.area_chart(data)

st.bar_chart(data)