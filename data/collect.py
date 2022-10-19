from sysdata import sysdata ,SysNetwork
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')

try:
    conn.execute('''CREATE TABLE sysdata
            (
            datetime       text ,
            cpu0           REAL   NOT NULL,
            cpu1           REAL   NOT NULL,
            cpu2           REAL   NOT NULL,
            ram            REAL   NOT NULL,
            data_download  REAL   NOT NULL,
            data_upload    REAL   NOT NULL);''')
except:
    print('database already created')
            
sd=sysdata()
sn=SysNetwork

samples=8000
interval=5
cpucores=True


for i in range(samples):

    # curr_date=sd.date()
    # curr_time=sd.time()

    cpu_data=sd.cpu(inter=interval,percores=cpucores)
    cpu0,cpu1,cpu2=cpu_data[0],cpu_data[1],cpu_data[2]
    # print(cpu0,cpu1,cpu2)

    ram_data=sd.ram().percent
    # print(f'Ram : {ram_data}')

    net=sn.data_used()
    netdf=pd.DataFrame(net)
    netdf=netdf.iloc[:2,]/1.25e+8
    data_net=netdf.values.tolist()
    data_upload=data_net[0]    
    data_download=data_net[1]
 
    # print(data_download)

    conn.execute(f"INSERT INTO sysdata (datetime,cpu0,cpu1,cpu2,ram,data_download,data_upload) VALUES (datetime('now'),{cpu0},{cpu1},{cpu2},{ram_data},{data_download[0]},{data_upload[0]} )")
    conn.commit() 
  
conn.close() 