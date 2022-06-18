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
| `updated_at` | `string` |
| `context` | `string` |
| `function_schedules` | `array` |
| `site_id` | `string` |
| `screenshot_url` | `string` |
| `draft` | `boolean` |
| `error_message` | `string` |
| `deploy_url` | `string` |
| `framework` | `string` |
| `deploy_ssl_url` | `string` |
| `ssl_url` | `string` |
| `admin_url` | `string` |
| `title` | `string` |
| `state` | `string` |
| `url` | `string` |
| `branch` | `string` |
| `required` | `array` |
| `commit_ref` | `string` |
| `commit_url` | `string` |
| `user_id` | `string` |
| `skipped` | `boolean` |
| `build_id` | `string` |
| `review_id` | `number` |
| `review_url` | `string` |
| `site_capabilities` | `object` |
| `required_functions` | `array` |
| `created_at` | `string` |
| `locked` | `boolean` |
| `published_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDeploy` | `SELECT` | `deploy_id` |
