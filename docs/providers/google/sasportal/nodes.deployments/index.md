---
title: nodes.deployments
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
<tr><td><b>Name</b></td><td><code>nodes.deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.sasportal.nodes.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A pagination token returned from a previous call to ListDeployments that indicates from where listing should continue. If the field is missing or empty, it means there are no more deployments. |
| `deployments` | `array` | The deployments that match the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deploymentsId, nodesId` | Returns a requested node. |
| `list` | `SELECT` | `nodesId` | Lists deployments. |
| `delete` | `DELETE` | `deploymentsId, nodesId` | Deletes a node. |
| `move` | `EXEC` | `deploymentsId, nodesId` | Moves a node under another node or customer. |
| `patch` | `EXEC` | `deploymentsId, nodesId` | Updates an existing node. |
