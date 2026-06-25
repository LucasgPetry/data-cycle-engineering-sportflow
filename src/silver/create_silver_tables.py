from src.common.postgres import create_silver_competitions_table


def main():
    create_silver_competitions_table()
    print("Tabela silver.competitions criada/verificada com sucesso.")


if __name__ == "__main__":
    main()