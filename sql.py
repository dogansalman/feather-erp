# Sql query generator.
# Burada sadece parametrele göre navite sql sorguları oluşturulacak
# select update create table, drop table sorguları oluşturulacak

# Postgresql configuration
# https://www.psycopg.org/docs/install.html#quick-install 

from gc import callbacks
import psycopg2



conn = psycopg2.connect("dbname=test user=postgres")


# generate edilmiş sorguyu db ye göndericek.
def run(query):
    return 




# Örnek method
# def fonksiyon(*args,**kwargs):
#     for i in args:
#         print(i)
#     for k,v in kwargs.items():
#         print('anahtar: ',k,'Degerimiz: ',v)
 
# fonksiyon(1,2,3,'args' , deger = 'kwargs')

# args key kwargs value olacak şekilde parameteler alıcak.
# **args'ın ilk değeri her zaman veritabanınındaki tablo ismini temsil edecek.
# bu durumda gelen parametrelere göre query oluşturulacak. 
def select(*args, **kwargs):
    return