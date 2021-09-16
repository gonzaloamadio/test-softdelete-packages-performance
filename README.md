# Performance

This repo is intended to measure soft delete packages alternatives performance, in order to decide which one to use.

We are measuring : 

https://github.com/makinacorpus/django-safedelete

https://github.com/scoursen/django-softdelete


# Results

❯ ./manage.py makemigrations
Migrations for 'myapp':
  myapp/migrations/0001_initial.py
    - Create model SafeChild1
    - Create model SafeChild2
    - Create model SafeParent
    - Create model SoftChild1
    - Create model SoftChild2
    - Create model SoftParent
    - Create model SoftChild3
    - Add field softparent to softchild1
    - Create model SafeChild3
    - Add field safeparent to safechild1
❯ ./manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions, softdelete
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying myapp.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying softdelete.0001_initial... OK
  Applying softdelete.0002_auto_20170912_0537... OK


############################################### TEST SAFEDELETE with 1K records
❯ python manage.py runscript test_safedelete
========================================
0:00:00.591 - Start Program
========================================
Execution time : 18.031069852999998
========================================
0:00:15.194 - End Program
Elapsed time: 0:00:14.603
========================================

❯ python manage.py runscript test_safedelete
========================================
0:00:00.516 - Start Program
========================================

Execution time : 17.30305214
========================================
0:00:14.687 - End Program
Elapsed time: 0:00:14.170
========================================


############################################### TEST SOFTDELETE with 1K records

❯ python manage.py runscript test_softdelete
========================================
0:00:00.566 - Start Program
========================================

Execution time : 68.090595157
========================================
0:00:58.102 - End Program
Elapsed time: 0:00:57.535
========================================

❯ python manage.py runscript test_softdelete
========================================
0:00:00.492 - Start Program
========================================

Execution time : 35.664727697000004
========================================
0:00:30.399 - End Program
Elapsed time: 0:00:29.907
========================================

❯ python manage.py runscript test_softdelete
========================================
0:00:00.490 - Start Program
========================================

Execution time : 35.800647049999995
========================================
0:00:30.653 - End Program
Elapsed time: 0:00:30.163
========================================


############################################### TEST SAFEDELETE with 10K records


❯ python manage.py runscript test_safedelete
========================================
0:00:00.554 - Start Program
========================================
Execution time : 169.97445052700002
========================================
0:02:19.842 - End Program
Elapsed time: 0:02:19.287
========================================

❯ python manage.py runscript test_softdelete
========================================
0:00:00.540 - Start Program
========================================

Execution time : 356.741077677
========================================
0:04:57.862 - End Program
Elapsed time: 0:04:57.321
========================================
