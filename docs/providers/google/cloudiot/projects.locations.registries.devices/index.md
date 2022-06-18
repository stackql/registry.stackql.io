---
title: projects.locations.registries.devices
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>projects.locations.registries.devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudiot.projects.locations.registries.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `devices` | `array` | The devices that match the request. |
| `nextPageToken` | `string` | If not empty, indicates that there may be more devices that match the request; this value should be passed in a new `ListDevicesRequest`. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `devicesId, locationsId, projectsId, registriesId` | Gets details about a device. |
| `list` | `SELECT` | `locationsId, projectsId, registriesId` | List devices in a device registry. |
| `create` | `INSERT` | `locationsId, projectsId, registriesId` | Creates a device in a device registry. |
| `delete` | `DELETE` | `devicesId, locationsId, projectsId, registriesId` | Deletes a device. |
| `modifyCloudToDeviceConfig` | `EXEC` | `devicesId, locationsId, projectsId, registriesId` | Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata. |
| `patch` | `EXEC` | `devicesId, locationsId, projectsId, registriesId` | Updates a device. |
| `sendCommandToDevice` | `EXEC` | `devicesId, locationsId, projectsId, registriesId` | Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device. |
