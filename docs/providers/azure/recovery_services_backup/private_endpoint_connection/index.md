---
title: private_endpoint_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connection
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.private_endpoint_connection</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnection_Delete` | `DELETE` | `api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName` | Delete Private Endpoint requests. This call is made by Backup Admin. |
| `PrivateEndpointConnection_Get` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName` | Get Private Endpoint Connection. This call is made by Backup Admin. |
| `PrivateEndpointConnection_Put` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, subscriptionId, vaultName` | Approve or Reject Private Endpoint requests. This call is made by Backup Admin. |
