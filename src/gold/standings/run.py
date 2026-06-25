from src.gold.standings.service import GoldStandingService


def main():
    result = GoldStandingService().execute()
    print(result)


if __name__ == "__main__":
    main()