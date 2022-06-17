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
<tr><td><b>Name</b></td><td><code>netlify.account_membership.accounts</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.account_membership.accounts</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `type_name` | `string` |  |
| `roles_allowed` | `array` |  |
| `owner_ids` | `array` |  |
| `slug` | `string` |  |
| `billing_email` | `string` |  |
| `type` | `string` |  |
| `payment_method_id` | `string` |  |
| `created_at` | `string` |  |
| `billing_name` | `string` |  |
| `type_id` | `string` |  |
| `updated_at` | `string` |  |
| `billing_details` | `string` |  |
| `capabilities` | `object` |  |
| `billing_period` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getAccount` | `account_id` |  | SELECT |
| `listAccountsForUser` | `` |  | SELECT |
| `createAccount` | `data__name, data__type_id` |  | INSERT |
| `cancelAccount` | `account_id` |  | EXEC |
| `updateAccount` | `account_id` |  | EXEC |
