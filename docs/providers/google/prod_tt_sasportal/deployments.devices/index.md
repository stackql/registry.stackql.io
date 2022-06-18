---
title: deployments.devices
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
<tr><td><b>Name</b></td><td><code>deployments.devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.deployments.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` | Output only. Resource name. |
| `displayName` | `string` | The node's display name. |
| `sasUserIds` | `array` | User ids used by the devices belonging to this node. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `deploymentsId, devicesId` | Returns a requested node. |
| `delete` | `DELETE` | `deploymentsId, devicesId` | Deletes a node. |
| `move` | `EXEC` | `deploymentsId, devicesId` | Moves a node under another node or customer. |
| `patch` | `EXEC` | `deploymentsId, devicesId` | Updates an existing node. |
| `signDevice` | `EXEC` | `deploymentsId, devicesId` | Signs a device. |
| `updateSigned` | `EXEC` | `deploymentsId, devicesId` | Updates a signed device. |
