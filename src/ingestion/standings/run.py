from src.ingestion.standings.service import StandingIngestionService


def main():
    result = StandingIngestionService().execute()
    print(result)


if __name__ == "__main__":
    main()