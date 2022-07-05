---
title: ekm_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - ekm_connections
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
<tr><td><b>Name</b></td><td><code>ekm_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudkms.ekm_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name for the EkmConnection in the format `projects/*/locations/*/ekmConnections/*`. |
| `createTime` | `string` | Output only. The time at which the EkmConnection was created. |
| `etag` | `string` | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding. |
| `serviceResolvers` | `array` | A list of ServiceResolvers where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single ServiceResolver is supported. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_ekmConnections_get` | `SELECT` | `name` | Returns metadata for a given EkmConnection. |
| `projects_locations_ekmConnections_list` | `SELECT` | `parent` | Lists EkmConnections. |
| `projects_locations_ekmConnections_create` | `INSERT` | `parent` | Creates a new EkmConnection in a given Project and Location. |
| `projects_locations_ekmConnections_patch` | `EXEC` | `name` | Updates an EkmConnection's metadata. |
