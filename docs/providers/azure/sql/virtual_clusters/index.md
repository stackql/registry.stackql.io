---
title: virtual_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_clusters
  - sql
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
<tr><td><b>Name</b></td><td><code>virtual_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.virtual_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `childResources` | `array` | List of resources in this virtual cluster. |
| `family` | `string` | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| `location` | `string` | Resource location. |
| `maintenanceConfigurationId` | `string` | Specifies maintenance configuration id to apply to this virtual cluster. |
| `subnetId` | `string` | Subnet resource ID for the virtual cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualClusters_List` | `SELECT` | `subscriptionId` | Gets a list of all virtualClusters in the subscription. |
| `VirtualClusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of virtual clusters in a resource group. |
| `VirtualClusters_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualClusterName` | Deletes a virtual cluster. |
| `VirtualClusters_Get` | `EXEC` | `resourceGroupName, subscriptionId, virtualClusterName` | Gets a virtual cluster. |
| `VirtualClusters_Update` | `EXEC` | `resourceGroupName, subscriptionId, virtualClusterName` | Updates a virtual cluster. |
| `VirtualClusters_UpdateDnsServers` | `EXEC` | `resourceGroupName, subscriptionId, virtualClusterName` | Synchronizes the DNS server settings used by the managed instances inside the given virtual cluster. |