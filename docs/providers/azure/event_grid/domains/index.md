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
| `publicNetworkAccess` | `string` | This determines if traffic is allowed over public network. By default it is enabled.<br />You can further restrict to specific IPs by configuring &lt;seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.DomainProperties.InboundIpRules" /&gt; |
| `location` | `string` | The geo-location where the resource lives |
| `autoDeleteTopicWithLastSubscription` | `boolean` | This Boolean is used to specify the deletion mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource.<br />In this context, deletion of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true.<br />When this property is set to true, Event Grid is responsible of automatically deleting the domain topic when the last event subscription at the scope<br />of the domain topic is deleted. If this property is set to false, then the user needs to manually delete the domain topic when it is no longer needed<br />(e.g., when last event subscription is deleted and the resource needs to be cleaned up). The self-management mode can be used if the user wants full<br />control of when the domain topic needs to be deleted, while auto-managed mode provides the flexibility to perform less operations and manage fewer<br />resources by the user. |
| `identity` | `object` | The identity information for the resource. |
| `disableLocalAuth` | `boolean` | This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the domain. |
| `privateEndpointConnections` | `array` | List of private endpoint connections. |
| `inputSchemaMapping` | `object` | By default, Event Grid expects events to be in the Event Grid event schema. Specifying an input schema mapping enables publishing to Event Grid using a custom input schema. Currently, the only supported type of InputSchemaMapping is 'JsonInputSchemaMapping'. |
| `metricResourceId` | `string` | Metric resource id for the Event Grid Domain Resource. |
| `endpoint` | `string` | Endpoint for the Event Grid Domain Resource which is used for publishing the events. |
| `inboundIpRules` | `array` | This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled. |
| `inputSchema` | `string` | This determines the format that Event Grid should expect for incoming events published to the Event Grid Domain Resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `dataResidencyBoundary` | `string` | Data Residency Boundary of the resource. |
| `autoCreateTopicWithFirstSubscription` | `boolean` | This Boolean is used to specify the creation mechanism for 'all' the Event Grid Domain Topics associated with this Event Grid Domain resource.<br />In this context, creation of domain topic can be auto-managed (when true) or self-managed (when false). The default value for this property is true.<br />When this property is null or set to true, Event Grid is responsible of automatically creating the domain topic when the first event subscription is<br />created at the scope of the domain topic. If this property is set to false, then creating the first event subscription will require creating a domain topic<br />by the user. The self-management mode can be used if the user wants full control of when the domain topic is created, while auto-managed mode provides the<br />flexibility to perform less operations and manage fewer resources by the user. Also, note that in auto-managed creation mode, user is allowed to create the<br />domain topic on demand if needed. |
| `provisioningState` | `string` | Provisioning state of the Event Grid Domain Resource. |
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
