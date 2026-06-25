from src.ingestion.teams.service import TeamIngestionService


def main():
    result = TeamIngestionService().execute()
    print(result)


if __name__ == "__main__":
    main()