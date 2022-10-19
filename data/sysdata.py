import psutil as p
import datetime as dt

class sysdata(object):

    
    def cpu(self,inter=0.0,percores=False):
        cpu_res=p.cpu_percent(interval=inter,percpu=percores)
        return cpu_res

    def ram(self):
        ramusage=p.virtual_memory()
        return ramusage

    def date(self):
        curr_date=dt.datetime.now().date()
        return curr_date


    def time(self):
        curr_time=dt.datetime.now().time()
        return curr_time

    def datme(self):
        return dt.datetime.now()

class SysNetwork:

    def net_conn(self,type_net='all'):
        net_conn=p.net_connections(kind=type_net)
        nf=pd.DataFrame(net_conn)
        # print(nf.dropna())
        return net_conn
    
    def data_used(all_nic=False):
            data_used=p.net_io_counters(pernic=all_nic)
            # print(conn)
            # nf=pd.DataFrame(conn)
            # print(nf.iloc[:2,]/1.25e+8)
            return data_used
        


if __name__ == '__main__':
    import pandas as pd
    import sqlite3

# Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect("data.db")
    df = pd.read_sql_query("SELECT * FROM sysdata", con)

# Verify that result of SQL query is stored in the dataframe
    # print(df.tail(1000))
    conn=p.net_io_counters(pernic='all')
    print(conn)
    nf=pd.DataFrame(conn)
    print(nf.iloc[:2,]/1e+9)
