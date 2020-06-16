import _sqlite3,sys
conn=_sqlite3.connect('food.db')
curs=conn.cursor()

#query='SELECT * FROM food  ORDER BY food.sugar DESC'
#curs.execute(query)
#print(curs.fetchmany(100))

query='SELECT * FROM food WHERE '+sys.argv[1]
print(query)
curs.execute(query)
names=[f[0] for f in curs.description]  #f[0]代表的是cursor.description返回的元祖的第一个字段，数据库的字段属性。
for row in curs.fetchall():
    for pair in zip(names,row):
       print('{}:{}'.format(*pair))
     print()  #作用是在每一组数据之间增加一个空格（上面的一个循环结束之后）