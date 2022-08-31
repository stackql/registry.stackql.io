---
title: azure_firewall_fqdn_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_firewall_fqdn_tags
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
<tr><td><b>Name</b></td><td><code>azure_firewall_fqdn_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.azure_firewall_fqdn_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `fqdnTagName` | `string` | The name of this FQDN Tag. |
| `location` | `string` | Resource location. |
| `provisioningState` | `string` | The current provisioning state. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AzureFirewallFqdnTags_ListAll` | `SELECT` | `subscriptionId` |