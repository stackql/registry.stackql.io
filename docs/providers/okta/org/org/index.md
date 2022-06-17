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
<tr><td><b>Name</b></td><td><code>okta.org.org</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.org.org</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `website` | `string` |  |
| `country` | `string` |  |
| `created` | `string` |  |
| `expiresAt` | `string` |  |
| `city` | `string` |  |
| `postalCode` | `string` |  |
| `state` | `string` |  |
| `status` | `string` |  |
| `lastUpdated` | `string` |  |
| `supportPhoneNumber` | `string` |  |
| `address1` | `string` |  |
| `phoneNumber` | `string` |  |
| `_links` | `object` |  |
| `companyName` | `string` |  |
| `endUserSupportHelpURL` | `string` |  |
| `address2` | `string` |  |
| `subdomain` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `` | Get settings of your organization. | SELECT |
| `partialUpdate` | `` | Partial update settings of your organization. | EXEC |
| `update` | `` | Update settings of your organization. | EXEC |
