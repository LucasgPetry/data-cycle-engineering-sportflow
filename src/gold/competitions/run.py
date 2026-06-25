from src.gold.competitions.service import GoldCompetitionService


def main():
    result = GoldCompetitionService().execute()
    print(result)


if __name__ == "__main__":
    main()