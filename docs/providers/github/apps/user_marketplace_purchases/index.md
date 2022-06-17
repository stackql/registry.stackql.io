---
title: user_marketplace_purchases
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
<tr><td><b>Name</b></td><td><code>user_marketplace_purchases</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.user_marketplace_purchases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `on_free_trial` | `boolean` |  |
| `plan` | `object` | Marketplace Listing Plan |
| `unit_count` | `integer` |  |
| `updated_at` | `string` |  |
| `account` | `object` |  |
| `billing_cycle` | `string` |  |
| `free_trial_ends_on` | `string` |  |
| `next_billing_date` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_subscriptions_for_authenticated_user` | `SELECT` |  |
