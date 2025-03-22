import dash
from dash import html, dcc
from dash import dash_table
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import requests

# Функция получения данных из NocoDB
def get_nocodb_data():
    url = "http://backend:8000/nocodb-data/"  # Замените на реальный URL вашего API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            records = data.get('records', [])
            print("Полученные данные:", records)
            cleaned_records = [
                {k: v for k, v in record.items() if not k.startswith('_nc_m2m_')}
                for record in records
            ]
            return pd.DataFrame(cleaned_records)
        else:
            print("Ошибка при получении данных:", response.status_code)
            return pd.DataFrame()
    except Exception as e:
        print(f"Ошибка соединения: {e}")
        return pd.DataFrame()

# Инициализация приложения Dash
app = dash.Dash(__name__)

# Базовый макет приложения
app.layout = html.Div([
    html.H1('User Dashboard'),
    dcc.Interval(
        id='interval-component',
        interval=1 * 1000,  # обновление каждую секунду при первой загрузке
        n_intervals=0,
        max_intervals=1   # выполняется только один раз при загрузке
    ),
    html.Div(id='dashboard-content')
])

# Callback для обновления содержимого при загрузке
@app.callback(
    Output('dashboard-content', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    # Получаем данные
    df = get_nocodb_data()

    # Проверяем, что DataFrame не пустой
    if df.empty:
        return html.P('Нет данных для отображения. Проверьте соединение с NocoDB.')

    # Преобразуем даты
    if 'CreatedAt' in df.columns:
        df['CreatedAt'] = pd.to_datetime(df['CreatedAt'])
    if 'UpdatedAt' in df.columns:
        df['UpdatedAt'] = pd.to_datetime(df['UpdatedAt'], errors='coerce')

    # Создаем визуализации
    change_columns = ['previous_value', 'new_value']
    if change_columns:
        fig_changes = px.line(df, 
                             x='timestamp', 
                             y=change_columns,
                             title='Изменение значений',
                             markers=True)
    else:
        fig_changes = px.line(title='Нет данных об изменениях')

    # Определяем колонки для таблицы
    table_columns = [
        {'name': 'ID', 'id': 'Id'},
        {'name': 'Change ID', 'id': 'change_id'},
        {'name': 'Тип изменения', 'id': 'change_type'},
        {'name': 'Предыдущее значение', 'id': 'previous_value'},
        {'name': 'Новое значение', 'id': 'new_value'},
        {'name': 'Время изменения', 'id': 'timestamp'},
        {'name': 'Создано', 'id': 'CreatedAt'},
        {'name': 'Обновлено', 'id': 'UpdatedAt'}
    ]

    # Возвращаем содержимое dashboard
    return [
        html.Div([
            html.H3('Общая статистика'),
            html.P(f"Тип изменений: {df['change_type'].unique()}"),
            html.P(f"Среднее изменение значения: {df['new_value'].mean() - df['previous_value'].mean():.2f}"),
        ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'}),
        
        html.Div([
            dcc.Graph(figure=fig_changes),
        ], style={'width': '65%', 'display': 'inline-block'}),
        
        html.Div([
            html.H3('Детальная информация'),
            dash_table.DataTable(
                data=df.to_dict('records'),
                columns=table_columns,
                style_table={'overflowX': 'auto'},
            )
        ])
    ]

# Запуск приложения
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)