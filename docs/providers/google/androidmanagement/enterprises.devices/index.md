---
title: enterprises.devices
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
<tr><td><b>Name</b></td><td><code>enterprises.devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidmanagement.enterprises.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there are more results, a token to retrieve next page of results. |
| `devices` | `array` | The list of devices. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `devicesId, enterprisesId` | Gets a web app. |
| `list` | `SELECT` | `enterprisesId` | Lists devices for a given enterprise. |
| `delete` | `DELETE` | `devicesId, enterprisesId` | Deletes a web app. |
| `issueCommand` | `EXEC` | `devicesId, enterprisesId` | Issues a command to a device. The Operation resource returned contains a Command in its metadata field. Use the get operation method to get the status of the command. |
| `patch` | `EXEC` | `devicesId, enterprisesId` | Updates a web app. |
