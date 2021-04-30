import dash
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv("us_state_vaccinations.csv")
df2 = pd.read_csv("country_vaccinations_by_manufacturer.csv")
df3 = pd.read_csv("WHO-COVID-19-global-data.csv")

fig_hist = px.histogram(data_frame=df, x='date', y='total_vaccinations')
fig_hist2 = px.histogram(data_frame=df, x='date', y='people_fully_vaccinated')
#fig_hist.show()
#fig_hist2.show()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
PAGE_SIZE = 10

text = '''This dashboard provides an interactive visualization of the progress of the Covid-19 Vaccine since its deployment in December 2020.'''
textA = '''Users residing in the U.S. will gain a better understanding of how their state compares to others as well as how the U.S. compares to other countries.''' 
textB = '''The information is taken from the World Health Organization and Our World in Data.'''
textC = '''The dashboard below allows users to learn more about:'''

text1 = ''' - The total amount of vaccines deployed since January 2021 by state'''
text2 = ''' - The reported amount of fully vaccinated individuals in each state since the deployment'''
text3 = ''' - The total amount of vaccines deployed in various countries since January 2021'''
text4 = ''' - The breakdown in the types of vaccines received by individuals in the different countries over time'''
text5 = ''' - How reported Covid-19 cases and related deaths have changed since the deployment of the vaccine'''

instructions1 = '''Please select a state from the dropdown menu. The dashboard will update the graphs below to show the progress in total vaccines deployed and the reported number of individuals who are fully vaccinated in the state chosen over time. '''
instructions2 = '''Please select a country from the dropdown menu. The dashboard will update the graph below to show the progress in total vaccines deployed in that country over time. The pie chart will also update to show the breakdown in the type of vaccine administered to the individuals. When hovering over the histogram, the pie chart will update to show the vaccine breakdown at that point in time.'''
instructions3 = '''Please select a country from the dropdown menu. The dashboard will update the graphs below to show the number of reported Covid-19 cases and Covid-19 related deaths in the chosen country since the deployment of the vaccine.'''

app.layout=html.Div([
    html.Div([
        html.Div([html.Br(),
            html.H1("Covid-19 Vaccination Progress", style={'color':'#003B73', 'textAlign' : 'center'}),
            html.Blockquote('Individual MA705 Project | Kirsten Dionne', style={'textAlign': 'left'}),
            html.B('The Purpose of This Dashboard', style={'color':'#003B73', 'textAlign': 'left'}),
            html.Section(text, style={'textAlign': 'left'}),
            html.Section(textA),
            html.Section(textB),
            html.Section(textC),
            html.Section(text1),
            html.Section(text2),
            html.Section(text3),
            html.Section(text4),
            html.Section(text5),
        ]),
        html.Hr(),
        html.Div([html.B('The United States', style={'color':'#003B73', 'textAlign': 'left'}),
        html.Div([html.B('How to use this dashboard:', style={'color':'#003B73', 'textAlign': 'left'}),
        html.Div(instructions1),
        html.Br(),
        
        html.Label("Select a State: "),
    dcc.Dropdown(id='location',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df.location.unique())],
                 value='Massachusetts',
                 style={'width':'50%'},
            ),
    dcc.Graph(id='total-graph'
    ) ,
    dcc.Graph(id='full-graph', 
    ),
    ]),
    html.Div([
    html.Br(),
    html.Hr(),
    html.Div([html.B('The World', style={'color':'#003B73', 'textAlign': 'left'}),
    html.Div(instructions2),
    html.Br(),

    html.Label("Select a Country: "),
    dcc.Dropdown(id='country',
                 options=[{'label':x, 'value':x}
                          for x in sorted(df2.country.unique())],
                 value='United States',
                 style={'width':'50%'}
            ),
    dcc.Graph(id='type-graph', 
    style={'width':'50%'}
    ),
    html.Div(
    dcc.Graph(id='country-graph', clickData=None, hoverData=None,
                config={
                    'staticPlot': False,
                    'scrollZoom': True,
                    'doubleClick': 'reset',
                    'showTips': True,
                    'displayModeBar': False,
                    'watermark': True,
                },
    )    
),
    html.Br(),
    html.Div(instructions3),
    html.Br(),
    html.Label("Select a Country: "),
    html.Div([
        dcc.Dropdown(id='country-list',
        options=[{'label':x, 'value':x}
                for x in sorted(df3.place.unique())],
                value='United States of America',
                 style={'width':'50%'}),
        dcc.Graph(id='cases-graph'),
    html.Div(
        dcc.Graph(id='deaths-graph'),
    )]),
    html.Div([
        html.Hr(),
        html.B('References:', style={'color': '#003B73', 'textAlign': 'left'}),
        html.Section(['-Vaccination by state data: ',html.A('https://ourworldindata.org/us-states-vaccinations',
                        href='https://ourworldindata.org/us-states-vaccinations')]),
        html.Section(['-World vaccine data: ',html.A('https://www.kaggle.com/gpreda/covid-world-vaccination-progress',
                        href='https://www.kaggle.com/gpreda/covid-world-vaccination-progress')]),
        html.Section(['-World Covid cases data: ',html.A('https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths',
                        href='https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths')]),
        html.Section(['-Dash callbacks: ',html.A('https://dash.plotly.com/basic-callbacks',
                        href=' https://dash.plotly.com/basic-callbacks')]),
        html.Section(['-Dash Dropdown menus: ',html.A('https://dash.plotly.com/dash-core-components/dropdown',
                        href='https://dash.plotly.com/dash-core-components/dropdown')]),
        html.Br(),
        html.Footer('April 2020, Kirsten Dionne')]),
    html.Div([], style={'width': '5%', 'display':'inline-block'}),
    ])
])
])
])
])


