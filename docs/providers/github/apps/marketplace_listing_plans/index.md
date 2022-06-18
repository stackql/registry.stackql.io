---
title: marketplace_listing_plans
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
<tr><td><b>Name</b></td><td><code>marketplace_listing_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listing_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `integer` |
| `name` | `string` |
| `description` | `string` |
| `monthly_price_in_cents` | `integer` |
| `bullets` | `array` |
| `price_model` | `string` |
| `unit_name` | `string` |
| `accounts_url` | `string` |
| `number` | `integer` |
| `url` | `string` |
| `yearly_price_in_cents` | `integer` |
| `has_free_trial` | `boolean` |
| `state` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_plans` | `SELECT` |  |
