# import required modules
import os
import time
import datetime
import pipes
import gzip


#database info and backup file
BACKUP_DIR_NAME ='/postgresql_backups'
DBHOST = '3.19.232.40:8081'
DBUSER = 'testuser'
DBUSERPASSWORD = 'F&9+7xZ`J%AXRgf'
DBNAME = 'testdb'

# Getting current DateTime
DATETIME = time.strftime('%Y%m%d-%H%M%S')
TODAYBACKUPPATH = BACKUP_DIR_NAME + '/'+ DATETIME

# check if the backup folder exist or not
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

#starting backups
db = DBNAME
dumpcmd = "pg_dump -h" + DBHOST + "-u" + DBUSER + "-p" + DBUSERPASSWORD + " " + db + ">" + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
os.system(dumpcmd)
gzipcmd = "gzip" + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
os.system(gzipcmd)

print("Backup completed and have been created in" + TODAYBACKUPPATH + "directory")
