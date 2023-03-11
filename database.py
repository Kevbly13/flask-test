from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://ehre34o64e2xbhgb24y4:pscale_pw_4tCWo76sRKBW5SIerM7Mvf2KEc5aSfp4nu2Gt64abdm@us-west.connect.psdb.cloud/joviancareers?charset=utf8mb4"

engine = create_engine(db_connection_string, 
    connect_args={
      "ssl": {
        "ca": "/etc/ssl/cert.pem",
        "cert": "/home/gord/client-ssl/client-cert.pem",
        "key": "/home/gord/client-ssl/client-key.pem"
      }
    })
  
with engine.connect() as conn:
  result = conn.execute(text("select * as jobs"))
  print(result.all())
