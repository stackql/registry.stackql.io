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
| `title` | `string` |
| `commit_ref` | `string` |
| `site_id` | `string` |
| `locked` | `boolean` |
| `screenshot_url` | `string` |
| `required` | `array` |
| `published_at` | `string` |
| `ssl_url` | `string` |
| `skipped` | `boolean` |
| `deploy_url` | `string` |
| `review_id` | `number` |
| `function_schedules` | `array` |
| `build_id` | `string` |
| `site_capabilities` | `object` |
| `commit_url` | `string` |
| `admin_url` | `string` |
| `user_id` | `string` |
| `framework` | `string` |
| `branch` | `string` |
| `deploy_ssl_url` | `string` |
| `updated_at` | `string` |
| `draft` | `boolean` |
| `context` | `string` |
| `url` | `string` |
| `created_at` | `string` |
| `review_url` | `string` |
| `state` | `string` |
| `error_message` | `string` |
| `required_functions` | `array` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
