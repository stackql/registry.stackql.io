---
title: nodes.devices
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
<tr><td><b>Name</b></td><td><code>nodes.devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.prod_tt_sasportal.nodes.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `devices` | `array` | The devices that match the request. |
| `nextPageToken` | `string` | A pagination token returned from a previous call to ListDevices that indicates from where listing should continue. If the field is missing or empty, it means there is no more devices. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `devicesId, nodesId` | Returns a requested node. |
| `list` | `SELECT` | `nodesId` | Lists devices under a node or customer. |
| `create` | `INSERT` | `nodesId` | Creates a device under a node or customer. |
| `delete` | `DELETE` | `devicesId, nodesId` | Deletes a node. |
| `createSigned` | `EXEC` | `nodesId` | Creates a signed device under a node or customer. |
| `move` | `EXEC` | `devicesId, nodesId` | Moves a node under another node or customer. |
| `patch` | `EXEC` | `devicesId, nodesId` | Updates an existing node. |
| `signDevice` | `EXEC` | `devicesId, nodesId` | Signs a device. |
| `updateSigned` | `EXEC` | `devicesId, nodesId` | Updates a signed device. |
