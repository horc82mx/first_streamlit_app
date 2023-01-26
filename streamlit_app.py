import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Buid Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# streamlit.dataframe(my_fruit_list)

# Let´s put a pick list here so they can pick the fruit they want to include
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
# streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')

# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
# streamlit.dataframe(my_fruit_list)

# Let´s put a pick list here so they can pick the fruit they want to include
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page
# streamlit.dataframe(my_fruit_list)

# Let´s put a pick list here so they can pick the fruit they want to include
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
# streamlit.dataframe(fruits_to_show)

# Let´s put a pick list here so they can pick the fruit they want to include --- Change values of the picker
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

# Al cambiar valores de Avocado y Strawberries por Banana y Grapes muestra este error
# File "/app/first_streamlit_app/streamlit_app.py", line 41
# streamlit.dataframe(fruits_to_show)
# ^
# IndentationError: unexpected indent

# Let´s put a pick list here so they can pick the fruit they want to include --- Change values of the picker
# fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Banana','Grapes'])
# fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
# streamlit.dataframe(fruits_to_show)
