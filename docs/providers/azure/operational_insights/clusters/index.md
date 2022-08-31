---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `createdDate` | `string` | The cluster creation time |
| `provisioningState` | `string` | The provisioning state of the cluster. |
| `isDoubleEncryptionEnabled` | `boolean` | Configures whether cluster will use double encryption. This Property can not be modified after cluster creation. Default value is 'true' |
| `clusterId` | `string` | The ID associated with the cluster. |
| `capacityReservationProperties` | `object` | The Capacity Reservation properties. |
| `lastModifiedDate` | `string` | The last time the cluster was updated. |
| `associatedWorkspaces` | `array` | The list of Log Analytics workspaces associated with the cluster |
| `billingType` | `string` | Configures whether billing will be only on the cluster or each workspace will be billed by its proportional use. This does not change the overall billing, only how it will be distributed. Default value is 'Cluster' |
| `keyVaultProperties` | `object` | The key vault properties. |
| `sku` | `object` | The cluster sku definition. |
| `isAvailabilityZonesEnabled` | `boolean` | Sets whether the cluster will support availability zones. This can be set as true only in regions where Azure Data Explorer support Availability Zones. This Property can not be modified after cluster creation. Default value is 'true' if region supports Availability Zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Clusters_List` | `SELECT` | `subscriptionId` | Gets the Log Analytics clusters in a subscription. |
| `Clusters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets Log Analytics clusters in a resource group. |
| `Clusters_CreateOrUpdate` | `INSERT` | `clusterName, resourceGroupName, subscriptionId` | Create or update a Log Analytics cluster. |
| `Clusters_Delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a cluster instance. |
| `Clusters_Get` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets a Log Analytics cluster instance. |
| `Clusters_Update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Updates a Log Analytics cluster. |
