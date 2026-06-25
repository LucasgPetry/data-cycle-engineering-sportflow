from src.silver.teams.service import SilverTeamService


def main():
    result = SilverTeamService().execute()
    print(result)


if __name__ == "__main__":
    main()