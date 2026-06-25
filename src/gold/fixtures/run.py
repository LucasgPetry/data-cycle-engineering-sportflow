from src.gold.fixtures.service import GoldFixtureService


def main():
    result = GoldFixtureService().execute()
    print(result)


if __name__ == "__main__":
    main()