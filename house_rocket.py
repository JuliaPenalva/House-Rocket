import pandas as pd
import numpy as np
import streamlit as st
from matplotlib import gridspec
import plotly.express as px
import plotly.figure_factory as ff
import warnings
warnings.simplefilter("ignore")

def database(path):
    data = pd.read_csv(path)

    return data

def show_results(data_buy):
    st.title("House Rocket - Analytics Insights")
    st.sidebar.image("images/small logo.jpg", use_column_width=True)

    # creating filters
    st.sidebar.title("Filters:")
    buy_type_filter = st.sidebar.multiselect("Buy type:", data_buy['buy_type'].unique(), default = data_buy['buy_type'].unique())
    minimum_profit = st.sidebar.slider("Minimum sell profit - per house:", min_value = int(data_buy['profit'].min()),
                                       max_value = int(data_buy['profit'].max()), value = int(data_buy['profit'].min()), step = int(data_buy['profit'].std()))
    max_price = st.sidebar.slider("Maximum house buy price - per house:", min_value = int(data_buy['price'].min()),
                                  max_value = int(data_buy['price'].max()), value = int(data_buy['price'].max()), step = int(data_buy['price'].std()))

    #applying filters
    if (buy_type_filter != []):
        data = data_buy.loc[data_buy['buy_type'].isin(buy_type_filter)]
    else:
        data = data.copy()

    desable_filters = st.sidebar.checkbox("Desable price and profit filters")

    if desable_filters:
        data = data.copy()
    else:
        data = data[(data['profit'] >= minimum_profit) & (data['price'] < max_price)]

    # initial statistics
    total_houses = '{:,}'.format((data['id'].shape[0]))
    total_profit = '${:,.2f}'.format(data['profit'].sum())

    c1, c2 = st.columns(2)
    c1.metric("Total houses:", total_houses)
    c2.metric("Total profit:", total_profit)

    # map
    fig = px.scatter_mapbox(data,
                            lat = 'lat',
                            lon = 'long',
                            zoom = 10,
                            color = 'buy_type',
                            size = 'price',
                            size_max= 15,
                            text= 'id',
                            mapbox_style= 'open-street-map')
    fig.update_layout(height = 600, margin = {'r':0, 't':0, 'b':0, 'l':0})
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)

    #table
    order_by = st.sidebar.selectbox("Order table by:", ( 'No specfic order', 'Highest profit', 'Highest margin', 'Lowest price', 'Lowest renovation cost'))
    if order_by == 'Highest profit':
        data = data.sort_values(by='profit', ascending = False)
    elif order_by == 'Highest margin':
        data = data.sort_values(by='margin', ascending = False)
    elif order_by == 'Lowest price':
        data = data.sort_values(by='price', ascending = True)
    elif order_by == 'Lowest renovation cost':
        data.sort_values(by='renovation_cost', ascending=True)
    else:
        data = data.copy()

    st.dataframe(data)

    @st.cache
    def convert(data):
        return data.to_csv().encode('utf-8')
    csv = convert(data)
    st.download_button(label = "Download table as CSV",
                       data = csv,
                       file_name = "house_selection.csv",
                       mime = 'text/csv')
    return None

if __name__ == '__main__':

    path = "data_buy.csv"
    data = database(path)

    show_results(data)
