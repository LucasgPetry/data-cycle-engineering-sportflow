from src.ingestion.seasons.service import SeasonIngestionService


def main():
    result = SeasonIngestionService().execute()
    print(result)


if __name__ == "__main__":
    main()