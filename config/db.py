from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Ved12ant35@localhost:3306/CCBLOG")
meta=MetaData()
conn = engine.connect()

