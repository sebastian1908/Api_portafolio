from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Database:

    def __init__(self):
        self.user = "root"
        self.password = ""
        self.server = "localhost"
        self.port = 3306
        self.database = "proyecto"
        self.engine = self.getconnection()

    def getconnection(self):
        return create_engine(
            "mysql+pymysql://{0}:{1}@{2}/{3}".format(self.user, self.password, self.server, self.database)
        )
    
    def setConnection(self):
        session = sessionmaker(bind=self.engine)
        return session()
