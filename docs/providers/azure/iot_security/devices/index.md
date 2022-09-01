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
| `additionalFields` | `object` |  A bag of fields which extends the device information. |
| `operatingSystem` | `object` | Device operating system data |
| `packages` | `array` | List of device packages |
| `deviceName` | `string` | Device name |
| `riskScore` | `integer` | risk score of the device. |
| `deviceStatus` | `string` | Device status. |
| `deviceCategoryDisplayName` | `string` | Device category display name |
| `deviceCategoryId` | `integer` | Device category id |
| `parentSlotNumber` | `integer` | For nested device, this is the slot number in the parent device that holds the nested device. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `onboardingStatus` | `string` | Device onboarding status. |
| `authorizedState` | `string` | Authorized state of the device. |
| `nics` | `array` | List of the device network interface cards. |
| `deviceSubTypeDisplayName` | `string` | Device sub type display name |
| `deviceTypeId` | `integer` | Device type id |
| `deviceTags` | `array` | Device tags |
| `profilingConfidence` | `integer` | Confidence of the device profile |
| `cpes` | `array` | List of Common Platform Enumeration (CPE) |
| `mergedDevices` | `array` | List of merged devices data |
| `purdueLevel` | `string` | Purdue level of the device. |
| `deviceSubTypeId` | `integer` | Device sub type id |
| `hardware` | `object` | Device hardware data |
| `lastProgrammingTime` | `string` | last time the device was programming or programed. |
| `parentDeviceId` | `string` | For nested device, this is the parent device id. |
| `schemaVersion` | `string` | Version of the device model schema |
| `deviceDataSource` | `string` | Device data source |
| `firstSeen` | `string` | First time the device was seen. |
| `lastUpdated` | `string` | Last time the device was updated by the profiler. |
| `lastSeen` | `string` | Last time the device was seen. |
| `criticality` | `string` | Device criticality. |
| `businessFunction` | `string` | Device business function |
| `firmwares` | `array` | List of device firmwares. |
| `slots` | `array` | List of the device slot in the backplane |
| `parentRackNumber` | `integer` | For nested device, this is the rack number in the parent device that holds the nested device. |
| `mergedToDeviceId` | `string` | The device Id that this device was merged into |
| `programmingState` | `string` | Indicates whether this device is programming |
| `deviceTypeDisplayName` | `string` | Device type display name |
| `sensor` | `object` | Sensor that scanned the device |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Devices_List` | `SELECT` | `deviceGroupName, iotDefenderLocation, subscriptionId` | List devices |
| `Devices_Get` | `EXEC` | `deviceGroupName, deviceId, iotDefenderLocation, subscriptionId` | Get device |
