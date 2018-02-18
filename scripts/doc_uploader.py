import os 
from os.path import isfile, join, dirname, realpath
from app import app
from sqlalchemy import create_engine, Column, Integer, Float, Date
from sqlalchemy import REAL, String, Boolean, exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pudb

#Connect to database
psql_address = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % \
app.config['POSTGRES']
engine = create_engine(psql_address)
Base = declarative_base(engine)
########################################################################
#Updating the Tests table
class Tests(Base):
    """"""
    __tablename__ = 'test'
    __table_args__ = {}
    id = Column(Integer, primary_key = True, nullable=False)
    doc_path = Column(String(500), index=True, unique=True)
    doc_name = Column(String(100), index=True, unique=True)
    api_number = Column(String(12), index=True)
    test_date = Column(Date)
    initial_pressure = Column(REAL)
    final_pressure = Column(REAL)
    buildup_pressure = Column(REAL)
    water_flow = Column(Boolean, default='False')
    oil_flow = Column(Boolean, default='False')
    scraped = Column(Boolean, default='False')
    scraper_name = Column(String(64))



#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    pu.db
    #This file uploads the documents from the 'scrape_docs' folder to the psql
    #database. The database must first be created through flask

    #Grab files:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(current_dir,'../scrape_docs')

    file_names = [f for f in os.listdir(dir_path) if isfile(join(dir_path,f))]
    file_paths = [join(dir_path, i) for i in file_names]
    #This can vary based on pdf format -- Set up for COGCC docs!
    api_nums = [i.split('_',1)[0] for i in file_names]
    file_dates = [i.rsplit('_',1)[1] for i in file_names]
    file_dates = [i.rsplit('.',1)[0] for i in file_dates]

    s = loadSession()

    try:
        #Loop through file names
        for i in range(len(file_names)):
            #If the file isn't in the database, add it
            d = s.query(Tests).filter(Tests.doc_name==file_names[i]).first()
            if d is None:
                record = Tests(**{
                    'doc_path' : file_paths[i],
                    'doc_name' : file_names[i],
                    'api_number' : api_nums[i],
                    'test_date' : file_dates[i],
                    'initial_pressure' : None,
                    'final_pressure' : None,
                    'buildup_pressure' : None,
                    'water_flow' : False,
                    'oil_flow' : False,
                    'scraped' : False,
                    'scraper_name' : None
                })
                s.add(record)
                s.commit()
                s.close()
    except:
        print('File: '+file_names[i]+' failed!')

    print('file names & paths uploaded')
 

