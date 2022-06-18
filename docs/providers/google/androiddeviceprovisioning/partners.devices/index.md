---
title: partners.devices
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
<tr><td><b>Name</b></td><td><code>partners.devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androiddeviceprovisioning.partners.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` | Output only. The API resource name in the format `partners/[PARTNER_ID]/devices/[DEVICE_ID]`. Assigned by the server. |
| `claims` | `array` | Output only. The provisioning claims for a device. Devices claimed for zero-touch enrollment have a claim with the type `SECTION_TYPE_ZERO_TOUCH`. Call `partners.devices.unclaim` or `partners.devices.unclaimAsync` to remove the device from zero-touch enrollment. |
| `configuration` | `string` | Not available to resellers. |
| `deviceId` | `string` | Output only. The ID of the device. Assigned by the server. |
| `deviceIdentifier` | `object` | Encapsulates hardware and product IDs to identify a manufactured device. To understand requirements on identifier sets, read [Identifiers](https://developers.google.com/zero-touch/guides/identifiers). |
| `deviceMetadata` | `object` | Metadata entries that can be attached to a `Device`. To learn more, read [Device metadata](https://developers.google.com/zero-touch/guides/metadata). |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `devicesId, partnersId` | Gets a device. |
| `claim` | `EXEC` | `partnersId` | Claims a device for a customer and adds it to zero-touch enrollment. If the device is already claimed by another customer, the call returns an error. |
| `claimAsync` | `EXEC` | `partnersId` | Claims a batch of devices for a customer asynchronously. Adds the devices to zero-touch enrollment. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). |
| `findByIdentifier` | `EXEC` | `partnersId` | Finds devices by hardware identifiers, such as IMEI. |
| `findByOwner` | `EXEC` | `partnersId` | Finds devices claimed for customers. The results only contain devices registered to the reseller that's identified by the `partnerId` argument. The customer's devices purchased from other resellers don't appear in the results. |
| `metadata` | `EXEC` | `devicesId, partnersId` | Updates reseller metadata associated with the device. |
| `unclaim` | `EXEC` | `partnersId` | Unclaims a device from a customer and removes it from zero-touch enrollment. |
| `unclaimAsync` | `EXEC` | `partnersId` | Unclaims a batch of devices for a customer asynchronously. Removes the devices from zero-touch enrollment. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). |
| `updateMetadataAsync` | `EXEC` | `partnersId` | Updates the reseller metadata attached to a batch of devices. This method updates devices asynchronously and returns an `Operation` that can be used to track progress. Read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). |
