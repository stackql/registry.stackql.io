---
title: firewall_policy_rule_collection_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_rule_collection_groups
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
<tr><td><b>Name</b></td><td><code>firewall_policy_rule_collection_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.firewall_policy_rule_collection_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `priority` | `integer` | Priority of the Firewall Policy Rule Collection Group resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `ruleCollections` | `array` | Group of Firewall Policy rule collections. |
| `type` | `string` | Rule Group type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallPolicyRuleCollectionGroups_List` | `SELECT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Lists all FirewallPolicyRuleCollectionGroups in a FirewallPolicy resource. |
| `FirewallPolicyRuleCollectionGroups_CreateOrUpdate` | `INSERT` | `firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId` | Creates or updates the specified FirewallPolicyRuleCollectionGroup. |
| `FirewallPolicyRuleCollectionGroups_Delete` | `DELETE` | `firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId` | Deletes the specified FirewallPolicyRuleCollectionGroup. |
| `FirewallPolicyRuleCollectionGroups_Get` | `EXEC` | `firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId` | Gets the specified FirewallPolicyRuleCollectionGroup. |
