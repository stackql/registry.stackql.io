---
title: web_pub_sub
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub
  - web_pub_sub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pub_sub.web_pub_sub</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The GEO location of the resource. e.g. West US \| East US \| North Central US \| South Central US. |
| `networkACLs` | `object` | Network ACLs for the resource |
| `provisioningState` | `string` | Provisioning state of the resource. |
| `disableLocalAuth` | `boolean` | DisableLocalAuth<br />Enable or disable local auth with AccessKey<br />When set as true, connection with AccessKey=xxx won't work. |
| `disableAadAuth` | `boolean` | DisableLocalAuth<br />Enable or disable aad auth<br />When set as true, connection with AuthType=aad won't work. |
| `sharedPrivateLinkResources` | `array` | The list of shared private link resources. |
| `tags` | `object` | Tags of the service which is a list of key value pairs that describe the resource. |
| `tls` | `object` | TLS settings for the resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `privateEndpointConnections` | `array` | Private endpoint connections to the resource. |
| `hostName` | `string` | FQDN of the service instance. |
| `serverPort` | `integer` | The publicly accessible port of the resource which is designed for customer server side usage. |
| `sku` | `object` | The billing information of the resource. |
| `identity` | `object` | A class represent managed identities used for request and response |
| `hostNamePrefix` | `string` | Deprecated. |
| `liveTraceConfiguration` | `object` | Live trace configuration of a Microsoft.SignalRService resource. |
| `publicPort` | `integer` | The publicly accessible port of the resource which is designed for browser/client side usage. |
| `publicNetworkAccess` | `string` | Enable or disable public network access. Default to "Enabled".<br />When it's Enabled, network ACLs still apply.<br />When it's Disabled, public network access is always disabled no matter what you set in network ACLs. |
| `externalIP` | `string` | The publicly accessible IP of the resource. |
| `version` | `string` | Version of the resource. Probably you need the same or higher version of client SDKs. |
| `resourceLogConfiguration` | `object` | Resource log configuration of a Microsoft.SignalRService resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebPubSub_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `WebPubSub_ListBySubscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `WebPubSub_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update a resource. |
| `WebPubSub_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Operation to delete a resource. |
| `WebPubSub_CheckNameAvailability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the resource name is valid and is not already in use. |
| `WebPubSub_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the resource and its properties. |
| `WebPubSub_ListKeys` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the access keys of the resource. |
| `WebPubSub_ListSkus` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | List all available skus of the resource. |
| `WebPubSub_RegenerateKey` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| `WebPubSub_Restart` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to restart a resource. |
| `WebPubSub_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to update an exiting resource. |
