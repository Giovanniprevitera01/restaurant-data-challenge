import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Caricamento e preprocessing dati
df = pd.read_csv("data/transactions.csv", parse_dates=["Date"])
print(f"Righe prima: {len(df)}")
df = df.drop_duplicates().copy()
print(f"Righe dopo drop duplicates: {len(df)}")

df.columns = df.columns.str.strip().str.replace(" ", "_")
num_cols = ['Price', 'Tax', 'Tax_rate_%', 'Net_minus_tax', 'Amount', '#_guests']
for col in num_cols:
    df.loc[:, col] = pd.to_numeric(df[col], errors='coerce')

def get_kpi(data):
    total_sales = data['Price'].sum()
    avg_ticket = data.groupby('Transaction_ID')['Price'].sum().mean()
    num_transactions = data['Transaction_ID'].nunique()
    return total_sales, avg_ticket, num_transactions

# App Dash
app = dash.Dash(__name__)
server = app.server  # Per deploy

app.layout = html.Div([
    html.H1("🍽️ Restaurant Data Dashboard", style={'textAlign': 'center'}),

    html.Div([
        dcc.DatePickerRange(
            id='date-range',
            start_date=df['Date'].min(),
            end_date=df['Date'].max(),
            display_format='YYYY-MM-DD'
        ),
        dcc.Dropdown(
            id='category-filter',
            options=[{'label': cat, 'value': cat} for cat in df['Product_category'].unique()],
            multi=True,
            placeholder="Filtra per categoria prodotto"
        ),
        dcc.RadioItems(
            id='order-type',
            options=[
                {'label': 'Tutti', 'value': 'all'},
                {'label': 'Dine-in', 'value': 'Al_tavolo'},
                {'label': 'Takeaway/Delivery', 'value': 'Asporto/Delivery'}
            ],
            value='all',
            inline=True
        )
    ], style={'margin': '20px'}),

    html.Div(id='kpi-div', style={'display': 'flex', 'justifyContent': 'space-around'}),

    html.Div([
        dcc.Graph(id='daily-sales'),
        dcc.Graph(id='top-products'),
        dcc.Graph(id='top-revenue'),
        dcc.Graph(id='weekday-sales'),
        dcc.Graph(id='hourly-heatmap')
    ])
])

@app.callback(
    [Output('kpi-div', 'children'),
     Output('daily-sales', 'figure'),
     Output('top-products', 'figure'),
     Output('top-revenue', 'figure'),
     Output('weekday-sales', 'figure'),
     Output('hourly-heatmap', 'figure')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date'),
     Input('category-filter', 'value'),
     Input('order-type', 'value')]
)
def update_dashboard(start_date, end_date, categories, order_type):
    filtered = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]
    if categories:
        filtered = filtered[filtered['Product_category'].isin(categories)]
    if order_type != 'all':
        filtered = filtered[filtered['At_the_table_Takeaway/Delivery'] == order_type]

    total_sales, avg_ticket, num_transactions = get_kpi(filtered)
    kpi_children = [
        html.Div([html.H3("💰 Totale Vendite"), html.H4(f"€ {total_sales:,.2f}")]),
        html.Div([html.H3("📊 Scontrino Medio"), html.H4(f"€ {avg_ticket:,.2f}")]),
        html.Div([html.H3("🧾 Numero Transazioni"), html.H4(num_transactions)])
    ]

    fig_daily = px.line(filtered.groupby('Date')['Price'].sum().reset_index(),
                        x='Date', y='Price', title='Vendite giornaliere')

    top_products = filtered.groupby('Category_and_product_ID')['Amount'].sum().nlargest(10).reset_index()
    fig_top = px.bar(top_products, x='Amount', y='Category_and_product_ID', orientation='h',
                     title='Top 10 Prodotti più venduti (per nome)')

    top_revenue = filtered.groupby('Category_and_product_ID')['Price'].sum().nlargest(10).reset_index()
    fig_revenue = px.bar(top_revenue, x='Price', y='Category_and_product_ID', orientation='h',
                         title='Top 10 Prodotti per incasso (per nome)')

    weekday_sales = filtered.groupby(filtered['Date'].dt.day_name())['Price'].sum()
    weekday_sales = weekday_sales.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    fig_weekday = px.bar(weekday_sales, x=weekday_sales.index, y=weekday_sales.values,
                         title='Vendite per giorno della settimana')

    hourly_sales = filtered.copy()
    hourly_sales['Hour'] = hourly_sales['Date'].dt.hour
    hourly_pivot = hourly_sales.pivot_table(values='Price', index='Hour', columns=hourly_sales['Date'].dt.day_name(), aggfunc='sum', fill_value=0)
    fig_heatmap = px.imshow(hourly_pivot, labels=dict(x="Giorno", y="Ora", color="Vendite (€)"),
                            title='Heatmap vendite per ora e giorno')

    return kpi_children, fig_daily, fig_top, fig_revenue, fig_weekday, fig_heatmap

if __name__ == '__main__':
    app.run(debug=True)

