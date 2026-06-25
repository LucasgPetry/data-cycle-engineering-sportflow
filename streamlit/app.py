import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import pandas as pd
import streamlit as st

from src.common.postgres import get_postgres_engine

import plotly.express as px

def render_footer():
    st.divider()

    st.caption(
        "SportFlow Analytics • Data Warehouse Esportivo • Camada Gold"
    )

st.set_page_config(
    page_title="SportFlow Analytics",
    layout="wide",
)

PRIMARY_COLOR = "#2563EB"
SECONDARY_COLOR = "#10B981"
BACKGROUND_COLOR = "#0F172A"
CARD_COLOR = "#111827"
TEXT_COLOR = "#F8FAFC"
MUTED_TEXT_COLOR = "#94A3B8"


st.markdown(
    f"""
    <style>
        .stApp {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}

        section[data-testid="stSidebar"] {{
            background-color: #020617;
        }}

        h1, h2, h3 {{
            color: {TEXT_COLOR};
            font-weight: 700;
        }}

        p, span, label {{
            color: {TEXT_COLOR};
        }}

        div[data-testid="stMetric"] {{
            background-color: {CARD_COLOR};
            padding: 1.2rem;
            border-radius: 16px;
            border: 1px solid rgba(148, 163, 184, 0.18);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
        }}

        div[data-testid="stMetricLabel"] {{
            color: {MUTED_TEXT_COLOR};
        }}

        div[data-testid="stMetricValue"] {{
            color: {TEXT_COLOR};
            font-weight: 700;
        }}

        .stDataFrame {{
            border-radius: 14px;
            overflow: hidden;
        }}

        div[data-baseweb="select"] > div {{
            background-color: {CARD_COLOR};
            border-radius: 10px;
        }}

        .stButton > button {{
            background-color: {PRIMARY_COLOR};
            color: white;
            border-radius: 10px;
            border: none;
            padding: 0.5rem 1rem;
            font-weight: 600;
        }}

        .stButton > button:hover {{
            background-color: #1D4ED8;
            color: white;
            border: none;
        }}

        hr {{
            border-color: rgba(148, 163, 184, 0.2);
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    # ⚽ SportFlow Analytics

    <span style="color:#94A3B8;">
    Plataforma analítica para exploração de dados esportivos
    utilizando arquitetura Data Lakehouse com SportsMonks,
    MinIO, PostgreSQL, Apache Airflow e Streamlit.
    </span>
    """,
    unsafe_allow_html=True,
)


@st.cache_data
def load_table(query: str):
    engine = get_postgres_engine()
    return pd.read_sql(query, con=engine)


competitions = load_table("SELECT * FROM gold.dim_competitions")
teams = load_table("SELECT * FROM gold.dim_teams")
seasons = load_table("SELECT * FROM gold.dim_seasons")
fixtures = load_table("SELECT * FROM gold.fact_fixtures")
standings = load_table("SELECT * FROM gold.fact_standings")

pipeline_logs = load_table(
    """
    SELECT
        pipeline_name,
        layer,
        records_processed,
        status,
        message,
        executed_at
    FROM gold.pipeline_execution_log
    ORDER BY executed_at DESC
    """
)


page = st.sidebar.selectbox(
    "Navegação",
    [
        "Overview",
        "Classificação",
        "Partidas",
        "Times",
        "Competições",
        "Temporadas",
        "Monitoramento"
    ],
)

st.sidebar.divider()

if st.sidebar.button("🔄 Atualizar Dados"):
    st.cache_data.clear()
    st.rerun()


