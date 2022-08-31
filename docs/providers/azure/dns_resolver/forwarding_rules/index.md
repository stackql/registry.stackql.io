---
title: forwarding_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - forwarding_rules
  - dns_resolver
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
<tr><td><b>Name</b></td><td><code>forwarding_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dns_resolver.forwarding_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | ETag of the forwarding rule. |
| `forwardingRuleState` | `string` | The state of forwarding rule. |
| `metadata` | `object` | Metadata attached to the forwarding rule. |
| `provisioningState` | `string` | The current provisioning state of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `targetDnsServers` | `array` | DNS servers to forward the DNS query to. |
| `domainName` | `string` | The domain name for the forwarding rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ForwardingRules_List` | `SELECT` | `dnsForwardingRulesetName, resourceGroupName, subscriptionId` | Lists forwarding rules in a DNS forwarding ruleset. |
| `ForwardingRules_CreateOrUpdate` | `INSERT` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Creates or updates a forwarding rule in a DNS forwarding ruleset. |
| `ForwardingRules_Delete` | `DELETE` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Deletes a forwarding rule in a DNS forwarding ruleset. WARNING: This operation cannot be undone. |
| `ForwardingRules_Get` | `EXEC` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Gets properties of a forwarding rule in a DNS forwarding ruleset. |
| `ForwardingRules_Update` | `EXEC` | `dnsForwardingRulesetName, forwardingRuleName, resourceGroupName, subscriptionId` | Updates a forwarding rule in a DNS forwarding ruleset. |
