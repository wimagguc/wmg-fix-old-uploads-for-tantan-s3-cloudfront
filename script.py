#!/usr/bin/python
import MySQLdb
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
execfile(os.path.join(BASE_DIR, 'settings.py'))

db = MySQLdb.connect(host=SETTINGS_SQL_HOST,
                     user=SETTINGS_SQL_USER,
                     passwd=SETTINGS_SQL_PASSWORD,
                     db=SETTINGS_SQL_DB)

cur = db.cursor()
cur.execute("SELECT post_id, meta_value FROM wp_postmeta where meta_key='_wp_attachment_metadata' ORDER BY post_id DESC")

images = []

##
## First, we collect all media data that we will need to insert the bucket info rows for
##
for row in cur.fetchall():
    rexp = 's:4:"file";s:(?:\d+):"((?:.+?)\.(?:jpg|jpeg|png|gif))";'
    if re.search(rexp, row[1]):
        p = re.search(rexp, row[1])
        file = str(p.groups()[0])
        images.append([row[0], file])

##
## Then, let's insert the bucket info data to wp_postmeta
##
## !!! CAUTION: THIS IS GOING TO MODIFY YOUR DB !!!
##
for i in images:
    post_id = i[0]
    key = 'wp-content/uploads/' + i[1]

    cur.execute("DELETE FROM wp_postmeta WHERE post_id=" + str(post_id) + " AND meta_key='amazonS3_info';")
    cur.execute("INSERT INTO wp_postmeta (post_id, meta_key, meta_value) VALUES (" +
        str(post_id) + ", 'amazonS3_info', 'a:2:{s:6:\"bucket\";s:" + str(len(SETTINGS_S3_BUCKET)) +
        ":\"" + SETTINGS_S3_BUCKET + "\";s:3:\"key\";s:" + str(len(key)) + ":\"" + key + "\";}')")

    print 'done: ' + str(post_id) + ' -> ' + i[1]

cur.close()
db.close()
