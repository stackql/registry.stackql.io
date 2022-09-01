---
title: connection_monitor_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitor_tests
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
<tr><td><b>Name</b></td><td><code>connection_monitor_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.connection_monitor_tests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `destinationPort` | `integer` | The Connection Monitor test destination port |
| `type` | `string` | The type of the resource. |
| `sourceAgent` | `string` | The Connection Monitor test source agent |
| `isTestSuccessful` | `boolean` | The flag that indicates if the Connection Monitor test is successful or not. |
| `provisioningState` | `string` | The provisioning state of the resource. |
| `testFrequencyInSec` | `integer` | The Connection Monitor test frequency in seconds |
| `destination` | `string` | The Connection Monitor test destination |
| `path` | `array` | The path representing the Connection Monitor test. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ConnectionMonitorTests_ListByPeeringService` | `SELECT` | `peeringServiceName, resourceGroupName, subscriptionId` | Lists all connection monitor tests under the given subscription, resource group and peering service. |
| `ConnectionMonitorTests_CreateOrUpdate` | `INSERT` | `connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId` | Creates or updates a connection monitor test with the specified name under the given subscription, resource group and peering service. |
| `ConnectionMonitorTests_Delete` | `DELETE` | `connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId` | Deletes an existing connection monitor test with the specified name under the given subscription, resource group and peering service. |
| `ConnectionMonitorTests_Get` | `EXEC` | `connectionMonitorTestName, peeringServiceName, resourceGroupName, subscriptionId` | Gets an existing connection monitor test with the specified name under the given subscription, resource group and peering service. |
