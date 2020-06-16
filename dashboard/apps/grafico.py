import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime as dt
from datetime import date, timedelta
from app import app
from dash.dependencies import Input, Output

colors = {
    'background': '#23272c',
    'text': 'black'
}

df = pd.read_csv('../data/dados_pe.csv', infer_datetime_format=True)
df['data'] = pd.to_datetime(df['data'])
current_year = 2020
columns = df.columns

layout = html.Div(
    children=[
        html.H1(
            children='Dados Pernambuco',
            style={'textAlign': 'center'}
        ),
        
        html.Div(
            'Compras de Respiradores',
            style={'textAlign': 'center'}
        ),

        html.Div(
            className="row ",
            style={'marginTop': 30, 'marginBottom': 15},
            children = [
                dcc.DatePickerRange(
                    id='my-date-picker',
                    min_date_allowed=df['data'].min(),
                    max_date_allowed=df['data'].max(),
                    initial_visible_month=dt(current_year,df['data'].max().month, 1),
                    start_date=df['data'].min(),
                    end_date=df['data'].max(),
                ),
            ],
        ),

        html.Div(
            style={'textAlign': 'center'},
            children=[
                dash_table.DataTable(
                    id='table',
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.assign(
                        **df.select_dtypes(['datetime']).astype(str).to_dict('list')
                    ).to_dict('records'),
                    style_header={'textAlign': 'center'},
                    style_data={'textAlign': 'left'}
                )
            ]
        )
])


def update_first_datatable(start_date, end_date):
    if start_date is not None:
        start_date = dt.strptime(start_date, '%Y-%m-%d')
        start_date_string = start_date.strftime('%Y-%m-%d')
    if end_date is not None:
        end_date = dt.strptime(end_date, '%Y-%m-%d')
        end_date_string = end_date.strftime('%Y-%m-%d')

    days_selected = (end_date - start_date).days

    df_by_date = df[(df['data'] >= start_date) & (df['data'] <= end_date)]
    data_df = df_by_date.assign(
        **df_by_date.select_dtypes(['datetime']).astype(str).to_dict('list')
    ).to_dict("rows")
    return data_df

@app.callback(Output('table', 'data'),
	[Input('my-date-picker', 'start_date'),
	 Input('my-date-picker', 'end_date')])
def update_data(start_date, end_date):
	data = update_first_datatable(start_date[:10], end_date[:10])
	return data