---
title: server_azure_ad_administrators
hide_title: false
hide_table_of_contents: false
keywords:
  - server_azure_ad_administrators
  - sql
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
<tr><td><b>Name</b></td><td><code>server_azure_ad_administrators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_azure_ad_administrators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `login` | `string` | Login name of the server administrator. |
| `sid` | `string` | SID (object ID) of the server administrator. |
| `tenantId` | `string` | Tenant ID of the administrator. |
| `administratorType` | `string` | Type of the sever administrator. |
| `azureADOnlyAuthentication` | `boolean` | Azure Active Directory only Authentication enabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAzureADAdministrators_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of Azure Active Directory administrators in a server. |
| `ServerAzureADAdministrators_CreateOrUpdate` | `INSERT` | `administratorName, resourceGroupName, serverName, subscriptionId` | Creates or updates an existing Azure Active Directory administrator. |
| `ServerAzureADAdministrators_Delete` | `DELETE` | `administratorName, resourceGroupName, serverName, subscriptionId` | Deletes the Azure Active Directory administrator with the given name. |
| `ServerAzureADAdministrators_Get` | `EXEC` | `administratorName, resourceGroupName, serverName, subscriptionId` | Gets a Azure Active Directory administrator. |