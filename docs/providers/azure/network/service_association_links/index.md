---
title: service_association_links
hide_title: false
hide_table_of_contents: false
keywords:
  - service_association_links
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
<tr><td><b>Name</b></td><td><code>service_association_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.service_association_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `link` | `string` | Link to the external resource. |
| `provisioningState` | `string` | The current provisioning state. |
| `linkedResourceType` | `string` | Resource type of the linked resource. |
| `type` | `string` | Resource type. |
| `allowDelete` | `boolean` | If true, the resource can be deleted. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `locations` | `array` | A list of locations. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ServiceAssociationLinks_List` | `SELECT` | `resourceGroupName, subnetName, subscriptionId, virtualNetworkName` |
