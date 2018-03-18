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
class Documents(Base):
    """"""
    __tablename__ = 'documents'
    __table_args__ = {}
    id = Column(Integer, primary_key = True, nullable=False)
    doc_path = Column(String(500), index=True, unique=True)
    doc_name = Column(String(100), index=True, unique=True)
    api_number = Column(String(12), index=True)
    test_date = Column(Date)
    init_bradenhead_pressure = Column(REAL)
    init_intermediate_1_pressure = Column(REAL)
    init_intermediate_2_pressure = Column(REAL)
    init_casing_pressure = Column(REAL)
    init_tubing_pressure = Column(REAL)
    fin_bradenhead_pressure = Column(REAL)
    fin_intermediate_1_pressure = Column(REAL)
    fin_intermediate_2_pressure = Column(REAL)
    fin_casing_pressure = Column(REAL)
    fin_tubing_pressure = Column(REAL)
    bradenhead_buildup_pressure = Column(REAL)
    intermediate_1_buildup_pressure = Column(REAL)
    intermediate_2_buildup_pressure = Column(REAL)
    comment = Column(String(1000))
    shut_in = Column(Boolean, default='False')
    water_flow = Column(Boolean, default='False')
    oil_flow = Column(Boolean, default='False')
    scraped = Column(Boolean, default='False')
    scraper_name = Column(String(64))
    scraper_id = Column(Integer)
    date_scraped = Column(Date)
    user_id = Column(Integer)
    in_use = Column(Boolean)
    date_scraped = Column(Date)

class PrevDoc(Base):
    """"""
    __tablename__ = 'prev_doc'
    __table_args__ = {}
    id = Column(Integer, primary_key = True, nullable=False)
    doc_path = Column(String(500), index=True, unique=True)
    doc_name = Column(String(100), index=True, unique=True)
    api_number = Column(String(12), index=True)
    test_date = Column(Date)
    init_bradenhead_pressure = Column(REAL)
    init_intermediate_1_pressure = Column(REAL)
    init_intermediate_2_pressure = Column(REAL)
    init_casing_pressure = Column(REAL)
    init_tubing_pressure = Column(REAL)
    fin_bradenhead_pressure = Column(REAL)
    fin_intermediate_1_pressure = Column(REAL)
    fin_intermediate_2_pressure = Column(REAL)
    fin_casing_pressure = Column(REAL)
    fin_tubing_pressure = Column(REAL)
    bradenhead_buildup_pressure = Column(REAL)
    intermediate_1_buildup_pressure = Column(REAL)
    intermediate_2_buildup_pressure = Column(REAL)
    comment = Column(String(1000))
    shut_in = Column(Boolean, default='False')
    water_flow = Column(Boolean, default='False')
    oil_flow = Column(Boolean, default='False')
    scraped = Column(Boolean, default='False')
    scraper_name = Column(String(64))
    scraper_id = Column(Integer)
    date_scraped = Column(Date)
    user_id = Column(Integer)
    in_use = Column(Boolean)
    date_scraped = Column(Date)

#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == "__main__":
    #This file uploads the documents from the 'static' folder to the psql
    #database. The database must first be created through flask

    #Grab files:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(current_dir,'app', 'static')
    
    
    file_names = [f for f in os.listdir(dir_path) if isfile(join(dir_path,f))]
    file_paths = [join(dir_path, i) for i in file_names]
    #This can vary based on pdf format -- Set up for COGCC docs!
    api_nums = [i.split('_',1)[0] for i in file_names]
    api_nums = [i[0:10] for i in api_nums]
    api_nums = [i[0:2]+'-'+i[2:5]+'-'+i[5:10] for i in api_nums]
    #file_dates = [i.rsplit('_',1)[1] for i in file_names]
    #file_dates = [i.rsplit('.',1)[0] for i in file_dates]

    s = loadSession()
    
    try:
        #Loop through file names
        for i in range(len(file_names)):
            #If the file isn't in the database, add it
            d = s.query(Documents).filter(Documents.doc_name==file_names[i]).first()
            if d is None:
                record = Documents(**{
                    'doc_path' : file_paths[i],
                    'doc_name' : file_names[i],
                    'api_number' : api_nums[i],
                    'test_date' : None,
                    'init_bradenhead_pressure' : None,
                    'init_intermediate_1_pressure' : None,
                    'init_intermediate_2_pressure' : None,
                    'init_casing_pressure' : None,
                    'init_tubing_pressure' : None,
                    'fin_bradenhead_pressure' : None,
                    'fin_intermediate_1_pressure' : None,
                    'fin_intermediate_2_pressure' : None,
                    'fin_casing_pressure' : None,
                    'fin_tubing_pressure' : None,
                    'bradenhead_buildup_pressure' :None,
                    'intermediate_1_buildup_pressure' : None,
                    'intermediate_2_buildup_pressure' : None,
                    'comment' : None,
                    'shut_in' : False,
                    'water_flow' : False,
                    'oil_flow' : False,
                    'scraped' : False,
                    'scraper_name' : None,
                    'scraper_id' : None,
                    'date_scraped' : None,
                    'user_id' : None,
                    'in_use' : False,
                    'date_scraped' : None
                })
                s.add(record)
                s.commit()
                s.close()

        #Add a Previous Document for 100 potential users
        for i in range(100):
            record = PrevDoc(**{
                'doc_path' : None,
                'doc_name' : None,
                'api_number' : None,
                'test_date' : None,
                'init_bradenhead_pressure' : None,
                'init_intermediate_1_pressure' : None,
                'init_intermediate_2_pressure' : None,
                'init_casing_pressure' : None,
                'init_tubing_pressure' : None,
                'fin_bradenhead_pressure' : None,
                'fin_intermediate_1_pressure' : None,
                'fin_intermediate_2_pressure' : None,
                'fin_casing_pressure' : None,
                'fin_tubing_pressure' : None,
                'bradenhead_buildup_pressure' :None,
                'intermediate_1_buildup_pressure' : None,
                'intermediate_2_buildup_pressure' : None,
                'comment' : None,
                'shut_in' : False,
                'water_flow' : False,
                'oil_flow' : False,
                'scraped' : False,
                'scraper_name' : None,
                'scraper_id' : None,
                'date_scraped' : None,
                'user_id' : i,
                'in_use' : False,
                'date_scraped' : None
            })
            s.add(record)
            s.commit()
        s.close()

    except:
        print('File: '+file_names[i]+' failed!')

    print('file names & paths uploaded')
 

