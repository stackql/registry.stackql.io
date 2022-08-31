---
title: device_security_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_security_groups
  - security
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
<tr><td><b>Name</b></td><td><code>device_security_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.device_security_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `allowlistRules` | `array` | The allow-list custom alert rules. |
| `denylistRules` | `array` | The deny-list custom alert rules. |
| `thresholdRules` | `array` | The list of custom alert threshold rules. |
| `timeWindowRules` | `array` | The list of custom alert time-window rules. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeviceSecurityGroups_List` | `SELECT` | `api-version, resourceId` | Use this method get the list of device security groups for the specified IoT Hub resource. |
| `DeviceSecurityGroups_CreateOrUpdate` | `INSERT` | `api-version, deviceSecurityGroupName, resourceId` | Use this method to creates or updates the device security group on a specified IoT Hub resource. |
| `DeviceSecurityGroups_Delete` | `DELETE` | `api-version, deviceSecurityGroupName, resourceId` | User this method to deletes the device security group. |
| `DeviceSecurityGroups_Get` | `EXEC` | `api-version, deviceSecurityGroupName, resourceId` | Use this method to get the device security group for the specified IoT Hub resource. |