import pymysql
status=True


# Open database connection
try:
    db = pymysql.connect("37.59.55.185","GsZXhEqBA4","XZ96KKxtud","GsZXhEqBA4" )
    cursor = db.cursor()
    status=False
except Exception as e:
    print("Check Your Internet!",e)
    input("")
    exit(0)
    


