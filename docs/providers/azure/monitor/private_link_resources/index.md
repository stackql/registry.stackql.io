---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - monitor
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `requiredZoneNames` | `array` | The private link resource Private link DNS zone name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `requiredMembers` | `array` | The private link resource required member names. |
| `type` | `string` | Azure resource type |
| `groupId` | `string` | The private link resource group id. |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PrivateLinkResources_ListByPrivateLinkScope` | `SELECT` | `resourceGroupName, scopeName, subscriptionId` |
| `PrivateLinkResources_Get` | `EXEC` | `groupName, resourceGroupName, scopeName, subscriptionId` |
