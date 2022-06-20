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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.user.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `last_login` | `string` |
| `uid` | `string` |
| `created_at` | `string` |
| `avatar_url` | `string` |
| `full_name` | `string` |
| `onboarding_progress` | `object` |
| `email` | `string` |
| `site_count` | `integer` |
| `affiliate_id` | `string` |
| `login_providers` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getCurrentUser` | `SELECT` |  |