@app.callback(
    Output(component_id='total-graph', component_property='figure'),
    Input(component_id='location', component_property='value')
)
def update_graph(value_state):
    #print(value_state)
    dff = df[df.location==value_state]
    fig = px.histogram(data_frame=dff, x='date', y='total_vaccinations', title="Total Vaccinations by State",
    labels={'date': 'Date', 'total_vaccinations':'Total Vaccinations'}, color_discrete_sequence=['red'])
    fig.update_layout(yaxis_title= "Total Vaccinations")
    return fig

@app.callback(
    Output(component_id='full-graph', component_property='figure'),
    Input(component_id='location', component_property='value')
)
def interactive_graphs(value_state):
    #print(value_state)
    dff = df[df.location==value_state]
    fig2 = px.histogram(data_frame=dff, x='date', y='people_fully_vaccinated', title="Number of Individuals Reported Fully Vaccinated",
    labels={'date': 'Date', 'people_fully_vaccinated':'Fully Vaccinated Individuals'}, color_discrete_sequence=['blue'])
    fig2.update_layout(yaxis_title= "Fully Vaccinated Individuals")
    return fig2

@app.callback(
    Output(component_id='country-graph', component_property='figure'),
    Input(component_id='country', component_property='value')
)

def update_graph2(value_country):
    #print(value_country)
    dff2 = df2[df2.country==value_country]
    fig3 = px.histogram(data_frame=dff2, x='day', y='total_vaccinations', title="Total Vaccinations by Country",
    labels={'day': 'Date', 'total_vaccinations': 'Total Vaccinations'}, color_discrete_sequence=['purple'])
    fig3.update_layout(yaxis_title= "Total Vaccinations")
    return fig3

@app.callback(
    Output(component_id='type-graph', component_property='figure'),
    Input(component_id='country-graph', component_property='hoverData'),
    Input(component_id='country', component_property='value')
)
def update_side_graph(hov_data, value_country):
    if hov_data is None:
        dff3 = df2[df2.country==value_country]
        dff3 = dff3[dff3.day == '4/27/2021']
        #print(dff3)
        fig4 = px.pie(data_frame=dff3, names='vaccine', values='total_vaccinations', title='Breakdown of Vaccinations on: 4/27/2021')
        return fig4
    else:
        #print(f'hover data: {hov_data}')
        dff3 = df2[df2.country==value_country]
        hov_date = hov_data['points'][0]['x']
        dff3 = dff3[dff3.day == hov_date]
        fig4 = px.pie(data_frame=dff3, names='vaccine', values='total_vaccinations', title=f'Vaccinations on: {hov_date}')
        return fig4

@app.callback(
    Output(component_id='cases-graph', component_property='figure'),
    Input(component_id='country-list', component_property='value')
)
def update_graph3(value_cases):
    dff4 = df3[df3.place==value_cases]
    fig5 = px.histogram(data_frame=dff4, x='period', y='New_cases', title='Reported New Cases of Covid-19 by Country',
    labels={'period':'Date', 'New_cases':'New Cases'}, color_discrete_sequence=['green'])
    fig5.update_layout(yaxis_title= "New Cases")
    return fig5

@app.callback(
    Output(component_id='deaths-graph', component_property='figure'),
    Input(component_id='country-list', component_property='value')
)
def update_graph4(value_deaths):
    dff5 = df3[df3.place==value_deaths]
    fig6 = px.histogram(data_frame=dff5, x='period', y='New_deaths', title="Reported Covid-19 Related Deaths",
    labels={'period':'Date', 'New_deaths':'Reported Deaths'}, color_discrete_sequence=['orange'])
    fig6.update_layout(yaxis_title= "Reported Deaths")
    return fig6

if __name__=='__main__':
    app.run_server(debug=True)