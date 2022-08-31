---
title: delegation_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - delegation_settings
  - api_management
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
<tr><td><b>Name</b></td><td><code>delegation_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.delegation_settings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DelegationSettings_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create or Update Delegation settings. |
| `DelegationSettings_Get` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Get Delegation Settings for the Portal. |
| `DelegationSettings_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the DelegationSettings. |
| `DelegationSettings_ListSecrets` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the secret validation key of the DelegationSettings. |
| `DelegationSettings_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId` | Update Delegation settings. |
