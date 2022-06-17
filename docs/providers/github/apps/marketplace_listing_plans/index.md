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
<tr><td><b>Name</b></td><td><code>github.apps.marketplace_listing_plans</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listing_plans</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `price_model` | `string` |  |
| `state` | `string` |  |
| `has_free_trial` | `boolean` |  |
| `url` | `string` |  |
| `bullets` | `array` |  |
| `unit_name` | `string` |  |
| `yearly_price_in_cents` | `integer` |  |
| `number` | `integer` |  |
| `accounts_url` | `string` |  |
| `monthly_price_in_cents` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_plans` | `` | Lists all plans that are part of your GitHub Marketplace listing.<br /><br />GitHub Apps must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. OAuth Apps must use [basic authentication](https://docs.github.com/rest/overview/other-authentication-methods#basic-authentication) with their client ID and client secret to access this endpoint. | SELECT |
