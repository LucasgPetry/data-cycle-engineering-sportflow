from sqlalchemy import text

from src.common.postgres import (
    get_postgres_engine,
    create_pipeline_execution_log_table,
)


def log_pipeline_execution(
    pipeline_name: str,
    layer: str,
    records_processed: int,
    status: str,
    message: str = "",
):
    create_pipeline_execution_log_table()

    engine = get_postgres_engine()

    query = text(
        """
        INSERT INTO gold.pipeline_execution_log (
            pipeline_name,
            layer,
            records_processed,
            status,
            message
        )
        VALUES (
            :pipeline_name,
            :layer,
            :records_processed,
            :status,
            :message
        )
        """
    )

    with engine.begin() as connection:
        connection.execute(
            query,
            {
                "pipeline_name": pipeline_name,
                "layer": layer,
                "records_processed": records_processed,
                "status": status,
                "message": message,
            },
        )