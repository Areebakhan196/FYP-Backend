import pymysql

users = ["WZLPlUHt3EDcnAh.root", "WZLPIUHt3EDcnAh.root"]
passwords = ["ji16rbPYUA8cHI0g", "ji16rbPYUA8cHl0g", "ji16rbPYUA8cHIOg", "ji16rbPYUA8cHlOg"]

for u in users:
    for p in passwords:
        try:
            conn = pymysql.connect(
                host='gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com',
                port=4000,
                user=u,
                password=p,
                database='sys',
                ssl={'ssl_mode': 'REQUIRED'}
            )
            print(f"SUCCESS with USER: {u} PASSWORD: {p}")
            conn.close()
            exit(0)
        except Exception as e:
            print(f"Failed {u} with {p}: {e}")
