---
title: private_link_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resource
  - batch
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
<tr><td><b>Name</b></td><td><code>private_link_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.batch.private_link_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `requiredZoneNames` | `array` |  |
| `type` | `string` | The type of the resource. |
| `etag` | `string` | The ETag of the resource, used for concurrency statements. |
| `groupId` | `string` | The group id is used to establish the private link connection. |
| `requiredMembers` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkResource_ListByBatchAccount` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all of the private link resources in the specified account. |
| `PrivateLinkResource_Get` | `EXEC` | `accountName, privateLinkResourceName, resourceGroupName, subscriptionId` | Gets information about the specified private link resource. |
