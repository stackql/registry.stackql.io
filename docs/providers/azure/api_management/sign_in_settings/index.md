---
title: sign_in_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sign_in_settings
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
<tr><td><b>Name</b></td><td><code>sign_in_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.sign_in_settings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SignInSettings_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create or Update Sign-In settings. |
| `SignInSettings_Get` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Get Sign In Settings for the Portal |
| `SignInSettings_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the SignInSettings. |
| `SignInSettings_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId` | Update Sign-In settings. |
