from sysdata import sysdata ,SysNetwork
import pandas as pd
import sqlite3

conn = sqlite3.connect('sysdata.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)   
cursor = conn.cursor() 

try:
    create_table='''CREATE TABLE sysdata
            (
            datetime      TIMESTAMP NOT NULL,
            cpu0           REAL   NOT NULL,
            cpu1           REAL   NOT NULL,
            cpu2           REAL   NOT NULL,
            ram            REAL   NOT NULL,
            data_download  REAL   NOT NULL,
            data_upload    REAL   NOT NULL);'''
    cursor.execute(create_table)

except:
    print('database already created')

record_insert="INSERT INTO sysdata VALUES (?,?,?,?,?,?,?);"       

sd=sysdata()
sn=SysNetwork

samples=6000
interval=2
cpucores=True


for i in range(samples):

    curr_datetime=sd.datme()

    cpu_data=sd.cpu(inter=interval,percores=cpucores)
    cpu0,cpu1,cpu2=cpu_data[0],cpu_data[1],cpu_data[2]
    # print(cpu0,cpu1,cpu2)

    ram_data=sd.ram().percent
    # print(f'Ram : {ram_data}')

    net=sn.data_used()
    netdf=pd.DataFrame(net)
    netdf=netdf.iloc[:2,]/1e+9
    data_net=netdf.values.tolist()
    data_upload=data_net[0]    
    data_download=data_net[1]


    cursor.execute(record_insert,(curr_datetime,cpu0,cpu1,cpu2,ram_data,data_download[0],data_upload[0] ))
    conn.commit() 

cursor.close()  
conn.close() 