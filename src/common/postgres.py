from sqlalchemy import create_engine, text

from src.config.settings import (
    POSTGRES_HOST,
    POSTGRES_PORT,
    POSTGRES_DB,
    POSTGRES_USER,
    POSTGRES_PASSWORD,
)


def get_postgres_engine():
    connection_url = (
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
        f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    )

    return create_engine(connection_url)


def create_silver_competitions_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS silver;

    CREATE TABLE IF NOT EXISTS silver.competitions (
        competition_id INTEGER PRIMARY KEY,
        sport_id INTEGER,
        country_id INTEGER,
        competition_name VARCHAR(255),
        short_code VARCHAR(50),
        type VARCHAR(100),
        sub_type VARCHAR(100),
        category INTEGER,
        active BOOLEAN,
        has_jerseys BOOLEAN,
        image_path TEXT,
        last_played_at TIMESTAMP,
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))


def create_gold_dim_competitions_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS gold;

    CREATE TABLE IF NOT EXISTS gold.dim_competitions (
        competition_key SERIAL PRIMARY KEY,
        competition_id INTEGER UNIQUE NOT NULL,
        competition_name VARCHAR(255),
        country_id INTEGER,
        type VARCHAR(100),
        sub_type VARCHAR(100),
        active BOOLEAN,
        last_played_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))

def create_silver_teams_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS silver;

    CREATE TABLE IF NOT EXISTS silver.teams (
        team_id INTEGER PRIMARY KEY,
        sport_id INTEGER,
        country_id INTEGER,
        venue_id INTEGER,
        gender VARCHAR(50),
        team_name VARCHAR(255),
        short_code VARCHAR(50),
        image_path TEXT,
        founded INTEGER,
        type VARCHAR(100),
        placeholder BOOLEAN,
        last_played_at TIMESTAMP,
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))

def create_gold_dim_teams_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS gold;

    CREATE TABLE IF NOT EXISTS gold.dim_teams (
        team_key SERIAL PRIMARY KEY,
        team_id INTEGER UNIQUE NOT NULL,
        team_name VARCHAR(255),
        country_id INTEGER,
        venue_id INTEGER,
        gender VARCHAR(50),
        type VARCHAR(100),
        founded INTEGER,
        last_played_at TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl)) 


def create_silver_seasons_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS silver;

    CREATE TABLE IF NOT EXISTS silver.seasons (
        season_id INTEGER PRIMARY KEY,
        sport_id INTEGER,
        league_id INTEGER,
        tie_breaker_rule_id INTEGER,
        name VARCHAR(255),
        finished BOOLEAN,
        pending BOOLEAN,
        is_current BOOLEAN,
        starting_at DATE,
        ending_at DATE,
        standings_recalculated_at TIMESTAMP,
        games_in_current_week BOOLEAN,
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))

def create_gold_dim_seasons_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS gold;

    CREATE TABLE IF NOT EXISTS gold.dim_seasons (
        season_key SERIAL PRIMARY KEY,
        season_id INTEGER UNIQUE NOT NULL,
        league_id INTEGER,
        season_name VARCHAR(255),
        is_current BOOLEAN,
        finished BOOLEAN,
        starting_at DATE,
        ending_at DATE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))

def create_silver_fixtures_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS silver;

    CREATE TABLE IF NOT EXISTS silver.fixtures (
        fixture_id BIGINT PRIMARY KEY,
        sport_id INTEGER,
        league_id INTEGER,
        season_id INTEGER,
        stage_id INTEGER,
        group_id INTEGER,
        aggregate_id INTEGER,
        round_id INTEGER,
        state_id INTEGER,
        venue_id INTEGER,
        name VARCHAR(255),
        starting_at TIMESTAMP,
        result_info TEXT,
        leg VARCHAR(50),
        details TEXT,
        length INTEGER,
        placeholder BOOLEAN,
        has_odds BOOLEAN,
        has_premium_odds BOOLEAN,
        starting_at_timestamp BIGINT,
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl)) 

def create_gold_fact_fixtures_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS gold;

    CREATE TABLE IF NOT EXISTS gold.fact_fixtures (
        fixture_key SERIAL PRIMARY KEY,
        fixture_id BIGINT UNIQUE NOT NULL,
        league_id INTEGER,
        season_id INTEGER,
        venue_id INTEGER,
        state_id INTEGER,
        fixture_name VARCHAR(255),
        starting_at TIMESTAMP,
        result_info TEXT,
        has_odds BOOLEAN,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))

def create_silver_standings_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS silver;

    CREATE TABLE IF NOT EXISTS silver.standings (
        standing_id BIGINT PRIMARY KEY,
        participant_id INTEGER,
        sport_id INTEGER,
        league_id INTEGER,
        season_id INTEGER,
        stage_id INTEGER,
        group_id INTEGER,
        round_id INTEGER,
        standing_rule_id INTEGER,
        position INTEGER,
        result VARCHAR(50),
        points INTEGER,
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl)) 

def create_gold_fact_standings_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS gold;

    CREATE TABLE IF NOT EXISTS gold.fact_standings (
        standing_key SERIAL PRIMARY KEY,
        standing_id BIGINT UNIQUE NOT NULL,
        participant_id INTEGER,
        league_id INTEGER,
        season_id INTEGER,
        stage_id INTEGER,
        position INTEGER,
        points INTEGER,
        result VARCHAR(50),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl)) 

def create_pipeline_execution_log_table():
    engine = get_postgres_engine()

    ddl = """
    CREATE SCHEMA IF NOT EXISTS gold;

    CREATE TABLE IF NOT EXISTS gold.pipeline_execution_log (
        execution_id SERIAL PRIMARY KEY,
        pipeline_name VARCHAR(255),
        layer VARCHAR(50),
        records_processed INTEGER,
        status VARCHAR(50),
        message TEXT,
        executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """

    with engine.begin() as connection:
        connection.execute(text(ddl))