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