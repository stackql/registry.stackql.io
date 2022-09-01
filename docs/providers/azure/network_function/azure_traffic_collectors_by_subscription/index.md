---
title: azure_traffic_collectors_by_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_traffic_collectors_by_subscription
  - network_function
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
<tr><td><b>Name</b></td><td><code>azure_traffic_collectors_by_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_function.azure_traffic_collectors_by_subscription</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `virtualHub` | `object` | Resource reference properties. |
| `provisioningState` | `string` | The current provisioning state. |
| `location` | `string` | Resource location. |
| `collectorPolicies` | `array` | Collector Policies for Azure Traffic Collector. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `tags` | `object` | Resource tags. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `AzureTrafficCollectorsBySubscription_List` | `SELECT` | `subscriptionId` |
