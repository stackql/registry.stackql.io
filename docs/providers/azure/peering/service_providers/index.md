---
title: service_providers
hide_title: false
hide_table_of_contents: false
keywords:
  - service_providers
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
<tr><td><b>Name</b></td><td><code>service_providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.service_providers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `peeringLocations` | `array` | The list of locations at which the service provider peers with Microsoft. |
| `serviceProviderName` | `string` | The name of the service provider. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `PeeringServiceProviders_List` | `SELECT` | `subscriptionId` |
