---
title: security_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_rules
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
<tr><td><b>Name</b></td><td><code>security_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.security_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `description` | `string` | A description for this rule. Restricted to 140 chars. |
| `destinationPortRange` | `string` | The destination port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports. |
| `sourceAddressPrefix` | `string` | The CIDR or source IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. If this is an ingress rule, specifies where network traffic originates from. |
| `destinationAddressPrefix` | `string` | The destination address prefix. CIDR or destination IP range. Asterisk '*' can also be used to match all source IPs. Default tags such as 'VirtualNetwork', 'AzureLoadBalancer' and 'Internet' can also be used. |
| `protocol` | `string` | Network protocol this rule applies to. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `sourceApplicationSecurityGroups` | `array` | The application security group specified as source. |
| `destinationAddressPrefixes` | `array` | The destination address prefixes. CIDR or destination IP ranges. |
| `sourcePortRange` | `string` | The source port or range. Integer or range between 0 and 65535. Asterisk '*' can also be used to match all ports. |
| `priority` | `integer` | The priority of the rule. The value can be between 100 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule. |
| `destinationPortRanges` | `array` | The destination port ranges. |
| `sourcePortRanges` | `array` | The source port ranges. |
| `destinationApplicationSecurityGroups` | `array` | The application security group specified as destination. |
| `type` | `string` | The type of the resource. |
| `direction` | `string` | The direction of the rule. The direction specifies if rule will be evaluated on incoming or outgoing traffic. |
| `sourceAddressPrefixes` | `array` | The CIDR or source IP ranges. |
| `access` | `string` | Whether network traffic is allowed or denied. |
| `provisioningState` | `string` | The current provisioning state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SecurityRules_List` | `SELECT` | `networkSecurityGroupName, resourceGroupName, subscriptionId` | Gets all security rules in a network security group. |
| `SecurityRules_CreateOrUpdate` | `INSERT` | `networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId` | Creates or updates a security rule in the specified network security group. |
| `SecurityRules_Delete` | `DELETE` | `networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId` | Deletes the specified network security rule. |
| `SecurityRules_Get` | `EXEC` | `networkSecurityGroupName, resourceGroupName, securityRuleName, subscriptionId` | Get the specified network security rule. |