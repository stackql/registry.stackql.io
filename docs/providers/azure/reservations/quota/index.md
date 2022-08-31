---
title: quota
hide_title: false
hide_table_of_contents: false
keywords:
  - quota
  - reservations
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
<tr><td><b>Name</b></td><td><code>quota</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.reservations.quota</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The quota request ID. |
| `name` | `string` | The name of the quota request. |
| `type` | `string` | Type of resource. "Microsoft.Capacity/ServiceLimits" |
| `properties` | `object` | Quota properties for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Quota_List` | `SELECT` | `location, providerId, subscriptionId` | Gets a list of current quotas (service limits) and usage for all resources. The response from the list quota operation can be leveraged to request quota updates. |
| `Quota_CreateOrUpdate` | `INSERT` | `location, providerId, resourceName, subscriptionId` | Create or update the quota (service limits) of a resource to the requested value.<br /> Steps:
| `Quota_Get` | `EXEC` | `location, providerId, resourceName, subscriptionId` | Get the current quota (service limit) and usage of a resource. You can use the response from the GET operation to submit quota update request. |
| `Quota_Update` | `EXEC` | `location, providerId, resourceName, subscriptionId` | Update the quota (service limits) of this resource to the requested value.