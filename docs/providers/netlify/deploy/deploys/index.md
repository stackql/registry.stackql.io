---
title: deploys
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
<tr><td><b>Name</b></td><td><code>deploys</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `context` | `string` |
| `screenshot_url` | `string` |
| `required` | `array` |
| `error_message` | `string` |
| `function_schedules` | `array` |
| `published_at` | `string` |
| `user_id` | `string` |
| `framework` | `string` |
| `locked` | `boolean` |
| `skipped` | `boolean` |
| `updated_at` | `string` |
| `build_id` | `string` |
| `commit_ref` | `string` |
| `title` | `string` |
| `required_functions` | `array` |
| `admin_url` | `string` |
| `commit_url` | `string` |
| `site_id` | `string` |
| `created_at` | `string` |
| `url` | `string` |
| `review_id` | `number` |
| `review_url` | `string` |
| `deploy_url` | `string` |
| `deploy_ssl_url` | `string` |
| `site_capabilities` | `object` |
| `draft` | `boolean` |
| `state` | `string` |
| `ssl_url` | `string` |
| `branch` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDeploy` | `SELECT` | `deploy_id` |
