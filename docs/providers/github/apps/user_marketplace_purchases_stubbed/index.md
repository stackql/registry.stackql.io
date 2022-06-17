---
title: user_marketplace_purchases_stubbed
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
<tr><td><b>Name</b></td><td><code>github.apps.user_marketplace_purchases_stubbed</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.user_marketplace_purchases_stubbed</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `free_trial_ends_on` | `string` |  |
| `next_billing_date` | `string` |  |
| `on_free_trial` | `boolean` |  |
| `plan` | `object` | Marketplace Listing Plan |
| `unit_count` | `integer` |  |
| `updated_at` | `string` |  |
| `account` | `object` |  |
| `billing_cycle` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_subscriptions_for_authenticated_user_stubbed` | `` | Lists the active subscriptions for the authenticated user. You must use a [user-to-server OAuth access token](https://docs.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint. . OAuth Apps must authenticate using an [OAuth token](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/). | SELECT |
