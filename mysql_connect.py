import MySQLdb

def select(query):
    db = MySQLdb.connect(host="localhost",    
                        user="root",         
                        passwd='~e83c3RO"25;',  
                        db="olx_mobile")        
    cur = db.cursor()

    cur.execute(query)
    db.close()
    result = cur.fetchall()
    return(result)
    


def insert(query):
    db = MySQLdb.connect(host="localhost",   
                        user="root",       
                        passwd='~e83c3RO"25;',  
                        db="olx_mobile")       
    cur = db.cursor()

    cur.execute(query)

    db.commit()
    db.close()