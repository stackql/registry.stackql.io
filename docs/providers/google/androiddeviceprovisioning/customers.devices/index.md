---
title: customers.devices
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
<tr><td><b>Name</b></td><td><code>customers.devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androiddeviceprovisioning.customers.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `devices` | `array` | The customer's devices. |
| `nextPageToken` | `string` | A token used to access the next page of results. Omitted if no further results are available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customersId, devicesId` | Gets a device. |
| `list` | `SELECT` | `customersId` | Lists a customer's devices. |
| `applyConfiguration` | `EXEC` | `customersId` | Applies a Configuration to the device to register the device for zero-touch enrollment. After applying a configuration to a device, the device automatically provisions itself on first boot, or next factory reset. |
| `removeConfiguration` | `EXEC` | `customersId` | Removes a configuration from device. |
| `unclaim` | `EXEC` | `customersId` | Unclaims a device from a customer and removes it from zero-touch enrollment. After removing a device, a customer must contact their reseller to register the device into zero-touch enrollment again. |
