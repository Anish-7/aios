'''
author : anish m
created:Oct-17-2022
'''

import psutil as p
import datetime as dt

class sysdata:
    '''
    class sysdata 
    functions are to return system data

    1.cpu()- returns cpu usage in percentage
    agruments inter - interval as sample
              percores- if true returns all the cores values ; else returns average of all

    2. ram()- returns the ram usage in percentage

    3. datme()- returns the current date time as a TIMESTAMP which uses built in datetime module

    4.date()-returns the current data

    5.time()-returns the current time

    '''

    def cpu(self,inter=0.0,percores=False):
        cpu_res=p.cpu_percent(interval=inter,percpu=percores)
        return cpu_res

    def ram(self):
        ramusage=p.virtual_memory()
        return ramusage

    def datme(self):
        return dt.datetime.now()

    def date(self):
        curr_date=dt.datetime.now().date()
        return curr_date


    def time(self):
        curr_time=dt.datetime.now().time()
        return curr_time



class SysNetwork:
    '''
    1.net_conn()
    return system-wide socket connections as a list of
    (fd, family, type, laddr, raddr, status, pid) namedtuples.
    In case of limited privileges 'fd' and 'pid' may be set to -1
    and None respectively.
    The *kind* parameter filters for connections that fit the
    following criteria:

    +------------+----------------------------------------------------+
    | Kind Value | Connections using                                  |
    +------------+----------------------------------------------------+
    | inet       | IPv4 and IPv6                                      |
    | inet4      | IPv4                                               |
    | inet6      | IPv6                                               |
    | tcp        | TCP                                                |
    | tcp4       | TCP over IPv4                                      |
    | tcp6       | TCP over IPv6                                      |
    | udp        | UDP                                                |
    | udp4       | UDP over IPv4                                      |
    | udp6       | UDP over IPv6                                      |
    | unix       | UNIX socket (both UDP and TCP protocols)           |
    | all        | the sum of all the possible families and protocols |
    +------------+----------------------------------------------------+

    2.data_used():
       bytes_sent:   number of bytes sent
       bytes_recv:   number of bytes received

    If *type_net* is True return the same information for every
    network interface installed on the system as a dictionary
    with network interface names as the keys and the namedtuple
    described above as the values.

    we can convert the bytes to gb by dividing 1e+9

    '''

    def net_conn(self,type_net='all'):
        net_conn=p.net_connections(kind=type_net)
        nf=pd.DataFrame(net_conn)
        # print(nf.dropna())
        return net_conn

    
    
    def data_used(all_nic=False):
            data_used=p.net_io_counters(pernic=all_nic)
            # print(conn)
            # nf=pd.DataFrame(conn)
            # print(nf.iloc[:2,]/1e+9)
            return data_used

    def get_processes(self):
        fqdn = self.get_FQDN()
        process_infos = list()
        for proc in p.process_iter():
            proc_info = dict()
            with proc.oneshot():
                proc_info["pid"] = proc.pid
                proc_info["ppid"] = proc.ppid()
                proc_info["name"] = proc.name()
                proc_info["exe"] = proc.exe()  # Requires root access for '/proc/#/exe'
                proc_info["computer"] = fqdn
                proc_info["cpu_percent"] = proc.cpu_percent()

                mem_info = proc.memory_info()
                proc_info["mem_rss"] = mem_info.rss

                proc_info["num_threads"] = proc.num_threads()
                proc_info["nice_priority"] = proc.nice()
            process_infos.append(proc_info)
        return process_infos
        


if __name__ == '__main__':
    import pandas as pd
    import sqlite3

# Read sqlite query results into a pandas DataFrame
    con = sqlite3.connect("sysdata.db")
    df = pd.read_sql_query("SELECT * FROM sysdata", con)

# Verify that result of SQL query is stored in the dataframe
    print(df.tail(100))




