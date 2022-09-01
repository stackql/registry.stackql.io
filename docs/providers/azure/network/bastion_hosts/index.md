---
title: bastion_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - bastion_hosts
  - network
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
<tr><td><b>Name</b></td><td><code>bastion_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.bastion_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `enableFileCopy` | `boolean` | Enable/Disable File Copy feature of the Bastion Host resource. |
| `enableIpConnect` | `boolean` | Enable/Disable IP Connect feature of the Bastion Host resource. |
| `location` | `string` | Resource location. |
| `dnsName` | `string` | FQDN for the endpoint on which bastion host is accessible. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `disableCopyPaste` | `boolean` | Enable/Disable Copy/Paste feature of the Bastion Host resource. |
| `sku` | `object` | The sku of this Bastion Host. |
| `type` | `string` | Resource type. |
| `ipConfigurations` | `array` | IP configuration of the Bastion Host resource. |
| `enableTunneling` | `boolean` | Enable/Disable Tunneling feature of the Bastion Host resource. |
| `scaleUnits` | `integer` | The scale units for the Bastion Host resource. |
| `enableShareableLink` | `boolean` | Enable/Disable Shareable Link of the Bastion Host resource. |
| `tags` | `object` | Resource tags. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BastionHosts_List` | `SELECT` | `subscriptionId` | Lists all Bastion Hosts in a subscription. |
| `BastionHosts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Bastion Hosts in a resource group. |
| `BastionHosts_CreateOrUpdate` | `INSERT` | `bastionHostName, resourceGroupName, subscriptionId` | Creates or updates the specified Bastion Host. |
| `BastionHosts_Delete` | `DELETE` | `bastionHostName, resourceGroupName, subscriptionId` | Deletes the specified Bastion Host. |
| `BastionHosts_Get` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Gets the specified Bastion Host. |
| `BastionHosts_UpdateTags` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Updates Tags for BastionHost resource |
| `DeleteBastionShareableLink` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Deletes the Bastion Shareable Links for all the VMs specified in the request. |
| `DisconnectActiveSessions` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Returns the list of currently active sessions on the Bastion. |
| `GetActiveSessions` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Returns the list of currently active sessions on the Bastion. |
| `GetBastionShareableLink` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Return the Bastion Shareable Links for all the VMs specified in the request. |
| `PutBastionShareableLink` | `EXEC` | `bastionHostName, resourceGroupName, subscriptionId` | Creates a Bastion Shareable Links for all the VMs specified in the request. |
