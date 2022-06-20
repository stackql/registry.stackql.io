---
title: customers.deployments
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>customers.deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.customers.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `deployments` | `array` | The deployments that match the request. |
| `nextPageToken` | `string` | A pagination token returned from a previous call to ListDeployments that indicates from where listing should continue. If the field is missing or empty, it means there are no more deployments. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customersId, deploymentsId` | Returns a requested node. |
| `list` | `SELECT` | `customersId` | Lists deployments. |
| `create` | `INSERT` | `customersId` | Creates a new deployment. |
| `delete` | `DELETE` | `customersId, deploymentsId` | Deletes a node. |
| `move` | `EXEC` | `customersId, deploymentsId` | Moves a node under another node or customer. |
| `patch` | `EXEC` | `customersId, deploymentsId` | Updates an existing node. |
