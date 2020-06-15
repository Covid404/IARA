import dash_core_components as dcc
import dash_html_components as html

colors = {
    'background': '#23272c',
    'text': '#a3a7b0'
}

layout = html.Div(
    children=[
        html.H1(
            children='Home',
            style={'textAlign': 'center'}
        ),
        
        html.Div(
            'Um Plot Aleatório',
            style={'textAlign': 'center'}
        ),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'chart', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'chart', 'name': u'Montréal'},
                ],
                'layout': {
                    'title': 'Visualização Plot Aleatório',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        ),
])
