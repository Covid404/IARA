import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import grafico, quem_somos


app.layout = html.Div([
    html.Nav(
        className='navbar navbar-expand-lg navbar-dark bg-dark',
        children=[
            html.Div(
                className='collapse navbar-collapse',
                id='navbarNav',
                children=[
                    html.Div(
                        className='navbar-nav',
                        children=[
                            html.A(
                                'Home',
                                className='nav-item nav-link',
                                href='/'
                            ),
                            html.A(
                                'Quem somos',
                                className='nav-item nav-link',
                                href='/quem_somos'
                            ),
                        ]
                    )
                ]
            )
        ]
    ),
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', className='container')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return grafico.layout
    elif pathname == '/quem_somos':
        return quem_somos.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)