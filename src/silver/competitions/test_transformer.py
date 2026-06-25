from src.bronze.competitions.reader import BronzeCompetitionReader
from src.silver.competitions.transformer import SilverCompetitionTransformer


def main():
    reader = BronzeCompetitionReader()
    _, data = reader.read_latest()

    transformer = SilverCompetitionTransformer()
    df = transformer.transform(data)

    print(df.head())
    print(df.dtypes)
    print(f"Total de registros transformados: {len(df)}")


if __name__ == "__main__":
    main()