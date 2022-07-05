---
title: federations
hide_title: false
hide_table_of_contents: false
keywords:
  - federations
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
<tr><td><b>Name</b></td><td><code>federations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.metastore.federations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The relative resource name of the federation, of the form: projects/{project_number}/locations/{location_id}/federations/{federation_id}`. |
| `updateTime` | `string` | Output only. The time when the metastore federation was last updated. |
| `createTime` | `string` | Output only. The time when the metastore federation was created. |
| `endpointUri` | `string` | Output only. The federation endpoint. |
| `uid` | `string` | Output only. The globally unique resource identifier of the metastore federation. |
| `backendMetastores` | `object` | A map from BackendMetastore rank to BackendMetastores from which the federation service serves metadata at query time. The map key is an integer that represents the order in which BackendMetastores should be evaluated to resolve database names at query time. A BackendMetastore with a lower number will be evaluated before a BackendMetastore with a higher number. |
| `labels` | `object` | User-defined labels for the metastore federation. |
| `state` | `string` | Output only. The current state of the federation. |
| `version` | `string` | Immutable. The Apache Hive metastore version of the federation. All backend metastore versions must be compatible with the federation version. |
| `stateMessage` | `string` | Output only. Additional information about the current state of the metastore federation, if available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_federations_get` | `SELECT` | `name` | Gets the details of a single federation. |
| `projects_locations_federations_list` | `SELECT` | `parent` | Lists federations in a project and location. |
| `projects_locations_federations_create` | `INSERT` | `parent` | Creates a metastore federation in a project and location. |
| `projects_locations_federations_delete` | `DELETE` | `name` | Deletes a single federation. |
| `projects_locations_federations_patch` | `EXEC` | `name` | Updates the fields of a federation. |
