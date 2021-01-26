```
❯ sqlite3 db.sqlite3
SQLite version 3.28.0 2019-04-15 14:49:49
Enter ".help" for usage hints.
sqlite> .table
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            tag
auth_user_user_permissions  tag2bookmark
bookmark
sqlite> .schema bookmark
CREATE TABLE IF NOT EXISTS "bookmark" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "url" text NOT NULL);
sqlite> .schema tag
CREATE TABLE IF NOT EXISTS "tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" text NOT NULL);
sqlite> .schema tag2bookmark
CREATE TABLE IF NOT EXISTS "tag2bookmark" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tagged_at" datetime NOT NULL, "bookmark_id" integer NOT NULL REFERENCES "bookmark" ("id") DEFERRABLE INITIALLY DEFERRED, "tag_id" integer NOT NULL REFERENCES "tag" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "tag2bookmark_bookmark_id_e94d240b" ON "tag2bookmark" ("bookmark_id");
CREATE INDEX "tag2bookmark_tag_id_e7ac339a" ON "tag2bookmark" ("tag_id");
```
