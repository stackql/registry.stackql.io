---
title: service_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_locations
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
<tr><td><b>Name</b></td><td><code>service_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.service_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `state` | `string` | State of the customer |
| `type` | `string` | The type of the resource. |
| `azureRegion` | `string` | Azure region for the location |
| `country` | `string` | Country of the customer |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PeeringServiceLocations_List` | `SELECT` | `subscriptionId` |
