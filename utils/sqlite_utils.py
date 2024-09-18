import sqlite3
import pandas as pd

def load_table_to_dataframe(db_path, table_name):
    """
    SQLite 데이터베이스에서 특정 테이블을 읽어와 DataFrame으로 반환하는 함수입니다.

    Parameters:
        db_path (str): SQLite 데이터베이스 파일의 경로
        table_name (str): 읽어올 테이블의 이름

    Returns:
        pandas.DataFrame: 테이블 데이터를 담은 DataFrame
    """
    try:
        # SQLite 데이터베이스에 연결합니다.
        conn = sqlite3.connect(db_path)

        # 테이블 데이터를 읽어옵니다.
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)

    except Exception as e:
        print(f"데이터를 읽어오는 중 오류 발생: {e}")
        df = None

    finally:
        # 데이터베이스 연결을 닫습니다.
        conn.close()

    return df

if __name__ == "__main__":
    database_path = 'test_database.db'
    table = 'test_table'

    # 데이터베이스에 연결합니다.
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # 테이블을 생성합니다.
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS {table} (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        email TEXT
    );
    '''
    cursor.execute(create_table_query)

    # 테스트 데이터를 정의합니다.
    test_data = [
        (1, 'Alice', 30, 'alice@example.com'),
        (2, 'Bob', 25, 'bob@example.com'),
        (3, 'Charlie', 35, 'charlie@example.com')
    ]

    # 이미 데이터가 존재하는지 확인하고 없으면 삽입합니다.
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    count = cursor.fetchone()[0]
    if count == 0:
        insert_query = f"INSERT INTO {table} (id, name, age, email) VALUES (?, ?, ?, ?)"
        cursor.executemany(insert_query, test_data)
        conn.commit()
        print("테스트 데이터를 삽입했습니다.")
    else:
        print("테이블에 이미 데이터가 존재합니다.")

    # 데이터베이스 연결을 닫습니다.
    conn.close()

    # DataFrame으로 데이터를 로드합니다.
    dataframe = load_table_to_dataframe(database_path, table)
    print(dataframe)
