# import required modules
import os
import time
import datetime
import pipes
import gzip


#database info and backup file
BACKUP_DIR_NAME ='/postgresql_backups'
DBHOST = '127.0.0.1'
DBUSER = 'testuser'
DBUSERPASSWORD = 'F&9+7xZ`J%AXRgf'
DBNAME = 'test'

# Getting current DateTime
DATETIME = time.strftime('%Y%m%d-%H%M')
TODAYBACKUPPATH = BACKUP_DIR_NAME

# check if the backup folder exist or not
try:
    os.stat(TODAYBACKUPPATH)
except:
    os.mkdir(TODAYBACKUPPATH)

#starting backups
db = DBNAME
dumpcmd = "pg_dump -h " + DBHOST + " -U " + DBUSER + " -p " +  DBUSERPASSWORD + " -d  " + db + " -f " + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
os.system(dumpcmd)
#gzipcmd = "gzip" + pipes.quote(TODAYBACKUPPATH) + "/" + db + ".sql"
#os.system(gzipcmd)

print("Backup completed and have been created in" + TODAYBACKUPPATH + "directory")

