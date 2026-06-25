from src.silver.fixtures.service import SilverFixtureService


def main():
    result = SilverFixtureService().execute()
    print(result)


if __name__ == "__main__":
    main()