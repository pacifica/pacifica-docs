# Python PIP Install Instructions

Pacifica is highly recommended to use virtual environments to install manually.

## Install Software Dependencies

There are several external services that need to be installed and configured to use the Pacifica services.

### PostgreSQL

Download and install the latest version of PostgreSQL for your platform.

For RedHat systems.

```
yum -y install postgresql-server
service postgresql initdb
service postgresql start
```

For Windows use EnterpriseDB installer.

Adding users and databases require that the user be given all permissions to
the database specified.

 * Metadata service requires:
  - Username is `pacifica`
  - Password is `pacifica`
  - Database is `pacifica_metadata`

### MySQL

Download and install MySQL (or equivalent) for your platform.

```
yum -y install mysql-server
service mysql start
```

Adding users and databases require that the user be given all permissions to
the database specified.

 * Cart service requires:
  - Username is `cartd`
  - Password is `cartd`
  - Database is `pacifica_cart`
 * Ingest service requires:
  - Username is `ingest`
  - Password is `ingest`
  - Database is `pacifica_ingest`
 * UniqueID service requires:
  - Username is `uniqueid`
  - Password is `uniqueid`
  - Database is `pacifica_uniqueid`

### RabbitMQ

Download and install the RabbitMQ server for your platform.

For RedHat bases systems you should follow the RabbitMQ
[install instructions](https://www.rabbitmq.com/install-rpm.html).

You should also configure a user with access to vhosts as follows.

 * Cart service requires:
  - Username is `guest`
  - Password is `guest`
  - VHost is `/cart`
 * Ingest service requires:
  - Username is `guest`
  - Password is `guest`
  - VHost is `/ingest`

### ElasticSearch

Download and install ElasticSearch for your platform.

For Redhat bases systems you should follow the Elasticsearch
[install instructions](https://www.elastic.co/guide/en/elasticsearch/reference/current/rpm.html).


### Install Python

Install Python for your platform most Linux systems have this done already.
Windows users should get it [here](https://www.python.org/downloads/).

```
yum -y install python python-pip python-virtualenv
```

### Install Git

Install Git source code manager for your platform, most Linux systems have
this done already. Windows users should get it [here](https://git-scm.com/downloads).

```
yum -y install git
```

## Install Pacifica Core Services

It is recommended to install the core services into a virtual environment.

```
virtualenv /opt/pacifica
. /opt/pacifica/bin/activate
pip install --upgrade pip setuptools wheel
```

The requirements file for all the core services is as follows.

```
git+https://github.com/pacifica/pacifica-archiveinterface.git#egg=PacificaArchiveInterface
git+https://github.com/pacifica/pacifica-metadata.git#egg=PacificaMetadata
git+https://github.com/pacifica/pacifica-policy.git#egg=PacificaPolicy
git+https://github.com/pacifica/pacifica-uniqueid.git#egg=PacificaUniqueID
git+https://github.com/pacifica/pacifica-ingest.git#egg=PacificaIngest
git+https://github.com/pacifica/pacifica-cartd.git#egg=PacificaCartd
git+https://github.com/pacifica/pacifica-proxy.git#egg=PacificaProxy
```

Then run pip the with the requirements file.

```
pip install -r /tmp/pacifica-requirements.txt
```

Set the following environment variables.

```
export AMQP_VHOST=/cart
export BROKER_VHOST=/ingest
```

## Start the Pacifica Core Services

Run the commands to start the services.

```
MetadataServer &
PolicyServer &
UniqueIDServer &
ArchiveInterface &
ProxyServer &
IngestServer &
CartServer &
celery -A cart worker -l info &
celery -A ingest.backend worker -l info &
```
