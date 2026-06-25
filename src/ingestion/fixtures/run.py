from src.ingestion.fixtures.service import FixtureIngestionService


def main():
    result = FixtureIngestionService().execute()
    print(result)


if __name__ == "__main__":
    main()