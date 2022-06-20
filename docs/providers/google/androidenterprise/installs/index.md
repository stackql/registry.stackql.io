---
title: installs
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
<tr><td><b>Name</b></td><td><code>installs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.installs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceId, enterpriseId, installId, userId` | Retrieves details of an installation of an app on a device. |
| `list` | `SELECT` | `deviceId, enterpriseId, userId` | Retrieves the details of all apps installed on the specified device. |
| `delete` | `DELETE` | `deviceId, enterpriseId, installId, userId` | Requests to remove an app from a device. A call to get or list will still show the app as installed on the device until it is actually removed. |
| `update` | `EXEC` | `deviceId, enterpriseId, installId, userId` | Requests to install the latest version of an app to a device. If the app is already installed, then it is updated to the latest version if necessary. |
