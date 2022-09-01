---
title: azure_firewalls
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewalls
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
<tr><td><b>Name</b></td><td><code>azure_firewalls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.azure_firewalls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `ipGroups` | `array` | List of IpGroups associated with azure firewall. |
| `location` | `string` | Resource location. |
| `hubIPAddresses` | `object` | IP addresses associated with azure firewall. |
| `ipConfigurations` | `array` | IP configuration of the Azure Firewall resource. |
| `sku` | `object` | SKU of an Azure Firewall. |
| `virtualHub` | `object` | Reference to another subresource. |
| `firewallPolicy` | `object` | Reference to another subresource. |
| `applicationRuleCollections` | `array` | Collection of application rule collections used by Azure Firewall. |
| `managementIpConfiguration` | `object` | IP configuration of an Azure Firewall. |
| `natRuleCollections` | `array` | Collection of NAT rule collections used by Azure Firewall. |
| `networkRuleCollections` | `array` | Collection of network rule collections used by Azure Firewall. |
| `threatIntelMode` | `string` | The operation mode for Threat Intel. |
| `additionalProperties` | `object` | The additional properties of azure firewall. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AzureFirewalls_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Azure Firewalls in a resource group. |
| `AzureFirewalls_ListAll` | `SELECT` | `subscriptionId` | Gets all the Azure Firewalls in a subscription. |
| `AzureFirewalls_CreateOrUpdate` | `INSERT` | `azureFirewallName, resourceGroupName, subscriptionId` | Creates or updates the specified Azure Firewall. |
| `AzureFirewalls_Delete` | `DELETE` | `azureFirewallName, resourceGroupName, subscriptionId` | Deletes the specified Azure Firewall. |
| `AzureFirewalls_Get` | `EXEC` | `azureFirewallName, resourceGroupName, subscriptionId` | Gets the specified Azure Firewall. |
| `AzureFirewalls_ListLearnedPrefixes` | `EXEC` | `azureFirewallName, resourceGroupName, subscriptionId` | Retrieves a list of all IP prefixes that azure firewall has learned to not SNAT. |
| `AzureFirewalls_UpdateTags` | `EXEC` | `azureFirewallName, resourceGroupName, subscriptionId` | Updates tags of an Azure Firewall resource. |
