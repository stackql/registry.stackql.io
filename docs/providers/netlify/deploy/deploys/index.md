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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `error_message` | `string` |
| `function_schedules` | `array` |
| `context` | `string` |
| `build_id` | `string` |
| `deploy_url` | `string` |
| `site_id` | `string` |
| `updated_at` | `string` |
| `state` | `string` |
| `framework` | `string` |
| `branch` | `string` |
| `draft` | `boolean` |
| `locked` | `boolean` |
| `url` | `string` |
| `admin_url` | `string` |
| `published_at` | `string` |
| `skipped` | `boolean` |
| `review_id` | `number` |
| `user_id` | `string` |
| `site_capabilities` | `object` |
| `review_url` | `string` |
| `commit_url` | `string` |
| `deploy_ssl_url` | `string` |
| `title` | `string` |
| `created_at` | `string` |
| `required` | `array` |
| `required_functions` | `array` |
| `ssl_url` | `string` |
| `screenshot_url` | `string` |
| `commit_ref` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getDeploy` | `SELECT` | `deploy_id` |
