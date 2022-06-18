---
title: accounts.returncarrier
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
<tr><td><b>Name</b></td><td><code>accounts.returncarrier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.accounts.returncarrier</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `list` | `SELECT` | `accountId` | Lists available return carriers in the merchant account. |
| `create` | `INSERT` | `accountId` | Links return carrier to a merchant account. |
| `delete` | `DELETE` | `accountId, carrierAccountId` | Delete a return carrier in the merchant account. |
| `patch` | `EXEC` | `accountId, carrierAccountId` | Updates a return carrier in the merchant account. |
