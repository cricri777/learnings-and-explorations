import duckdb


def run():
    conn = duckdb.connect()
    results = conn.execute("""
        SELECT
            COUNT(*)
        FROM read_csv('resources/billionaires.csv', 
        header=True,
        AUTO_DETECT=TRUE,
        dateformat='%d-%m-%Y', filename=True);
        
    """).fetchall()

    print(results)


if __name__ == '__main__':
    run()
