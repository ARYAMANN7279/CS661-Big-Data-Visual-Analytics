import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from tabs import overview, genre, country, company

import warnings
warnings.filterwarnings("ignore")

# Initialize Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)
app.title = "Cinescope Dash App"

# ✅ Register callbacks from each tab
overview.register_callbacks(app)
genre.register_callbacks(app)
country.register_callbacks(app)
company.register_callbacks(app)

# Define the main app layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.Div([
        html.H2("Navigation Window", className="sidebar-title"),
        html.Hr(),
        dcc.Link("Overview Tab", href="/overview", className="sidebar-link"),
        html.Br(),
        dcc.Link("Genre Tab", href="/genre", className="sidebar-link"),
        html.Br(),
        dcc.Link("Country Tab", href="/country", className="sidebar-link"),
        html.Br(),
        dcc.Link("Company Tab", href="/company", className="sidebar-link"),
    ], className="sidebar"),

    html.Div(id='page-content', className="content")
])

# Route different tabs
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname in ['/', '/overview']:
        return overview.layout() if callable(overview.layout) else overview.layout
    elif pathname == '/genre':
        return genre.layout() if callable(genre.layout) else genre.layout
    elif pathname == '/country':
        return country.layout() if callable(country.layout) else country.layout
    elif pathname == '/company':
        return company.layout() if callable(company.layout) else company.layout
    else:
        return html.H3("404: Page not found. Please use the sidebar to navigate.")

if __name__ == '__main__':
    app.run(debug=True)
