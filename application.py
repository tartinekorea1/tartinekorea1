import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
application = app.server

app.layout = html.Div(children=[
			html.H1(children='&Beyond Tartine'),
			html.Div(children='Dash app running on Azure'),
			dcc.Graph(
				id='example1',
				figure={
					'data': [
							{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                					{'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            					],
					'layout': {
						'title': 'Dash Data Visualization'
					}
				}
			)
])

if __name__ == '__main__':
	application.run(debug=True, host='0.0.0.0', port='8000')
