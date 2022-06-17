---
title: factors
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
<tr><td><b>Name</b></td><td><code>okta.userfactor.factors</code></td></tr>
<tr><td><b>Id</b></td><td><code>okta.userfactor.factors</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `provider` | `string` |  |
| `_links` | `object` |  |
| `verify` | `object` |  |
| `created` | `string` |  |
| `factorType` | `string` |  |
| `lastUpdated` | `string` |  |
| `status` | `string` |  |
| `_embedded` | `object` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get` | `factorId, userId` | Fetches a factor for the specified user | SELECT |
| `list` | `userId` | Enumerates all the enrolled factors for the specified user | SELECT |
| `insert` | `userId` | Enrolls a user with a supported factor. | INSERT |
| `delete` | `factorId, userId` | Unenrolls an existing factor for the specified user, allowing the user to enroll a new factor. | DELETE |
| `activate` | `factorId, userId` | The `sms` and `token:software:totp` factor types require activation to complete the enrollment process. | EXEC |
| `verify` | `factorId, userId` | Verifies an OTP for a `token` or `token:hardware` factor | EXEC |
