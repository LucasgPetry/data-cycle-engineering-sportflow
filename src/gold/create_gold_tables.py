from src.common.postgres import create_gold_dim_competitions_table


def main():
    create_gold_dim_competitions_table()
    print("Tabela gold.dim_competitions criada/verificada com sucesso.")


if __name__ == "__main__":
    main()