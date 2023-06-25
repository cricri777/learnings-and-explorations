import duckdb

def run():
    duckdb.sql("""
        SELECT
            *
        FROM read_csv('resources/billionaires.csv', 
        header=True,
        AUTO_DETECT=TRUE,
        dateformat='%d-%m-%Y', filename=True)
        LIMIT 100;
    """).show()

    conn = duckdb.connect()
    conn.execute("""
    
    """).df()

if __name__ == '__main__':
    run()
