import dash
import dash_html_components as html

app = dash.Dash(__name__, server=app)
app.layout = html.Div("Hello from Dash!")

if __name__ == '__main__':
    app.run_server(debug=True)
