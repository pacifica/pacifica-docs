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
shared state and workers. Each part has latency requirements so that
responses to the client are 
