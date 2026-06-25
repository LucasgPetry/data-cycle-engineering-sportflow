from src.ingestion.competitions.service import (
    CompetitionIngestionService
)


def main():

    service = CompetitionIngestionService()

    result = service.execute()

    print(result)


if __name__ == "__main__":
    main()