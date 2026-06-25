from src.bronze.competitions.reader import BronzeCompetitionReader


def main():
    reader = BronzeCompetitionReader()

    object_name, data = reader.read_latest()

    print(f"Arquivo lido: {object_name}")
    print(f"Tipo dos dados: {type(data)}")
    print(f"Quantidade de registros: {len(data)}")


if __name__ == "__main__":
    main()