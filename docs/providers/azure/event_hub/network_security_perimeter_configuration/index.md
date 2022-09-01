---
title: network_security_perimeter_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - network_security_perimeter_configuration
  - event_hub
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
<tr><td><b>Name</b></td><td><code>network_security_perimeter_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.event_hub.network_security_perimeter_configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `networkSecurityPerimeter` | `object` | NetworkSecurityPerimeter related information |
| `profile` | `object` | Information about current network profile |
| `provisioningIssues` | `array` | List of Provisioning Issues if any |
| `provisioningState` | `string` | Provisioning state of NetworkSecurityPerimeter configuration propagation |
| `resourceAssociation` | `object` | Information about resource association |
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `NetworkSecurityPerimeterConfiguration_List` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` |
