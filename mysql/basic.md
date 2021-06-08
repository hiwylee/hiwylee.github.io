## How-to Mysql

### Install MySQL Shell
```bash
[opc@db19c ~]$ sudo yum install https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
Failed to set locale, defaulting to C
Loaded plugins: langpacks, ulninfo
mysql80-community-release-el7-3.noarch.rpm                                              |  25 kB  00:00:00
Examining /var/tmp/yum-root-6e3sM1/mysql80-community-release-el7-3.noarch.rpm: mysql80-community-release-el7-3.noarch
Marking /var/tmp/yum-root-6e3sM1/mysql80-community-release-el7-3.noarch.rpm to be installed
Resolving Dependencies
There are unfinished transactions remaining. You might consider running yum-complete-transaction, or "yum-complete-transaction --cleanup-only" and "yum history redo last", first to finish them. If those don't work you'll have to try removing/installing packages by hand (maybe package-cleanup can help).
--> Running transaction check
---> Package mysql80-community-release.noarch 0:el7-3 will be installed
--> Finished Dependency Resolution
ol7_UEKR4/x86_64                                                                        | 2.5 kB  00:00:00
ol7_UEKR5/x86_64                                                                        | 2.5 kB  00:00:00
ol7_addons/x86_64                                                                       | 2.5 kB  00:00:00
ol7_developer/x86_64                                                                    | 2.5 kB  00:00:00
ol7_developer_EPEL/x86_64                                                               | 2.7 kB  00:00:00
ol7_developer_EPEL/x86_64/updateinfo                                                    | 178 kB  00:00:00
ol7_developer_EPEL/x86_64/primary_db                                                    |  15 MB  00:00:00
ol7_ksplice                                                                             | 2.5 kB  00:00:00
ol7_latest/x86_64                                                                       | 2.7 kB  00:00:00
ol7_latest/x86_64/updateinfo                                                            | 3.2 MB  00:00:00
ol7_latest/x86_64/primary_db                                                            |  35 MB  00:00:00
ol7_oci_included/x86_64                                                                 | 2.9 kB  00:00:00
ol7_oci_included/x86_64/primary_db                                                      | 589 kB  00:00:00
ol7_optional_latest/x86_64                                                              | 2.5 kB  00:00:00
ol7_optional_latest/x86_64/updateinfo                                                   | 1.3 MB  00:00:00
ol7_software_collections/x86_64                                                         | 2.5 kB  00:00:00

Dependencies Resolved

===============================================================================================================
 Package                         Arch         Version      Repository                                     Size
===============================================================================================================
Installing:
 mysql80-community-release       noarch       el7-3        /mysql80-community-release-el7-3.noarch        31 k

Transaction Summary
===============================================================================================================
Install  1 Package

Total size: 31 k
Installed size: 31 k
Is this ok [y/d/N]: y
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : mysql80-community-release-el7-3.noarch                                                      1/1
  Verifying  : mysql80-community-release-el7-3.noarch                                                      1/1

Installed:
  mysql80-community-release.noarch 0:el7-3

Complete!
[opc@db19c ~]$  sudo yum install mysql-client mysql-shell -y
Failed to set locale, defaulting to C
Loaded plugins: langpacks, ulninfo
mysql-connectors-community                                                              | 2.6 kB  00:00:00
mysql-tools-community                                                                   | 2.6 kB  00:00:00
mysql80-community                                                                       | 2.6 kB  00:00:00
(1/3): mysql-tools-community/x86_64/primary_db                                          |  88 kB  00:00:00
(2/3): mysql-connectors-community/x86_64/primary_db                                     |  80 kB  00:00:00
(3/3): mysql80-community/x86_64/primary_db                                              | 165 kB  00:00:00
No package mysql-client available.
Resolving Dependencies
There are unfinished transactions remaining. You might consider running yum-complete-transaction, or "yum-complete-transaction --cleanup-only" and "yum history redo last", first to finish them. If those don't work you'll have to try removing/installing packages by hand (maybe package-cleanup can help).
--> Running transaction check
---> Package mysql-shell.x86_64 0:8.0.25-1.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

===============================================================================================================
 Package                 Arch               Version                    Repository                         Size
===============================================================================================================
Installing:
 mysql-shell             x86_64             8.0.25-1.el7               mysql-tools-community              31 M

Transaction Summary
===============================================================================================================
Install  1 Package

Total download size: 31 M
Installed size: 140 M
Downloading packages:
warning: /var/cache/yum/x86_64/7Server/mysql-tools-community/packages/mysql-shell-8.0.25-1.el7.x86_64.rpm: Header V3 DSA/SHA1 Signature, key ID 5072e1f5: NOKEY
Public key for mysql-shell-8.0.25-1.el7.x86_64.rpm is not installed
mysql-shell-8.0.25-1.el7.x86_64.rpm                                                     |  31 MB  00:00:00
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
Importing GPG key 0x5072E1F5:
 Userid     : "MySQL Release Engineering <mysql-build@oss.oracle.com>"
 Fingerprint: a4a9 4068 76fc bd3c 4567 70c8 8c71 8d3b 5072 e1f5
 Package    : mysql80-community-release-el7-3.noarch (@/mysql80-community-release-el7-3.noarch)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : mysql-shell-8.0.25-1.el7.x86_64                                                             1/1
  Verifying  : mysql-shell-8.0.25-1.el7.x86_64                                                             1/1

Installed:
  mysql-shell.x86_64 0:8.0.25-1.el7

Complete!
```

