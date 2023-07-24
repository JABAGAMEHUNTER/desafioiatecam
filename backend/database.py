#imports
import sys
import mariadb


#from typing import List
#from typing import Optional
#from sqlalchemy import ForeignKey
#from sqlalchemy import String
#from sqlalchemy.orm import DeclarativeBase
#from sqlalchemy.orm import Mapped
#from sqlalchemy.orm import mapped_column
#from sqlalchemy.orm import relationship



try: con = mariadb.connect(
    user="root",
    password="b",
    host="localhost",
    port=3306,
    database="companydb"
)

except mariadb.Error as ex:
    print(f"An error occurred while connecting to MariaDB: {ex}")
    sys.exit(1)

cur = con.cursor()
