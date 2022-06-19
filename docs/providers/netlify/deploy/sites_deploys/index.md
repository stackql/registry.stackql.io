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
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.sites_deploys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `review_id` | `number` |
| `locked` | `boolean` |
| `user_id` | `string` |
| `commit_ref` | `string` |
| `commit_url` | `string` |
| `draft` | `boolean` |
| `url` | `string` |
| `site_capabilities` | `object` |
| `error_message` | `string` |
| `context` | `string` |
| `published_at` | `string` |
| `function_schedules` | `array` |
| `required_functions` | `array` |
| `framework` | `string` |
| `state` | `string` |
| `created_at` | `string` |
| `build_id` | `string` |
| `ssl_url` | `string` |
| `title` | `string` |
| `deploy_url` | `string` |
| `site_id` | `string` |
| `skipped` | `boolean` |
| `deploy_ssl_url` | `string` |
| `branch` | `string` |
| `review_url` | `string` |
| `screenshot_url` | `string` |
| `updated_at` | `string` |
| `admin_url` | `string` |
| `required` | `array` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
