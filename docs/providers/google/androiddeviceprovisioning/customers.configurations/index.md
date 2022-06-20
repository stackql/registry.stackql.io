---
title: customers.configurations
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
<tr><td><b>Name</b></td><td><code>customers.configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androiddeviceprovisioning.customers.configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationsId, customersId` | Gets a device. |
| `list` | `SELECT` | `customersId` | Lists a customer's configurations. |
| `create` | `INSERT` | `customersId` | Creates a new configuration. Once created, a customer can apply the configuration to devices. |
| `delete` | `DELETE` | `configurationsId, customersId` | Deletes an unused configuration. The API call fails if the customer has devices with the configuration applied. |
| `patch` | `EXEC` | `configurationsId, customersId` | Updates a configuration's field values. |
