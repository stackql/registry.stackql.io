---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - services
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the metastore service, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}. |
| `metadataIntegration` | `object` | Specifies how metastore metadata should be integrated with external services. |
| `network` | `string` | Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:projects/{project_number}/global/networks/{network_id}. |
| `updateTime` | `string` | Output only. The time when the metastore service was last updated. |
| `port` | `integer` | The TCP port at which the metastore service is reached. Default: 9083. |
| `releaseChannel` | `string` | Immutable. The release channel of the service. If unspecified, defaults to STABLE. |
| `endpointUri` | `string` | Output only. The URI of the endpoint used to access the metastore service. |
| `hiveMetastoreConfig` | `object` | Specifies configuration information specific to running Hive metastore software as the metastore service. |
| `metadataManagementActivity` | `object` | The metadata management activities of the metastore service. |
| `encryptionConfig` | `object` | Encryption settings for the service. |
| `state` | `string` | Output only. The current state of the metastore service. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore service. |
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore service, if available. |
| `artifactGcsUri` | `string` | Output only. A Cloud Storage URI (starting with gs://) that specifies where artifacts related to the metastore service are stored. |
| `createTime` | `string` | Output only. The time when the metastore service was created. |
| `tier` | `string` | The tier of the service. |
| `networkConfig` | `object` | Network configuration for the Dataproc Metastore service. |
| `maintenanceWindow` | `object` | Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service. |
| `labels` | `object` | User-defined labels for the metastore service. |
| `databaseType` | `string` | Immutable. The database type that the Metastore service stores its data. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_services_get` | `SELECT` | `name` | Gets the details of a single service. |
| `projects_locations_services_list` | `SELECT` | `parent` | Lists services in a project and location. |
| `projects_locations_services_create` | `INSERT` | `parent` | Creates a metastore service in a project and location. |
| `projects_locations_services_delete` | `DELETE` | `name` | Deletes a single service. |
| `projects_locations_services_exportMetadata` | `EXEC` | `service` | Exports metadata from a service. |
| `projects_locations_services_patch` | `EXEC` | `name` | Updates the parameters of a single service. |
| `projects_locations_services_restore` | `EXEC` | `service` | Restores a service from a backup. |
