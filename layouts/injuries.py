from dash import html, dcc
import dash_bootstrap_components as dbc
from datetime import datetime, date

def create_injuries_layout():
    """
    Crea el layout del dashboard de injuries (área no competitiva).
    Simula un sistema de gestión de lesiones para cumplir con los requisitos.
    """
    
    layout = dbc.Container([
        # Header del dashboard
        dbc.Row([
            dbc.Col([
                html.H1(
                    "Injuries Dashboard", 
                    className="text-center mb-4",
                    style={'color': '#f39c12'}
                ),
                html.Hr()
            ])
        ]),
        
        # Panel de control / Filtros
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H4("Analysis Filters", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dbc.Row([
                            # Selector de tipo de análisis
                            dbc.Col([
                                dbc.Label("Analysis Type:", html_for="injury-analysis-type"),
                                dcc.Dropdown(
                                    id="injury-analysis-type",
                                    options=[
                                        {"label": "🏥 General Injuries", "value": "general"},
                                        {"label": "🦵 Injuries by Region", "value": "body_part"},
                                        {"label": "📅 Temporal Trends", "value": "temporal"},
                                        {"label": "⚽ Injuries by Team", "value": "team"}
                                    ],
                                    value="general",
                                    className="mb-3",
                                    disabled=True 
                                )
                            ], md=3),
                            
                            # Selector de equipo
                            dbc.Col([
                                dbc.Label("Equipo:", html_for="injury-team-selector"),
                                dcc.Dropdown(
                                    id="injury-team-selector",
                                    placeholder="Todos los equipos...",
                                    className="mb-3",
                                    value="all"  # ← AGREGAR VALOR POR DEFECTO
                                )
                            ], md=3),
                            
                            # Selector de período
                            dbc.Col([
                                dbc.Label("Período:", html_for="injury-period"),
                                dcc.Dropdown(
                                    id="injury-period",
                                    options=[
                                        {"label": "Último mes", "value": "1m"},
                                        {"label": "Últimos 3 meses", "value": "3m"},
                                        {"label": "Últimos 6 meses", "value": "6m"},
                                        {"label": "Última temporada", "value": "season"},
                                        {"label": "Todo el historial", "value": "all"}
                                    ],
                                    value="season",  # ← CAMBIAR A 'season' POR DEFECTO
                                    className="mb-3"
                                )
                            ], md=3),
                            
                            # Botones de acción
                            dbc.Col([
                                dbc.Label("Actions:", html_for="injury-action-buttons"),
                                html.Div([
                                    dbc.Button(
                                        "🔄 Refresh",
                                        id="injury-refresh-button",
                                        color="primary",
                                        size="sm",
                                        className="me-2"
                                    ),
                                    dbc.Button(
                                        "📊 Export Report",
                                        id="injury-export-button",
                                        color="success",
                                        size="sm"
                                    )
                                ], className="d-grid gap-2")
                            ], md=3)
                        ])
                    ])
                ], className="mb-4")
            ])
        ]),
        
        # Métricas principales (KPIs)
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Injury Metrics", className="card-title"),
                        html.Div(id="injury-main-kpis")
                    ])
                ])
            ])
        ], className="mb-4"),
        
        # Sección de visualizaciones principales
        dbc.Row([
            # Gráfico de distribución de lesiones
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("Injury Distribution", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-injury-distribution",
                            children=[html.Div(id="injury-distribution-chart")],
                            type="default"
                        )
                    ])
                ])
            ], md=6),
            
            # Gráfico de tendencias temporales
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("Injury Trends", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-injury-trends",
                            children=[html.Div(id="injury-trends-chart")],
                            type="default"
                        )
                    ])
                ])
            ], md=6)
        ], className="mb-4"),
        
        # Sección de datos detallados
        dbc.Row([
            # Tabla interactiva de lesiones
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("Injury Records", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-injury-table",
                            children=[html.Div(id="injury-table-container")],
                            type="default"
                        )
                    ])
                ])
            ], md=8),
            
            # Panel de estadísticas por región corporal
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("Injuries by Region", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-injury-body-parts",
                            children=[html.Div(id="injury-body-parts-analysis")],
                            type="default"
                        )
                    ])
                ])
            ], md=4)
        ], className="mb-4"),
        
        # Gráfico de análisis de riesgos
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("Injury Risk Analysis", className="mb-0")
                    ]),
                    dbc.CardBody([
                        dcc.Loading(
                            id="loading-injury-risk",
                            children=[html.Div(id="injury-risk-analysis")],
                            type="default"
                        )
                    ])
                ])
            ])
        ], className="mb-4"),
        
        # Stores para datos
        dcc.Store(id="injury-data-store"),
        dcc.Store(id="injury-filters-store"),
        
        # Download component para reportes
        dcc.Download(id="download-injury-report")
        
    ], fluid=True, className="py-4")
    
    return layout