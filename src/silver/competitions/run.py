from src.silver.competitions.service import SilverCompetitionService


def main():
    result = SilverCompetitionService().execute()
    print(result)


if __name__ == "__main__":
    main()