---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - azure_stack_hci
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_stack_hci.extensions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | Provisioning state of the Extension proxy resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `aggregateState` | `string` | Aggregate state of Arc Extensions across the nodes in this HCI cluster. |
| `extensionParameters` | `object` | Describes the properties of a Machine Extension. This object mirrors the definition in HybridCompute. |
| `perNodeExtensionDetails` | `array` | State of Arc Extension in each of the nodes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Extensions_ListByArcSetting` | `SELECT` | `arcSettingName, clusterName, resourceGroupName, subscriptionId` | List all Extensions under ArcSetting resource. |
| `Extensions_Create` | `INSERT` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Create Extension for HCI cluster. |
| `Extensions_Delete` | `DELETE` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Delete particular Arc Extension of HCI Cluster. |
| `Extensions_Get` | `EXEC` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Get particular Arc Extension of HCI Cluster. |
| `Extensions_Update` | `EXEC` | `arcSettingName, clusterName, extensionName, resourceGroupName, subscriptionId` | Update Extension for HCI cluster. |
