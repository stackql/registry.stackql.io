---
title: sensors
hide_title: false
hide_table_of_contents: false
keywords:
  - sensors
  - iot_security
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
<tr><td><b>Name</b></td><td><code>sensors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_security.sensors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `tiStatus` | `string` | TI Status of the IoT sensor |
| `connectivityTime` | `string` | Last connectivity time of the IoT sensor |
| `learningMode` | `boolean` | Learning mode status of the IoT sensor |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `tiVersion` | `string` | TI Version of the IoT sensor |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `sensorVersion` | `string` | Version of the IoT sensor |
| `tiAutomaticUpdates` | `boolean` | TI Automatic mode status of the IoT sensor |
| `sensorType` | `string` | Type of sensor |
| `dynamicLearning` | `boolean` | Dynamic mode status of the IoT sensor |
| `zone` | `string` | Zone of the IoT sensor |
| `sensorStatus` | `string` | Status of the IoT sensor |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Sensors_List` | `SELECT` | `scope` | List IoT sensors |
| `Sensors_CreateOrUpdate` | `INSERT` | `scope, sensorName` | Create or update IoT sensor |
| `Sensors_Delete` | `DELETE` | `scope, sensorName` | Delete IoT sensor |
| `Sensors_DownloadActivation` | `EXEC` | `scope, sensorName` | Download sensor activation file |
| `Sensors_DownloadResetPassword` | `EXEC` | `scope, sensorName` | Download file for reset password of the sensor |
| `Sensors_Get` | `EXEC` | `scope, sensorName` | Get IoT sensor |
| `Sensors_TriggerTiPackageUpdate` | `EXEC` | `scope, sensorName` | Trigger threat intelligence package update |
