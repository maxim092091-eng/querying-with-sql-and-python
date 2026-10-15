import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.figure import Figure


def get_business_question_results(
    connection: sqlite3.Connection,
) -> dict[str : pd.DataFrame]:
    """Return business analysis results as a dictionary of DataFrames."""

    query_best_10_tracks = """
    SELECT
        Track.Name AS track,
        SUM(InvoiceLine.Quantity) AS total_sold
    FROM InvoiceLine
    Join Track
        ON InvoiceLine.TrackId = Track.TrackId
    GROUP BY InvoiceLine.TrackId
    ORDER BY total_sold DESC
    LIMIT 10;
    """

    query_country_revenue = """
    SELECT 
        BillingCountry AS country,
        SUM(Total) AS total_revenue
    FROM Invoice
    GROUP BY BillingCountry
    ORDER BY total_revenue DESC;
    """

    query_employee_sales = """
    SELECT 
        Employee.FirstName AS first_name,
        Employee.LastName AS last_name,
        SUM(Invoice.Total) AS total_sales
    FROM Employee
    Join Customer
        ON Employee.EmployeeId = Customer.SupportRepId
    Join Invoice
        ON Invoice.CustomerId = Customer.CustomerId
    GROUP BY Employee.EmployeeId
    ORDER BY total_sales DESC;
    """

    result = {
        "top_10_tracks": pd.read_sql_query(query_best_10_tracks, connection),
        "country_revenue": pd.read_sql_query(query_country_revenue, connection),
        "top_sales_employee": pd.read_sql_query(query_employee_sales, connection),
    }

    return result


def create_bar_charts(data: dict[str, pd.DataFrame]) -> Figure:
    "Create charts based on the data and return them."
    figure, axes = plt.subplots(3, 1, figsize=(12, 15))

    data["top_10_tracks"].plot(
        x="track",
        y="total_sold",
        kind="bar",
        legend=False,
        ax=axes[0],
    )
    axes[0].set_title("Best tracks")
    axes[0].set_xlabel("Track")
    axes[0].set_ylabel("Total sold")

    data["country_revenue"].plot(
        x="country",
        y="total_revenue",
        kind="bar",
        legend=False,
        ax=axes[1],
    )
    axes[1].set_title("Revenue by Country")
    axes[1].set_xlabel("Country")
    axes[1].set_ylabel("Revenue")

    employee_data = data["top_sales_employee"].copy()
    employee_data["employee"] = (
        employee_data["first_name"] + " " + employee_data["last_name"]
    )

    employee_data.plot(
        x="employee",
        y="total_sales",
        kind="bar",
        legend=False,
        ax=axes[2],
    )
    axes[2].set_title("Employee sales")
    axes[2].set_xlabel("Full name")
    axes[2].set_ylabel("Total sales")

    figure.tight_layout()

    return figure


def display_result(data: dict[str, pd.DataFrame]) -> None:
    "Format and display the result tables, call the function to create charts, and display the charts."
    for value in data.values():
        display_value = value.copy()
        display_value.insert(0, "#", range(1, len(display_value) + 1))

        print(f"{display_value.to_string(index=False)}\n")

    create_bar_charts(data)
    plt.show()
