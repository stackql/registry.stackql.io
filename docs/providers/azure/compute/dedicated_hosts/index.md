---
title: dedicated_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hosts
  - compute
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
<tr><td><b>Name</b></td><td><code>dedicated_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.dedicated_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `virtualMachines` | `array` | A list of references to all virtual machines in the Dedicated Host. |
| `location` | `string` | Resource location |
| `licenseType` | `string` | Specifies the software license type that will be applied to the VMs deployed on the dedicated host. &lt;br&gt;&lt;br&gt; Possible values are: &lt;br&gt;&lt;br&gt; **None** &lt;br&gt;&lt;br&gt; **Windows_Server_Hybrid** &lt;br&gt;&lt;br&gt; **Windows_Server_Perpetual** &lt;br&gt;&lt;br&gt; Default: **None** |
| `autoReplaceOnFailure` | `boolean` | Specifies whether the dedicated host should be replaced automatically in case of a failure. The value is defaulted to 'true' when not provided. |
| `tags` | `object` | Resource tags |
| `hostId` | `string` | A unique id generated and assigned to the dedicated host by the platform. &lt;br&gt;&lt;br&gt; Does not change throughout the lifetime of the host. |
| `instanceView` | `object` | The instance view of a dedicated host. |
| `platformFaultDomain` | `integer` | Fault domain of the dedicated host within a dedicated host group. |
| `timeCreated` | `string` | Specifies the time at which the Dedicated Host resource was created.&lt;br&gt;&lt;br&gt;Minimum api-version: 2022-03-01. |
| `provisioningState` | `string` | The provisioning state, which only appears in the response. |
| `sku` | `object` | Describes a virtual machine scale set sku. NOTE: If the new VM SKU is not supported on the hardware the scale set is currently on, you need to deallocate the VMs in the scale set before you modify the SKU name. |
| `provisioningTime` | `string` | The date when the host was first provisioned. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DedicatedHosts_ListByHostGroup` | `SELECT` | `hostGroupName, resourceGroupName, subscriptionId` | Lists all of the dedicated hosts in the specified dedicated host group. Use the nextLink property in the response to get the next page of dedicated hosts. |
| `DedicatedHosts_CreateOrUpdate` | `INSERT` | `hostGroupName, hostName, resourceGroupName, subscriptionId, data__sku` | Create or update a dedicated host . |
| `DedicatedHosts_Delete` | `DELETE` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Delete a dedicated host. |
| `DedicatedHosts_Get` | `EXEC` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Retrieves information about a dedicated host. |
| `DedicatedHosts_Restart` | `EXEC` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Restart the dedicated host. The operation will complete successfully once the dedicated host has restarted and is running. To determine the health of VMs deployed on the dedicated host after the restart check the Resource Health Center in the Azure Portal. Please refer to https://docs.microsoft.com/azure/service-health/resource-health-overview for more details. |
| `DedicatedHosts_Update` | `EXEC` | `hostGroupName, hostName, resourceGroupName, subscriptionId` | Update an dedicated host . |
