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
    total_points = st.slider("Number of points in Cardioid spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in Cardioid spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = (5 - 5 * math.sin(angle)) * curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))
        
    

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
    
   



"""

**Astroid spiral**

Astroid spiral is shining like a star :star:


"""

with st.echo(code_location='below'):
    total_points2 = st.slider("Number of points in Astroid spiral", 1, 10000, 2000, key = 2)
    num_turns2 = st.slider("Number of turns in Astroid spiral", 1, 100, 11, key = 3)
    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn2 = total_points2 / num_turns2

    for curr_point_num2 in range(total_points2):
        curr_turn2, i = divmod(curr_point_num2, points_per_turn2)
        angle2 = (curr_turn2 + 1) * 2 * math.pi * i / points_per_turn2
        radius2 = curr_point_num2 / total_points2
        x = radius2 * math.cos(angle2) ** 3
        y = radius2 * math.sin(angle2) ** 3
        data.append(Point(x, y))
        
    

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
 
"""

**Hypotrochoid spiral**

Hypotrochoid spiral 


"""

with st.echo(code_location='below'):
    total_points3 = st.slider("Number of points in Hypotrochoid spiral", 1, 10000, 2000, key = 4)
    num_turns3 = st.slider("Number of turns in Hypotrochoid spiral", 1, 100, 11, key = 5)
    angle32 = st.number_input("Second angle in Hypotrochoid spiral", key = 6)
    radius32 = st.number_input("Second radius in Hypotrochoid spiral", min_value=0, key = 7)
    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn3 = total_points3 / num_turns3

    for curr_point_num3 in range(total_points3):
        curr_turn3, i = divmod(curr_point_num3, points_per_turn3)
        angle31 = (curr_turn3 + 1) * 2 * math.pi * i / points_per_turn3
        radius3 = curr_point_num3 / total_points3
        x = radius31 * math.cos(angle31) + radius32 * math.cos(angle32)
        y = radius31 * math.sin(angle31) + radius32 * math.sin(angle32)
        data.append(Point(x, y))
        
    

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    
    

