---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - event_grid
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | Provisioning state of the Event Grid Domain Resource. |
| `disableLocalAuth` | `boolean` | This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the domain. |
| `autoDeleteTopicWithLastSubscription` | `boolean` | This Boolean is used to specify the deletion mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource.
| `inboundIpRules` | `array` | This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled. |
| `autoCreateTopicWithFirstSubscription` | `boolean` | This Boolean is used to specify the creation mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource.
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `privateEndpointConnections` | `array` | List of private endpoint connections. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `inputSchema` | `string` | This determines the format that Event Grid should expect for incoming events published to the Event Grid Domain Resource. |
| `publicNetworkAccess` | `string` | This determines if traffic is allowed over public network. By default it is enabled.
| `tags` | `object` | Resource tags. |
| `inputSchemaMapping` | `object` | By default, Event Grid expects events to be in the Event Grid event schema. Specifying an input schema mapping enables publishing to Event Grid using a custom input schema. Currently, the only supported type of InputSchemaMapping is 'JsonInputSchemaMapping'. |
| `metricResourceId` | `string` | Metric resource id for the Event Grid Domain Resource. |
| `dataResidencyBoundary` | `string` | Data Residency Boundary of the resource. |
| `endpoint` | `string` | Endpoint for the Event Grid Domain Resource which is used for publishing the events. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Domains_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the domains under a resource group. |
| `Domains_ListBySubscription` | `SELECT` | `subscriptionId` | List all the domains under an Azure subscription. |
| `Domains_CreateOrUpdate` | `INSERT` | `domainName, resourceGroupName, subscriptionId` | Asynchronously creates or updates a new domain with the specified parameters. |
| `Domains_Delete` | `DELETE` | `domainName, resourceGroupName, subscriptionId` | Delete existing domain. |
| `Domains_Get` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Get properties of a domain. |
| `Domains_ListSharedAccessKeys` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | List the two keys used to publish to a domain. |
| `Domains_RegenerateKey` | `EXEC` | `domainName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a domain. |
| `Domains_Update` | `EXEC` | `domainName, resourceGroupName, subscriptionId` | Asynchronously updates a domain with the specified parameters. |