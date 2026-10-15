from contextlib import closing

from .data_analysis import display_result, get_business_question_results
from .database import get_connection


def main():
    with closing(get_connection()) as connection:
        business_question_results = get_business_question_results(connection)

        display_result(business_question_results)


if __name__ == "__main__":
    main()
