---
title: managedconfigurationsfordevice
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
<tr><td><b>Name</b></td><td><code>managedconfigurationsfordevice</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.managedconfigurationsfordevice</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceId, enterpriseId, managedConfigurationForDeviceId, userId` | Retrieves details of a per-device managed configuration. |
| `list` | `SELECT` | `deviceId, enterpriseId, userId` | Lists all the per-device managed configurations for the specified device. Only the ID is set. |
| `delete` | `DELETE` | `deviceId, enterpriseId, managedConfigurationForDeviceId, userId` | Removes a per-device managed configuration for an app for the specified device. |
| `update` | `EXEC` | `deviceId, enterpriseId, managedConfigurationForDeviceId, userId` | Adds or updates a per-device managed configuration for an app for the specified device. |
