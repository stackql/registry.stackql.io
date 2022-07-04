---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudidentity.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device}`, where device is the unique id assigned to the Device. |
| `lastSyncTime` | `string` | Most recent time when device synced with this service. |
| `assetTag` | `string` | Asset tag of the device. |
| `meid` | `string` | Output only. MEID number of device if CDMA device; empty otherwise. |
| `kernelVersion` | `string` | Output only. Kernel version of the device. |
| `wifiMacAddresses` | `array` | WiFi MAC addresses of device. |
| `encryptionState` | `string` | Output only. Device encryption state. |
| `manufacturer` | `string` | Output only. Device manufacturer. Example: Motorola. |
| `buildNumber` | `string` | Output only. Build number of the device. |
| `networkOperator` | `string` | Output only. Mobile or network operator of device, if available. |
| `compromisedState` | `string` | Output only. Represents whether the Device is compromised. |
| `enabledUsbDebugging` | `boolean` | Output only. Whether USB debugging is enabled on device. |
| `ownerType` | `string` | Output only. Whether the device is owned by the company or an individual |
| `deviceId` | `string` | Unique identifier for the device. |
| `bootloaderVersion` | `string` | Output only. Device bootloader version. Example: 0.6.7. |
| `otherAccounts` | `array` | Output only. Domain name for Google accounts on device. Type for other accounts on device. On Android, will only be populated if \|ownership_privilege\| is \|PROFILE_OWNER\| or \|DEVICE_OWNER\|. Does not include the account signed in to the device policy app if that account's domain has only one account. Examples: "com.example", "xyz.com". |
| `enabledDeveloperOptions` | `boolean` | Output only. Whether developer options is enabled on device. |
| `osVersion` | `string` | Output only. OS version of the device. Example: Android 8.1.0. |
| `androidSpecificAttributes` | `object` | Resource representing the Android specific attributes of a Device. |
| `managementState` | `string` | Output only. Management state of the device |
| `model` | `string` | Output only. Model name of device. Example: Pixel 3. |
| `deviceType` | `string` | Output only. Type of device. |
| `basebandVersion` | `string` | Output only. Baseband version of the device. |
| `imei` | `string` | Output only. IMEI number of device if GSM device; empty otherwise. |
| `createTime` | `string` | Output only. When the Company-Owned device was imported. This field is empty for BYOD devices. |
| `brand` | `string` | Output only. Device brand. Example: Samsung. |
| `serialNumber` | `string` | Serial Number of device. Example: HT82V1A01076. |
| `securityPatchTime` | `string` | Output only. OS security patch update time on device. |
| `releaseVersion` | `string` | Output only. OS release version. Example: 6.0. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `devices_get` | `SELECT` | `name` | Retrieves the specified device. |
| `devices_list` | `SELECT` |  | Lists/Searches devices. |
| `devices_create` | `INSERT` |  | Creates a device. Only company-owned device may be created. **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium |
| `devices_delete` | `DELETE` | `name` | Deletes the specified device. |
| `devices_cancelWipe` | `EXEC` | `name` | Cancels an unfinished device wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped. This operation is possible when the device is in a "pending wipe" state. The device enters the "pending wipe" state when a wipe device command is issued, but has not yet been sent to the device. The cancel wipe will fail if the wipe command has already been issued to the device. |
| `devices_wipe` | `EXEC` | `name` | Wipes all data on the specified device. |