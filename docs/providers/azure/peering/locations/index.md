---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - peering
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
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `country` | `string` | The country in which the peering location exists. |
| `peeringLocation` | `string` | The name of the peering location. |
| `azureRegion` | `string` | The Azure region associated with the peering location. |
| `direct` | `object` | The properties that define a direct peering location. |
| `type` | `string` | The type of the resource. |
| `exchange` | `object` | The properties that define an exchange peering location. |
| `kind` | `string` | The kind of peering that the peering location supports. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PeeringLocations_List` | `SELECT` | `kind, subscriptionId` |