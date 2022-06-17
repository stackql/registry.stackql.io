---
title: sites_deploys
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
<tr><td><b>Name</b></td><td><code>sites_deploys</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.sites_deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `branch` | `string` |
| `framework` | `string` |
| `deploy_ssl_url` | `string` |
| `review_url` | `string` |
| `required_functions` | `array` |
| `commit_url` | `string` |
| `context` | `string` |
| `error_message` | `string` |
| `screenshot_url` | `string` |
| `draft` | `boolean` |
| `user_id` | `string` |
| `updated_at` | `string` |
| `title` | `string` |
| `review_id` | `number` |
| `state` | `string` |
| `site_id` | `string` |
| `skipped` | `boolean` |
| `function_schedules` | `array` |
| `admin_url` | `string` |
| `locked` | `boolean` |
| `deploy_url` | `string` |
| `commit_ref` | `string` |
| `build_id` | `string` |
| `created_at` | `string` |
| `site_capabilities` | `object` |
| `required` | `array` |
| `url` | `string` |
| `ssl_url` | `string` |
| `published_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
