---
title: network_firewall_policies_association
hide_title: false
hide_table_of_contents: false
keywords:
  - network_firewall_policies_association
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_firewall_policies_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.network_firewall_policies_association</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name for an association. |
| `attachmentTarget` | `string` | The target that the firewall policy is attached to. |
| `displayName` | `string` | [Output Only] Deprecated, please use short name instead. The display name of the firewall policy of the association. |
| `firewallPolicyId` | `string` | [Output Only] The firewall policy ID of the association. |
| `shortName` | `string` | [Output Only] The short name of the firewall policy of the association. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `networkFirewallPolicies_getAssociation` | `SELECT` | `firewallPolicy, project` | Gets an association with the specified name. |
| `networkFirewallPolicies_addAssociation` | `INSERT` | `firewallPolicy, project` | Inserts an association for the specified firewall policy. |
| `networkFirewallPolicies_removeAssociation` | `DELETE` | `firewallPolicy, project` | Removes an association for the specified firewall policy. |
