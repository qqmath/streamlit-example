from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
This article shows different types of spirals in an interactive way. 

**Cardioid spiral**

Cardioid spiral is now on Streamlit to your heart's desire :heart:



"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        #angle = np.linspace(0, 2*np.pi, 1000) / points_per_turn
        #radius = curr_point_num / total_points
        radius = (5 - 5 * math.sin(angle)) * curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))
        
    

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
    
   



"""

 Astroid spiral

Astroid spiral is shining like a star :star:


"""

with st.echo(code_location='below'):
    total_points2 = st.slider("Number of points in spiral", 1, 5000, 2000, key = 2)
    num_turns2 = st.slider("Number of turns in spiral", 1, 100, 9, key = 3)
    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn2 = total_points2 / num_turns2

    for curr_point_num2 in range(total_points2):
        curr_turn2, i = divmod(curr_point_num2, points_per_turn2)
        angle2 = (curr_turn2 + 1) * 2 * math.pi * i / points_per_turn2
        #angle = np.linspace(0, 2*np.pi, 1000) / points_per_turn
        #radius = curr_point_num / total_points
        radius2 = (5 - 5 * math.sin(angle2)) * curr_point_num2 / total_points2
        x = radius2 * math.cos(angle2) * math.cos(angle2) * math.cos(angle2)
        y = radius2 * math.sin(angle2) * math.sin(angle2) * math.sin(angle2)
        data.append(Point(x, y))
        
    

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500, key = 4)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
    

