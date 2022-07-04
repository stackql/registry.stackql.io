---
title: instances
hide_title: false
hide_table_of_contents: false
keywords:
  - instances
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
<tr><td><b>Name</b></td><td><code>instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigeeregistry.instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Format: `projects/*/locations/*/instance`. Currently only locations/global is supported. |
| `config` | `object` | Available configurations to provision an Instance. |
| `createTime` | `string` | Output only. Creation timestamp. |
| `state` | `string` | Output only. The current state of the Instance. |
| `stateMessage` | `string` | Output only. Extra information of Instance.State if the state is `FAILED`. |
| `updateTime` | `string` | Output only. Last update timestamp. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_instances_get` | `SELECT` | `name` | Gets details of a single Instance. |
| `projects_locations_instances_create` | `INSERT` | `parent` | Provisions instance resources for the Registry. |
| `projects_locations_instances_delete` | `DELETE` | `name` | Deletes the Registry instance. |