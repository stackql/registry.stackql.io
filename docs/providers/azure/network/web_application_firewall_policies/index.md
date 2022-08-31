---
title: web_application_firewall_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - web_application_firewall_policies
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
<tr><td><b>Name</b></td><td><code>web_application_firewall_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.web_application_firewall_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `provisioningState` | `string` | The current provisioning state. |
| `type` | `string` | Resource type. |
| `managedRules` | `object` | Allow to exclude some variable satisfy the condition for the WAF check. |
| `httpListeners` | `array` | A collection of references to application gateway http listeners. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `resourceState` | `string` | Resource status of the policy. |
| `pathBasedRules` | `array` | A collection of references to application gateway path rules. |
| `customRules` | `array` | The custom rules inside the policy. |
| `tags` | `object` | Resource tags. |
| `policySettings` | `object` | Defines contents of a web application firewall global configuration. |
| `location` | `string` | Resource location. |
| `applicationGateways` | `array` | A collection of references to application gateways. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebApplicationFirewallPolicies_List` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the protection policies within a resource group. |
| `WebApplicationFirewallPolicies_ListAll` | `SELECT` | `subscriptionId` | Gets all the WAF policies in a subscription. |
| `WebApplicationFirewallPolicies_CreateOrUpdate` | `INSERT` | `policyName, resourceGroupName, subscriptionId` | Creates or update policy with specified rule set name within a resource group. |
| `WebApplicationFirewallPolicies_Delete` | `DELETE` | `policyName, resourceGroupName, subscriptionId` | Deletes Policy. |
| `WebApplicationFirewallPolicies_Get` | `EXEC` | `policyName, resourceGroupName, subscriptionId` | Retrieve protection policy with specified name within a resource group. |
