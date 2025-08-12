import streamlit  as st
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import numpy as np


# configuracion pagina 
st.set_page_config(
    layout = 'wide'
)

# titulo Principal
st.title('Visual date of Vehicles')
st.markdown('Visuaizacíón de datos ')

car_data = pd.read_csv('vehicle_data.csv')
st.sidebar.title('Graph Vehicle')
st.download_button(
    label= 'Dowland dataset',
    data = car_data.to_csv(index =False),
    file_name= 'vehicles_us.csv')
st.sidebar.divider()
# Introducción 
with st.sidebar:
    intro = st.button(label='Dataset Introduction')
# Si el usuario presiona el botón
if intro:
    with st.expander('Dataset Introduction', expanded=True):
        st.markdown("""
        This dataset contains vehicle sale listings published between 2018 and 2019.
        It includes detailed information on price, technical specifications, condition,
        fuel type, color, transmission type, and other relevant attributes. It also records
        the posting date and the number of days each listing remained active.
        This data can be used to analyze trends in the automotive market, identify pricing patterns,
        and segment vehicles by characteristics such as brand, fuel type, or drivetrain.
        """)
st.divider()
with st.sidebar:
    info= st.button(label='Columns information')
if info:
    with st.expander('Columns information',expanded=False):
        st.markdown("""
                    - price: Vehicle sale price (in USD). - model_year: Vehicle’s model year . 
                    - model: Vehicle make and model.
                    - condition: Vehicle’s condition as stated by the seller.
                    - cylinders: Number of engine cylinders.
                    - fuel: Type of fuel used by the vehicle.
                    - odometer: Vehicle mileage, in miles.- transmission: Type of transmission (automatic, manual)
                    - type: Vehicle category
                    - paint_color: Vehicle’s exterior color
                    - is_4wd: Indicates if the vehicle has four-wheel drive
                    - date_posted: Exact date when the listing was posted.
                    - days_listed: Number of days the listing was active before removal.
                    - year_posted: Year the listing was posted.
                    - month_posted: Month the listing was posted.""")
# codigo para mostrar el data set
if st.sidebar.checkbox('Data preview'):
    st.write('Excel information of the DataFrame for vehicles')
    st.write(car_data)
st.sidebar.divider()

# Graphics  base un vehicle type 
with st.sidebar:
    slect_gra = st.header('Graph base on Vehicle type and qualities')
    graph_option = ['Vehicle type according transmission','Typer of vehicle that are 4wd', 'Vehicle type according of cylinder','How many type of vehicles has been launched in the years']
    graph_choice = st.selectbox('Chose a graph',graph_option)
    st.sidebar.divider()
st.header('Graph base on Vehicle type and qualities')
st.write('The graphics make a comparison base on the type of vehicles and the qualities')
if graph_choice == "Vehicle type according transmission":
    totales = car_data.groupby('type')['transmission'].value_counts().reset_index()
    fig = px.line(totales, x = 'type', y ='count', color= 'transmission')
    fig.update_layout(
        title = 'Vehicle type according transmission',
        xaxis_title = 'Vehicle type',
        yaxis_title = 'transmission'
    )

    st.plotly_chart(fig, use_container_width=True)
elif graph_choice == 'Typer of vehicle that are 4wd':
    type_4wd = car_data.groupby('type')['is_4wd'].count().reset_index()
    graph_choice == "Typer of vehicle that are 4wd"
    fig = px.bar(type_4wd, x ='type', y = 'is_4wd')
    fig.update_layout(
        title = 'Type of vehicle that are 4wd',
        xaxis_title = 'Vehicle type',
        yaxis_title = 'Is_4wd'
    )
    st.plotly_chart(fig, use_container_width=True)
elif graph_choice == 'Vehicle type according of cylinder':
# Pendiente
    type_cylinder = car_data.groupby('type')['cylinders'].value_counts(dropna=True).reset_index()
    fig = px.line(type_cylinder, x = 'type', y ='count', color = 'cylinders' )
    fig.update_layout(
        title = 'Types of cylinder according',
        xaxis_title = 'Vehicle type',
        yaxis_title = 'Cylinder'
    )
    st.plotly_chart(fig, use_container_width=True)

