# Data Catalog — SportFlow Engine

## Visão Geral

Este catálogo documenta os principais ativos de dados disponibilizados pelo projeto SportFlow Engine.

O objetivo é fornecer governança, rastreabilidade e padronização dos dados consumidos pelo Data Warehouse e pelo dashboard analítico.

---

# Camada Gold

## gold.dim_competitions

### Descrição

Dimensão contendo informações descritivas das competições esportivas.

### Origem

SportsMonks API → Bronze → Silver → Gold

### Chave Primária

competition_id

### Principais Campos

| Campo            | Descrição                   |
| ---------------- | --------------------------- |
| competition_id   | Identificador da competição |
| competition_name | Nome da competição          |
| country_id       | País da competição          |
| type             | Tipo da competição          |
| active           | Indicador de atividade      |

---

## gold.dim_teams

### Descrição

Dimensão contendo informações dos times.

### Origem

SportsMonks API → Bronze → Silver → Gold

### Chave Primária

team_id

### Principais Campos

| Campo      | Descrição             |
| ---------- | --------------------- |
| team_id    | Identificador do time |
| team_name  | Nome do time          |
| country_id | País do time          |
| venue_id   | Estádio               |
| type       | Tipo do time          |

---

## gold.dim_seasons

### Descrição

Dimensão contendo informações das temporadas esportivas.

### Origem

SportsMonks API → Bronze → Silver → Gold

### Chave Primária

season_id

### Principais Campos

| Campo       | Descrição                  |
| ----------- | -------------------------- |
| season_id   | Identificador da temporada |
| season_name | Nome da temporada          |
| league_id   | Competição associada       |
| is_current  | Temporada atual            |
| finished    | Temporada finalizada       |

---

## gold.fact_fixtures

### Descrição

Tabela fato contendo partidas esportivas.

### Origem

SportsMonks API → Bronze → Silver → Gold

### Grão

Uma linha por partida.

### Principais Métricas

| Campo      | Descrição                     |
| ---------- | ----------------------------- |
| fixture_id | Identificador da partida      |
| season_id  | Temporada                     |
| league_id  | Competição                    |
| has_odds   | Indicador de odds disponíveis |

---

## gold.fact_standings

### Descrição

Tabela fato contendo classificações das equipes.

### Origem

SportsMonks API → Bronze → Silver → Gold

### Grão

Uma linha por posição na classificação.

### Principais Métricas

| Campo          | Descrição                  |
| -------------- | -------------------------- |
| participant_id | Time participante          |
| position       | Posição na tabela          |
| points         | Pontuação                  |
| result         | Resultado da classificação |

---

## gold.pipeline_execution_log

### Descrição

Tabela responsável pelo monitoramento das execuções dos pipelines.

### Origem

Processo interno de observabilidade.

### Principais Campos

| Campo             | Descrição               |
| ----------------- | ----------------------- |
| pipeline_name     | Nome do pipeline        |
| layer             | Camada processada       |
| records_processed | Quantidade de registros |
| status            | Status da execução      |
| executed_at       | Data e hora da execução |
| message           | Mensagem operacional    |
