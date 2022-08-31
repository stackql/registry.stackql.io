---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_security.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `mergedToDeviceId` | `string` | The device Id that this device was merged into |
| `onboardingStatus` | `string` | Device onboarding status. |
| `hardware` | `object` | Device hardware data |
| `schemaVersion` | `string` | Version of the device model schema |
| `deviceTypeDisplayName` | `string` | Device type display name |
| `firstSeen` | `string` | First time the device was seen. |
| `deviceCategoryDisplayName` | `string` | Device category display name |
| `deviceTypeId` | `integer` | Device type id |
| `sensor` | `object` | Sensor that scanned the device |
| `deviceSubTypeDisplayName` | `string` | Device sub type display name |
| `packages` | `array` | List of device packages |
| `criticality` | `string` | Device criticality. |
| `nics` | `array` | List of the device network interface cards. |
| `parentDeviceId` | `string` | For nested device, this is the parent device id. |
| `operatingSystem` | `object` | Device operating system data |
| `parentRackNumber` | `integer` | For nested device, this is the rack number in the parent device that holds the nested device. |
| `authorizedState` | `string` | Authorized state of the device. |
| `lastUpdated` | `string` | Last time the device was updated by the profiler. |
| `lastProgrammingTime` | `string` | last time the device was programming or programed. |
| `parentSlotNumber` | `integer` | For nested device, this is the slot number in the parent device that holds the nested device. |
| `cpes` | `array` | List of Common Platform Enumeration (CPE) |
| `mergedDevices` | `array` | List of merged devices data |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `deviceDataSource` | `string` | Device data source |
| `firmwares` | `array` | List of device firmwares. |
| `programmingState` | `string` | Indicates whether this device is programming |
| `deviceStatus` | `string` | Device status. |
| `lastSeen` | `string` | Last time the device was seen. |
| `riskScore` | `integer` | risk score of the device. |
| `slots` | `array` | List of the device slot in the backplane |
| `deviceName` | `string` | Device name |
| `businessFunction` | `string` | Device business function |
| `deviceCategoryId` | `integer` | Device category id |
| `profilingConfidence` | `integer` | Confidence of the device profile |
| `additionalFields` | `object` |  A bag of fields which extends the device information. |
| `deviceTags` | `array` | Device tags |
| `purdueLevel` | `string` | Purdue level of the device. |
| `deviceSubTypeId` | `integer` | Device sub type id |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Devices_List` | `SELECT` | `deviceGroupName, iotDefenderLocation, subscriptionId` | List devices |
| `Devices_Get` | `EXEC` | `deviceGroupName, deviceId, iotDefenderLocation, subscriptionId` | Get device |
