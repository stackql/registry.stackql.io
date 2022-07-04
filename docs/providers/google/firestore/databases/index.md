---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the Database. Format: `projects/{project}/databases/{database}` |
| `concurrencyMode` | `string` | The concurrency control mode to use for this database. |
| `etag` | `string` | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| `keyPrefix` | `string` | Output only. The key_prefix for this database. This key_prefix is used, in combination with the project id ("~") to construct the application id that is returned from the Cloud Datastore APIs in Google App Engine first generation runtimes. This value may be empty in which case the appid to use for URL-encoded keys is the project_id (eg: foo instead of v~foo). |
| `locationId` | `string` | The location of the database. Available databases are listed at https://cloud.google.com/firestore/docs/locations. |
| `type` | `string` | The type of the database. See https://cloud.google.com/datastore/docs/firestore-or-datastore for information about how to choose. |
| `appEngineIntegrationMode` | `string` | The App Engine integration mode to use for this database. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_databases_get` | `SELECT` | `name` | Gets information about a database. |
| `projects_databases_list` | `SELECT` | `parent` | List all the databases in the project. |
| `projects_databases_create` | `INSERT` | `parent` | Create a database. |
| `projects_databases_exportDocuments` | `EXEC` | `name` | Exports a copy of all or a subset of documents from Google Cloud Firestore to another storage system, such as Google Cloud Storage. Recent updates to documents may not be reflected in the export. The export occurs in the background and its progress can be monitored and managed via the Operation resource that is created. The output of an export may only be used once the associated operation is done. If an export operation is cancelled before completion it may leave partial data behind in Google Cloud Storage. For more details on export behavior and output format, refer to: https://cloud.google.com/firestore/docs/manage-data/export-import |
| `projects_databases_importDocuments` | `EXEC` | `name` | Imports documents into Google Cloud Firestore. Existing documents with the same name are overwritten. The import occurs in the background and its progress can be monitored and managed via the Operation resource that is created. If an ImportDocuments operation is cancelled, it is possible that a subset of the data has already been imported to Cloud Firestore. |
| `projects_databases_patch` | `EXEC` | `name` | Updates a database. |