if page == "Overview":
    st.header("Visão Geral")

    total_competitions = len(competitions)
    total_teams = len(teams)
    total_seasons = len(seasons)
    total_fixtures = len(fixtures)
    total_standings = len(standings)

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Competições", total_competitions)
    col2.metric("Times", total_teams)
    col3.metric("Temporadas", total_seasons)
    col4.metric("Partidas", total_fixtures)
    col5.metric("Classificações", total_standings)

    st.divider()

    st.subheader("Top 10 Times por Pontuação")

    standings_with_teams = standings.merge(
        teams[
            [
                "team_id",
                "team_name",
            ]
        ],
        left_on="participant_id",
        right_on="team_id",
        how="left",
    )

    standings_with_teams["team_label"] = standings_with_teams[
        "team_name"
    ].fillna(
        standings_with_teams["participant_id"].astype(str)
    )

    top_standings = (
        standings_with_teams
        .groupby("team_label")["points"]
        .max()
        .reset_index()
        .sort_values("points", ascending=False)
        .head(10)
    )

    st.bar_chart(
        top_standings,
        x="team_label",
        y="points",
    )

    st.subheader("Partidas por Competição")

    fixtures_with_competitions = fixtures.merge(
        competitions[
            [
                "competition_id",
                "competition_name",
            ]
        ],
        left_on="league_id",
        right_on="competition_id",
        how="left",
    )

    fixtures_with_competitions["competition_label"] = (
        fixtures_with_competitions["competition_name"]
        .fillna(
            fixtures_with_competitions["league_id"].astype(str)
        )
    )

    fixtures_by_competition = (
        fixtures_with_competitions
        .groupby("competition_label")
        .size()
        .reset_index(name="total")
        .sort_values("total", ascending=False)
    )

    st.bar_chart(
        fixtures_by_competition,
        x="competition_label",
        y="total",
    )

    st.divider()

    render_footer()


