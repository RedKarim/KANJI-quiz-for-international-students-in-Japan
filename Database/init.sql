CREATE DATABASE IF NOT EXISTS user_manage_dv;
CREATE DATABASE IF NOT EXISTS kanjiquiz;

USE user_manage_dv;
SOURCE /docker-entrypoint-initdb.d/user_manage_dv.sql;

USE kanjiquiz;
SOURCE /docker-entrypoint-initdb.d/kanjiquiz.sql;

GRANT ALL PRIVILEGES ON user_manage_dv.* TO 'web_weavers'@'%';
GRANT ALL PRIVILEGES ON kanjiquiz.* TO 'web_weavers'@'%';
FLUSH PRIVILEGES; 