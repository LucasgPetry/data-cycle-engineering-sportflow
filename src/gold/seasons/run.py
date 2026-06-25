from src.gold.seasons.service import GoldSeasonService


def main():
    result = GoldSeasonService().execute()
    print(result)


if __name__ == "__main__":
    main()