elif graph_choice == 'How many type of vehicles has been launched in the years':
    poste_type = car_data.groupby('type')['year_posted'].value_counts().reset_index()
    fig = px.line( poste_type,x ='type', y ='count', color='year_posted')
    fig.update_layout(
        title = 'Vehicle type posted in the years',
        xaxis_title = 'Vehicle type',
        yaxis_title = 'Vehicles posted (year)'
    )
    st.plotly_chart(fig, use_container_width=True)
# varianza precio 
his_odom = st.sidebar.checkbox('Histogram of odometer')
if his_odom:
    st.write('Creating a histogram for the car sales ads dataset')
    fig = px.histogram(car_data, x="odometer")
    fig.update_layout(
            title = 'Histogram of odometer', fontdict={'fontsize':20, 'fontweight':'bold', 'color':'black'},
            xaxis_title = 'Vehicle type',
            yaxis_title = 'transmission'
        )
    st.plotly_chart(fig, use_container_width=True)
hist_prices = st.sidebar.checkbox('Histogram of the prices')
price_distri = st.sidebar.checkbox('Price distribution')
if hist_prices:
    st.subheader('Histogram of the prices')
    fig = px.histogram(car_data, x="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
if price_distri:
    st.subheader('Price distribution')
    fig = px.box( car_data, x='month_posted', y='price')
    st.plotly_chart(fig, use_container_width=True)

year_posted = st.sidebar.radio('Select the year posted of the vehicles',['2018','2019'])

with st.container():
    col1, col2 = st.columns([1,2])
    with col1:
        if year_posted == '2018':
            st.divider()
            st.subheader('Information posted 2018')
            posted_2018 = car_data[car_data['year_posted']== 2018]
            inf_2018 = car_data.query('year_posted == 2018').groupby('model_year')['year_posted'].count().reset_index()
            median_2018 = np.mean(inf_2018['model_year'])
            st.metric(
            label='Mean',
            value='{}'.format(round(median_2018))
            )
            median_2018 = np.median(inf_2018['model_year'])
            st.metric(
                label='Median',
                value='{}'.format(round(median_2018))
            )
            varia_2018 = np.std(inf_2018['model_year'])
            st.metric(
                label='Deviation',
                value='{}'.format(round(varia_2018))
            )
        else:
            st.divider()
            st.subheader('Information posted 2019')
            posted_2019 = car_data[car_data['year_posted']== 2019]
            inf_2019 = car_data.query('year_posted == 2019').groupby('model_year')['year_posted'].count().reset_index()
            median_2019 = np.mean(inf_2019['model_year'])
            st.metric(
            label='Mean',
            value='{}'.format(round(median_2019))
            )
            median_2019 = np.median(inf_2019['model_year'])
            st.metric(
                label='Median',
                value='{}'.format(round(median_2019))
            )
            varia_2019 = np.std(inf_2019['model_year'])
            st.metric(
                label='Deviation',
                value='{}'.format(round(varia_2019))
            )
    with col2:
        # no coincide la grafica VER
        if year_posted  == '2018':
            posted_2018 = car_data.query('year_posted == 2018').groupby('model_year')['year_posted'].count().reset_index()
            posted_2018 = posted_2018.drop(posted_2018[posted_2018['model_year'] == 0].index)
            st.subheader('Year model of the vehicles that was posted in 2018')
            fig= px.line(posted_2018, x='model_year', y = 'year_posted')
            st.plotly_chart(fig, use_container_width=True)
        else:
            posted_2019 = car_data.query('year_posted == 2019').groupby('model_year')['year_posted'].count().reset_index()
            posted_2019 = posted_2019.drop(posted_2019[posted_2019['model_year'] == 0].index)
            st.subheader('Year model the vehicles that was posted in 2019')
            fig = px.line( posted_2019, x='model_year', y = 'year_posted')
            st.plotly_chart(fig, use_container_width=True)
            

opciones = list(car_data.columns)[:15]

st.sidebar.divider()
v = st.sidebar.multiselect(
    label="Choose maximum two options",
    options= opciones,
    max_selections= 2 
)
# botton para analizar 
analizar  = st.sidebar.button(
    label="Analizate"
)
st.sidebar.divider()
try:
    if analizar:
        fig = px.bar(car_data, x =v[0],y= v[1],title=f'{v[0]} vs {v[1]}')
        st.plotly_chart(fig, use_container_width=True)
except:
    st.write('Error The parameter that was chosen can match; select other parameter')

