import sqlite3

import pandas as pd
from querying_with_sql_and_python.data_analysis import get_business_question_results
from querying_with_sql_and_python.database import get_connection


def test_get_connection(tmp_path):
    db_path = tmp_path / "test.db"

    connection = get_connection(db_path)

    assert isinstance(connection, sqlite3.Connection)

    connection.close()


def test_business_question_results():
    connection = get_connection()

    answers = get_business_question_results(connection)

    assert all(
        key
        in (
            "top_10_tracks",
            "country_revenue",
            "top_sales_employee",
        )
        for key in answers
    )

    assert all(isinstance(value, pd.DataFrame) for value in answers.values())
