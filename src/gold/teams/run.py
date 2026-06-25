from src.gold.teams.service import GoldTeamService


def main():
    result = GoldTeamService().execute()
    print(result)


if __name__ == "__main__":
    main()