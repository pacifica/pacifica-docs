# Pacifica Architecture

## Overall Architecture

Pacifica has some very important architectural characteristics that
put some limitations into the system. These characteristics have some
advantages as well and we will cover both in this section.

Pacifica is built on HTTP micro services that focus on specific
groups of requirements. The micro services do not have any
requirements to authenticate to each other. This presents a natural
border between trusted and untrusted requests. This provides the
ability to deploy the system into cloud environments.

## Micro Service Patterns

The micro services have specific design patterns to meet the needs of
that service. These design patterns are replicated to multiple micro
services...

### Long Running Data Transformation

This design pattern is for services that need to have long running
processes transforming data in the system from one place to the next.
This includes the ingest, uploader and cart systems.

This design pattern involves four parts; web service, messaging,
shared state and workers. The system has latency requirements that
are strict, such that backend processing is a requirement of these
systems. Requests are made to a frontend web service API and messages
are then transfered to the backend for processing. The backend
processes are responsible for processing the data and updating status
so that the web service can respond to requests. The data and status
is kept on the shared storage, the form is intentionally not defined
to allow services to define what that looks like.

### Web Services Solution Stack

This design pattern is to facilitate web access to the internal
services and allow users easy access to status, reporting and
search of the data in Pacifica. This is currently implemented
as a LAMP (Linux, Apache, MySQL, PHP) stack but a derivative
stack may be used depending on the specific requirements of
one of the services.

There are two forms of this service; a service that users directly
interact with from a web browser and a service that other parts of
Pacifica interact with but still have the latency requirements.
