import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-2f9b8868-marketingdvtc-3290.b.aivencloud.com",

        port=14830,

        user="avnadmin",

        password="AVNS_lWrYNu_sFsbVeoQOedt",

        database="company1",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
