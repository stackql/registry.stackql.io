---
title: user
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
<tr><td><b>Name</b></td><td><code>netlify.user.user</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.user.user</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `uid` | `string` |  |
| `site_count` | `integer` |  |
| `email` | `string` |  |
| `last_login` | `string` |  |
| `affiliate_id` | `string` |  |
| `onboarding_progress` | `object` |  |
| `avatar_url` | `string` |  |
| `login_providers` | `array` |  |
| `full_name` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getCurrentUser` | `` |  | SELECT |