elif page == "Competições":
    st.header("Competições")

    total_competitions = len(competitions)
    active_competitions = competitions["active"].sum()
    total_types = competitions["type"].nunique()
    total_countries = competitions["country_id"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Competições", total_competitions)
    col2.metric("Ativas", int(active_competitions))
    col3.metric("Tipos", total_types)
    col4.metric("Países", total_countries)

    st.divider()

    type_options = sorted(
        competitions["type"].dropna().unique()
    )

    selected_type = st.selectbox(
        "Tipo",
        options=["Todos"] + list(type_options),
    )

    filtered = competitions.copy()

    if selected_type != "Todos":
        filtered = filtered[
            filtered["type"] == selected_type
        ]

    st.subheader("Tabela de Competições")

    st.dataframe(
        filtered[
            [
                "competition_id",
                "competition_name",
                "country_id",
                "type",
                "sub_type",
                "active",
                "last_played_at",
            ]
        ].sort_values("competition_name"),
        use_container_width=True,
    )


elif page == "Times":
    st.header("Times")

    total_teams = len(teams)
    total_countries = teams["country_id"].nunique()
    total_types = teams["type"].nunique()
    teams_with_venue = teams["venue_id"].notna().sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Times", total_teams)
    col2.metric("Países", total_countries)
    col3.metric("Tipos", total_types)
    col4.metric("Com Estádio", int(teams_with_venue))

    st.divider()

    country_options = sorted(
        teams["country_id"].dropna().unique()
    )

    type_options = sorted(
        teams["type"].dropna().unique()
    )

    selected_country = st.selectbox(
        "País",
        options=["Todos"] + list(country_options),
    )

    selected_type = st.selectbox(
        "Tipo",
        options=["Todos"] + list(type_options),
    )

    filtered = teams.copy()

    if selected_country != "Todos":
        filtered = filtered[
            filtered["country_id"] == selected_country
        ]

    if selected_type != "Todos":
        filtered = filtered[
            filtered["type"] == selected_type
        ]

    st.subheader("Tabela de Times")

    st.dataframe(
        filtered[
            [
                "team_id",
                "team_name",
                "country_id",
                "venue_id",
                "gender",
                "type",
                "founded",
            ]
        ].sort_values("team_name"),
        use_container_width=True,
    )


elif page == "Temporadas":
    st.header("Temporadas")

    total_seasons = len(seasons)
    current_seasons = seasons["is_current"].sum()
    finished_seasons = seasons["finished"].sum()
    total_leagues = seasons["league_id"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Temporadas", total_seasons)
    col2.metric("Atuais", int(current_seasons))
    col3.metric("Finalizadas", int(finished_seasons))
    col4.metric("Ligas", total_leagues)

    st.divider()

    status_option = st.selectbox(
        "Status",
        options=["Todas", "Atual", "Histórica"],
    )

    filtered = seasons.copy()

    if status_option == "Atual":
        filtered = filtered[filtered["is_current"] == True]

    elif status_option == "Histórica":
        filtered = filtered[filtered["is_current"] == False]

    st.subheader("Tabela de Temporadas")

    st.dataframe(
        filtered[
            [
                "season_id",
                "league_id",
                "season_name",
                "is_current",
                "finished",
                "starting_at",
                "ending_at",
            ]
        ].sort_values("starting_at", ascending=False),
        use_container_width=True,
    )


elif page == "Partidas":
    st.header("Partidas")

    fixtures_view = fixtures.merge(
        competitions[["competition_id", "competition_name"]],
        left_on="league_id",
        right_on="competition_id",
        how="left",
    )

    fixtures_view = fixtures_view.merge(
        seasons[["season_id", "season_name"]],
        on="season_id",
        how="left",
    )

    fixtures_view["competition_label"] = fixtures_view["competition_name"].fillna(
        fixtures_view["league_id"].astype(str)
    )

    fixtures_view["season_label"] = fixtures_view["season_name"].fillna(
        fixtures_view["season_id"].astype(str)
    )

    total_fixtures = len(fixtures_view)
    fixtures_with_odds = fixtures_view["has_odds"].sum()
    total_competitions = fixtures_view["competition_label"].nunique()
    total_seasons = fixtures_view["season_label"].nunique()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Partidas", total_fixtures)
    col2.metric("Partidas com Odds", int(fixtures_with_odds))
    col3.metric("Competições", total_competitions)
    col4.metric("Temporadas", total_seasons)

    st.divider()

    competition_options = sorted(
        fixtures_view["competition_label"].dropna().unique()
    )

    season_options = sorted(
        fixtures_view["season_label"].dropna().unique()
    )

    selected_competition = st.selectbox(
        "Competição",
        options=["Todas"] + list(competition_options),
    )

    selected_season = st.selectbox(
        "Temporada",
        options=["Todas"] + list(season_options),
    )

    filtered = fixtures_view.copy()

    if selected_competition != "Todas":
        filtered = filtered[
            filtered["competition_label"] == selected_competition
        ]

    if selected_season != "Todas":
        filtered = filtered[
            filtered["season_label"] == selected_season
        ]

    st.subheader("Partidas por Competição")

    fixtures_by_competition = (
        filtered
        .groupby("competition_label")
        .size()
        .reset_index(name="total")
        .sort_values("total", ascending=False)
    )

    fig = px.bar(
        fixtures_by_competition,
        x="competition_label",
        y="total",
        text="total",
        labels={
            "competition_label": "Competição",
            "total": "Total de Partidas",
        },
    )

    fig.update_yaxes(
        range=[
            0,
            max(fixtures_by_competition["total"].max() * 1.15, 1),
        ]
    )

    fig.update_layout(
        xaxis_title="Competição",
        yaxis_title="Total de Partidas",
        showlegend=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("Tabela de Partidas")

    st.dataframe(
        filtered[
            [
                "fixture_id",
                "competition_label",
                "season_label",
                "fixture_name",
                "starting_at",
                "has_odds",
            ]
        ].sort_values("starting_at"),
        use_container_width=True,
    )


elif page == "Classificação":
    st.header("Classificação")

    standings_view = standings.merge(
        teams[["team_id", "team_name"]],
        left_on="participant_id",
        right_on="team_id",
        how="left",
    )

    standings_view = standings_view.merge(
        competitions[["competition_id", "competition_name"]],
        left_on="league_id",
        right_on="competition_id",
        how="left",
    )

    standings_view = standings_view.merge(
        seasons[["season_id", "season_name"]],
        on="season_id",
        how="left",
    )

    standings_view["team_label"] = standings_view["team_name"].fillna(
        standings_view["participant_id"].astype(str)
    )

    standings_view["competition_label"] = standings_view["competition_name"].fillna(
        standings_view["league_id"].astype(str)
    )

    standings_view["season_label"] = standings_view["season_name"].fillna(
        standings_view["season_id"].astype(str)
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Registros", len(standings_view))
    col2.metric("Média de Pontos", round(standings_view["points"].mean(), 2))
    col3.metric("Maior Pontuação", int(standings_view["points"].max()))

    st.divider()

    season_options = sorted(standings_view["season_label"].dropna().unique())
    competition_options = sorted(standings_view["competition_label"].dropna().unique())

    selected_season = st.selectbox(
        "Temporada",
        options=["Todas"] + list(season_options),
    )

    selected_competition = st.selectbox(
        "Competição",
        options=["Todas"] + list(competition_options),
    )

    filtered = standings_view.copy()

    if selected_season != "Todas":
        filtered = filtered[filtered["season_label"] == selected_season]

    if selected_competition != "Todas":
        filtered = filtered[filtered["competition_label"] == selected_competition]

    filtered = filtered.sort_values(
        ["season_label", "competition_label", "position"]
    )

    st.subheader("Tabela de Classificação")

    st.dataframe(
        filtered[
            [
                "season_label",
                "competition_label",
                "team_label",
                "position",
                "points",
                "result",
            ]
        ],
        use_container_width=True,
    )

    st.subheader("Top 10 por Pontos")

    top_points = (
        filtered
        .sort_values("points", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_points,
        x="team_label",
        y="points",
        text="points",
        labels={
            "team_label": "Time",
            "points": "Pontos",
        },
    )

    fig.update_yaxes(
        range=[
            0,
            max(top_points["points"].max() * 1.15, 1),
        ]
    )

    fig.update_layout(
        xaxis_title="Time",
        yaxis_title="Pontos",
        showlegend=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    ) 

elif page == "Monitoramento":
    st.header("Monitoramento")

    total_executions = len(pipeline_logs)
    successful_executions = (
        pipeline_logs["status"] == "SUCCESS"
    ).sum()

    failed_executions = (
        pipeline_logs["status"] == "FAILED"
    ).sum()

    last_execution = pipeline_logs["executed_at"].max()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Execuções", total_executions)
    col2.metric("Sucesso", int(successful_executions))
    col3.metric("Falhas", int(failed_executions))
    col4.metric("Última Execução", str(last_execution))

    st.divider()

    st.subheader("Registros Processados por Pipeline")

    records_by_pipeline = (
        pipeline_logs
        .groupby("pipeline_name")["records_processed"]
        .sum()
        .reset_index()
        .sort_values("records_processed", ascending=False)
    )

    fig = px.bar(
        records_by_pipeline,
        x="pipeline_name",
        y="records_processed",
        text="records_processed",
        labels={
            "pipeline_name": "Pipeline",
            "records_processed": "Registros Processados",
        },
    )

    fig.update_yaxes(
        range=[
            0,
            max(records_by_pipeline["records_processed"].max() * 1.15, 1),
        ]
    )

    fig.update_layout(
        xaxis_title="Pipeline",
        yaxis_title="Registros Processados",
        showlegend=False,
    )

    #fig = apply_plotly_layout(fig)

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader("Histórico de Execuções")

    logs_table = pipeline_logs.rename(
        columns={
            "pipeline_name": "Pipeline",
            "layer": "Camada",
            "records_processed": "Registros",
            "status": "Status",
            "message": "Mensagem",
            "executed_at": "Executado em",
        }
    )

    st.dataframe(
        logs_table,
        use_container_width=True,
    )

    render_footer()