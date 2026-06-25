from src.silver.standings.service import SilverStandingService


def main():
    result = SilverStandingService().execute()
    print(result)


if __name__ == "__main__":
    main()