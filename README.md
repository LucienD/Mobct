Pew - Django - PostgreSQL
=======================


# Install Pew

    pip install pew

### See virtual env pew

    pew ls

### create pew env
    
    pew new --python=python2.7 -i django==1.7.8 <name env>

### run env

    pew workon <name env>

# Install Requirements

Go in folder mobycity

    pip install -r requirements.txt

# Install PostgreSQL

    sudo apt-get install postgresql

### configure postgresql for Mobyci

####connect you to default user => postgres

    sudo -i -u postgres

####create user

    sudo vim /etc/postgresql/x.x/main/pg_hba.conf

(x.x) = your version postgresql

change local

    local   all         all                         md5

save and get out pg_hba.conf

restart postgresql

    sudo /etc/init.d/postgresql restart

create user

    sudo -i -u postgres
    createuser -P --interactive <name_user>
    Enter password for new role:
    Enter it angain:
    Shall the new role be a superuser? (y/n) n
    Shall the new role be allowed to create databases? (y/n) y
    Shall the new role be allowed to create more new roles? (y/n) y


