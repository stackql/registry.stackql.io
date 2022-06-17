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
<tr><td><b>Name</b></td><td><code>netlify.deploy.deploys</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.deploys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `admin_url` | `string` |  |
| `site_id` | `string` |  |
| `url` | `string` |  |
| `build_id` | `string` |  |
| `user_id` | `string` |  |
| `context` | `string` |  |
| `published_at` | `string` |  |
| `deploy_url` | `string` |  |
| `created_at` | `string` |  |
| `review_id` | `number` |  |
| `updated_at` | `string` |  |
| `commit_ref` | `string` |  |
| `screenshot_url` | `string` |  |
| `required` | `array` |  |
| `framework` | `string` |  |
| `state` | `string` |  |
| `error_message` | `string` |  |
| `function_schedules` | `array` |  |
| `skipped` | `boolean` |  |
| `required_functions` | `array` |  |
| `commit_url` | `string` |  |
| `site_capabilities` | `object` |  |
| `review_url` | `string` |  |
| `draft` | `boolean` |  |
| `deploy_ssl_url` | `string` |  |
| `title` | `string` |  |
| `ssl_url` | `string` |  |
| `branch` | `string` |  |
| `locked` | `boolean` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getDeploy` | `deploy_id` |  | SELECT |
