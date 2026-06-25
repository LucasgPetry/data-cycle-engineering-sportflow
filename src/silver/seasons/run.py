from src.silver.seasons.service import SilverSeasonService


def main():
    result = SilverSeasonService().execute()
    print(result)


if __name__ == "__main__":
    main()