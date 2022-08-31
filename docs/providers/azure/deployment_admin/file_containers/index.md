---
title: file_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - file_containers
  - deployment_admin
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>file_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.deployment_admin.file_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `provisioningState` | `string` | Provisioning state of the resource. |
| `type` | `string` | Type of Resource. |
| `error` | `object` | Extended Error Information. |
| `fileContainerId` | `string` | File container resource identifier containing product manifest. |
| `location` | `string` | Location of the resource. |
| `postCopyAction` | `string` | Specifies the file post copy action. |
| `uri` | `string` | The file or container Uri. This is read-only property; a user cannot set it. |
| `sourceUri` | `string` | Specifies The remote file location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FileContainers_List` | `SELECT` | `subscriptionId` | Returns an array of file containers. |
| `FileContainers_Create` | `INSERT` | `fileContainerId, subscriptionId` | Creates a new file container. |
| `FileContainers_Delete` | `DELETE` | `fileContainerId, subscriptionId` | Delete an existing file container. |
| `FileContainers_Get` | `EXEC` | `fileContainerId, subscriptionId` | Retrieves the specific file container details. |
