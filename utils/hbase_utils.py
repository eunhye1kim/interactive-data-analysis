#!pip install happybase
#!$HBASE_HOME/bin/hbase-daemon.sh start thrift

import happybase
import pandas as pd

def hbase_to_dataframe(host, table_name, columns=None, row_start=None, row_stop=None, filter=None):
    """
    HBase 테이블로부터 데이터를 읽어와 Pandas DataFrame으로 반환합니다.

    Parameters:
    - host (str): HBase 서버의 호스트명 또는 IP 주소
    - table_name (str): HBase 테이블명
    - columns (list of str, optional): 가져올 컬럼의 리스트 (예: ['info:name', 'info:age'])
    - row_start (str, optional): 시작할 Row Key
    - row_stop (str, optional): 종료할 Row Key
    - filter (str, optional): HBase 필터 문자열

    Returns:
    - df (pd.DataFrame): HBase 데이터로부터 생성된 DataFrame
    """
    # HBase 연결 설정
    connection = happybase.Connection(host)
    table = connection.table(table_name)

    # 스캔 옵션 설정
    scan_kwargs = {}
    if columns:
        scan_kwargs['columns'] = [col.encode('utf-8') for col in columns]
    if row_start:
        scan_kwargs['row_start'] = row_start.encode('utf-8')
    if row_stop:
        scan_kwargs['row_stop'] = row_stop.encode('utf-8')
    if filter:
        scan_kwargs['filter'] = filter.encode('utf-8')

    # 데이터 스캔
    rows = table.scan(**scan_kwargs)

    # 데이터 수집을 위한 리스트 초기화
    data = []

    # 각 행의 데이터를 추출하여 리스트에 추가
    for key, value in rows:
        row_data = {'row_key': key.decode('utf-8')}
        for k, v in value.items():
            column_name = k.decode('utf-8')
            column_value = v.decode('utf-8')
            row_data[column_name] = column_value
        data.append(row_data)

    # HBase 연결 종료
    connection.close()

    # DataFrame 생성
    df = pd.DataFrame(data)

    return df

if __name__ == "__main__":
    # 함수 호출을 위한 매개변수 설정
    host = 'localhost'  # 실제 HBase 서버 주소로 변경하세요.
    table_name = 'users'  # 실제 테이블명으로 변경하세요.
    columns = ['info:name', 'info:age']  # 가져올 컬럼 지정

    # 함수 호출
    df = hbase_to_dataframe(host, table_name, columns=columns)

    # 필요한 경우 데이터 타입 변환
    if 'info:age' in df.columns:
        df['info:age'] = df['info:age'].astype(int)

    # 결과 출력
    print(df)