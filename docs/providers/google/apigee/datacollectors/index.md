---
title: datacollectors
hide_title: false
hide_table_of_contents: false
keywords:
  - datacollectors
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
<tr><td><b>Name</b></td><td><code>datacollectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.datacollectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | ID of the data collector. Must begin with `dc_`. |
| `description` | `string` | A description of the data collector. |
| `createdAt` | `string` | Output only. The time at which the data collector was created in milliseconds since the epoch. |
| `lastModifiedAt` | `string` | Output only. The time at which the Data Collector was last updated in milliseconds since the epoch. |
| `type` | `string` | Immutable. The type of data this data collector will collect. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_datacollectors_get` | `SELECT` | `name` | Gets a data collector. |
| `organizations_datacollectors_list` | `SELECT` | `parent` | Lists all data collectors. |
| `organizations_datacollectors_create` | `INSERT` | `parent` | Creates a new data collector. |
| `organizations_datacollectors_delete` | `DELETE` | `name` | Deletes a data collector. |
| `organizations_datacollectors_patch` | `EXEC` | `name` | Updates a data collector. |
