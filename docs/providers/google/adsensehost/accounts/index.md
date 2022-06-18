---
title: accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adsensehost.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Unique identifier of this account. |
| `name` | `string` | Name of this account. |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#account. |
| `status` | `string` | Approval status of this account. One of: PENDING, APPROVED, DISABLED. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `accountId` | Get information about the selected associated AdSense account. |
| `list` | `SELECT` | `filterAdClientId` | List hosted accounts associated with this AdSense account by ad client id. |
