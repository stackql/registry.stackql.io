---
title: partner_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_namespaces
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
<tr><td><b>Name</b></td><td><code>partner_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_grid.partner_namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `privateEndpointConnections` | `array` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `endpoint` | `string` | Endpoint for the partner namespace. |
| `inboundIpRules` | `array` | This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled. |
| `provisioningState` | `string` | Provisioning state of the partner namespace. |
| `tags` | `object` | Resource tags. |
| `disableLocalAuth` | `boolean` | This boolean is used to enable or disable local auth. Default value is false. When the property is set to true, only AAD token will be used to authenticate if user is allowed to publish to the partner namespace. |
| `partnerRegistrationFullyQualifiedId` | `string` | The fully qualified ARM Id of the partner registration that should be associated with this partner namespace. This takes the following format:<br />/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/Microsoft.EventGrid/partnerRegistrations/&#123;partnerRegistrationName&#125;. |
| `partnerTopicRoutingMode` | `string` | This determines if events published to this partner namespace should use the source attribute in the event payload<br />or use the channel name in the header when matching to the partner topic. If none is specified, source attribute routing will be used to match the partner topic. |
| `publicNetworkAccess` | `string` | This determines if traffic is allowed over public network. By default it is enabled.<br />You can further restrict to specific IPs by configuring &lt;seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.PartnerNamespaceProperties.InboundIpRules" /&gt; |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PartnerNamespaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all the partner namespaces under a resource group. |
| `PartnerNamespaces_ListBySubscription` | `SELECT` | `subscriptionId` | List all the partner namespaces under an Azure subscription. |
| `PartnerNamespaces_CreateOrUpdate` | `INSERT` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Asynchronously creates a new partner namespace with the specified parameters. |
| `PartnerNamespaces_Delete` | `DELETE` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Delete existing partner namespace. |
| `PartnerNamespaces_Get` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Get properties of a partner namespace. |
| `PartnerNamespaces_ListSharedAccessKeys` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | List the two keys used to publish to a partner namespace. |
| `PartnerNamespaces_RegenerateKey` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a partner namespace. |
| `PartnerNamespaces_Update` | `EXEC` | `partnerNamespaceName, resourceGroupName, subscriptionId` | Asynchronously updates a partner namespace with the specified parameters. |