### Connecting to MySQL
```sql
[opc@db19c ~]$  mysqlsh admin@10.0.0.134
Please provide the password for 'admin@10.0.0.134': ************
MySQL Shell 8.0.25

Copyright (c) 2016, 2021, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
Creating a session to 'admin@10.0.0.134'
Fetching schema names for autocompletion... Press ^C to stop.
Your MySQL connection id is 36 (X protocol)
Server version: 8.0.25-u2-cloud MySQL Enterprise - Cloud
No default schema selected; type \use <schema> to set one.
 MySQL  10.0.0.134:33060+ ssl  SQL > show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.0008 sec)
 MySQL  10.0.0.134:33060+ ssl  SQL > select * from mysql.user where user='admin'\G
*************************** 1. row ***************************
                    Host: %
                    User: admin
             Select_priv: Y
             Insert_priv: Y
             Update_priv: Y
             Delete_priv: Y
             Create_priv: Y
               Drop_priv: Y
             Reload_priv: N
           Shutdown_priv: N
            Process_priv: Y
               File_priv: N
              Grant_priv: Y
         References_priv: Y
              Index_priv: Y
              Alter_priv: Y
            Show_db_priv: Y
              Super_priv: N
   Create_tmp_table_priv: Y
        Lock_tables_priv: Y
            Execute_priv: Y
         Repl_slave_priv: Y
        Repl_client_priv: Y
        Create_view_priv: Y
          Show_view_priv: Y
     Create_routine_priv: Y
      Alter_routine_priv: Y
        Create_user_priv: Y
              Event_priv: Y
            Trigger_priv: Y
  Create_tablespace_priv: N
                ssl_type:
              ssl_cipher:
             x509_issuer:
            x509_subject:
           max_questions: 0
             max_updates: 0
         max_connections: 0
    max_user_connections: 0
                  plugin: caching_sha2_password
   authentication_string: $A$005$@9s58IC#;`oupG5sECOJJoHUtJ4q2oD2I7TF6TD0z6pL78fGeEMpSqkw4
        password_expired: N
   password_last_changed: 2021-06-08 16:14:54
       password_lifetime: NULL
          account_locked: N
        Create_role_priv: Y
          Drop_role_priv: Y
  Password_reuse_history: NULL
     Password_reuse_time: NULL
Password_require_current: NULL
         User_attributes: {"Restrictions": [{"Database": "sys", "Privileges": ["CREATE", "DROP", "REFERENCES", "INDEX", "ALTER", "CREATE TEMPORARY TABLES", "LOCK TABLES", "CREATE VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER"]}, {"Database": "mysql", "Privileges": ["INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "REFERENCES", "INDEX", "ALTER", "CREATE TEMPORARY TABLES", "LOCK TABLES", "EXECUTE", "CREATE VIEW", "CREATE ROUTINE", "ALTER ROUTINE", "EVENT", "TRIGGER"]}]}
1 row in set (0.0011 sec)
 MySQL  10.0.0.134:33060+ ssl  SQL >

````
