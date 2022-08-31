---
title: firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policies
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
<tr><td><b>Name</b></td><td><code>firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.firewall_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `firewalls` | `array` | List of references to Azure Firewalls that this Firewall Policy is associated with. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `insights` | `object` | Firewall Policy Insights. |
| `ruleCollectionGroups` | `array` | List of references to FirewallPolicyRuleCollectionGroups. |
| `sku` | `object` | SKU of Firewall policy. |
| `provisioningState` | `string` | The current provisioning state. |
| `location` | `string` | Resource location. |
| `explicitProxy` | `object` | Explicit Proxy Settings in Firewall Policy. |
| `threatIntelMode` | `string` | The operation mode for Threat Intel. |
| `sql` | `object` | SQL Settings in Firewall Policy. |
| `snat` | `object` | The private IP addresses/IP ranges to which traffic will not be SNAT. |
| `identity` | `object` | Identity for the resource. |
| `transportSecurity` | `object` | Configuration needed to perform TLS termination & initiation. |
| `intrusionDetection` | `object` | Configuration for intrusion detection mode and rules. |
| `threatIntelWhitelist` | `object` | ThreatIntel Whitelist for Firewall Policy. |
| `type` | `string` | Resource type. |
| `childPolicies` | `array` | List of references to Child Firewall Policies. |
| `dnsSettings` | `object` | DNS Proxy Settings in Firewall Policy. |
| `basePolicy` | `object` | Reference to another subresource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FirewallPolicies_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Firewall Policies in a resource group. |
| `FirewallPolicies_ListAll` | `SELECT` | `subscriptionId` | Gets all the Firewall Policies in a subscription. |
| `FirewallPolicies_CreateOrUpdate` | `INSERT` | `firewallPolicyName, resourceGroupName, subscriptionId` | Creates or updates the specified Firewall Policy. |
| `FirewallPolicies_Delete` | `DELETE` | `firewallPolicyName, resourceGroupName, subscriptionId` | Deletes the specified Firewall Policy. |
| `FirewallPolicies_Get` | `EXEC` | `firewallPolicyName, resourceGroupName, subscriptionId` | Gets the specified Firewall Policy. |
| `FirewallPolicies_UpdateTags` | `EXEC` | `firewallPolicyName, resourceGroupName, subscriptionId` | Updates tags of a Azure Firewall Policy resource. |
