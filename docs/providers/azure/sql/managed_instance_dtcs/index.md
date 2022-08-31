---
title: managed_instance_dtcs
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instance_dtcs
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
<tr><td><b>Name</b></td><td><code>managed_instance_dtcs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instance_dtcs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `securitySettings` | `object` | The Security Settings of managed instance DTC. |
| `dtcEnabled` | `boolean` | Active status of managed instance DTC. |
| `dtcHostNameDnsSuffix` | `string` | Host name dns suffix of managed instance DTC. |
| `externalDnsSuffixSearchList` | `array` | External dns suffix search list of managed instance DTC. |
| `provisioningState` | `string` | Provisioning state of managed instance DTC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstanceDtcs_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed instance DTC settings. |
| `ManagedInstanceDtcs_CreateOrUpdate` | `INSERT` | `dtcName, managedInstanceName, resourceGroupName, subscriptionId` | Updates managed instance DTC settings. |
| `ManagedInstanceDtcs_Get` | `EXEC` | `dtcName, managedInstanceName, resourceGroupName, subscriptionId` | Gets managed instance DTC settings. |
