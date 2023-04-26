import streamlit as st
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

st.markdown("# Title")

data = [1,2,3,4,5]
st.line_chart(data)

bar = Bar()
bar.add_xaxis(['A','B','C'])
bar.add_yaxis("Example", [1,2,3])
bar.add_yaxis("Dummy", [0.5,1.2,1.3])

st_pyecharts(bar)
