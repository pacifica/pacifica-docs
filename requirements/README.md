# Pacifica Requirements

## Terms and Definitions

*   HSM: hierarchical storage management

## Archive Interface

1.  The system must interface with existing *HSM* technologies.
2.  The system must store data in the *HSM*.
3.  The system must retrieve data upon request from the *HSM*.

## Metadata Storage

1.  The system must store the metadata given to the system.

2.  The system must provide flexible search capabilities to retrieve
    metadata from the system.

## Metadata and Data Ingest

1.  The system must accept data and metadata given to the system.

2.  The system must provide end-to-end validation of the data before
    accepting it into the system.

3.  The system must send the data to the archive interface.

4.  The system must send the metadata to the metadata storage
    interface.

## Metadata and Data Capture (Uploader)

1.  The system must be able to view source data at the creation
    source.

2.  The system must be able to utilize the site specific deployment
    configuration as metadata to the system.

3.  The system must except metadata provided to the system.

4.  The system must provide end-to-end validation of the data before
    sending it to the ingest system.

5.  The system must send data and metadata to the ingest system to be
    validated and stored.

## Data Egress (Cart)

1.  The system must accept a request to bundle data from the archive
    interface.

2.  The system must build a data bundle and store it temporarily.

3.  The system must provide the data bundle upon request.

## Data Ingest Status

1.  The system must present the status of the data and metadata,
    from the upload and ingest systems.

2.  The system must issue requests to the cart for data that's been
    validated by the upload and ingest systems.

## Data Ingest Reporting

1.  The system must present statistical information about the data
    and metadata from the ingest system.

2.  The system must issue requests to the cart for data that's been
    validated by the upload and ingest systems.

## Authorization and Authentication

1.  The system must support any kind of authenticator provided by the
    installation site.

1.  The system must be able to query metadata to utilize custom
    authorization mechanisms.

## Search and Discovery

1.  The system must use the metadata in the system to provide a
    dynamic search interface that changes as the metadata changes.

1.  The system must issue requests to the cart for data that's been
    validated by the upload and ingest systems.
