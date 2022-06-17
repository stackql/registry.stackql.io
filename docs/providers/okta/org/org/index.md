---
title: org
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
<tr><td><b>Name</b></td><td><code>org</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.org</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `_links` | `object` |
| `status` | `string` |
| `created` | `string` |
| `companyName` | `string` |
| `state` | `string` |
| `expiresAt` | `string` |
| `lastUpdated` | `string` |
| `subdomain` | `string` |
| `address2` | `string` |
| `postalCode` | `string` |
| `address1` | `string` |
| `supportPhoneNumber` | `string` |
| `city` | `string` |
| `phoneNumber` | `string` |
| `country` | `string` |
| `website` | `string` |
| `endUserSupportHelpURL` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` |  | Get settings of your organization. |
| `partialUpdate` | `EXEC` |  | Partial update settings of your organization. |
| `update` | `EXEC` |  | Update settings of your organization. |
