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
| `commit_ref` | `string` |
| `build_id` | `string` |
| `state` | `string` |
| `skipped` | `boolean` |
| `required` | `array` |
| `commit_url` | `string` |
| `deploy_ssl_url` | `string` |
| `created_at` | `string` |
| `url` | `string` |
| `deploy_url` | `string` |
| `locked` | `boolean` |
| `title` | `string` |
| `draft` | `boolean` |
| `required_functions` | `array` |
| `site_capabilities` | `object` |
| `function_schedules` | `array` |
| `branch` | `string` |
| `admin_url` | `string` |
| `review_id` | `number` |
| `updated_at` | `string` |
| `site_id` | `string` |
| `published_at` | `string` |
| `framework` | `string` |
| `user_id` | `string` |
| `error_message` | `string` |
| `screenshot_url` | `string` |
| `ssl_url` | `string` |
| `context` | `string` |
| `review_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getSiteDeploy` | `SELECT` | `deploy_id, site_id` |
| `listSiteDeploys` | `SELECT` | `site_id` |
| `createSiteDeploy` | `INSERT` | `site_id` |
| `updateSiteDeploy` | `EXEC` | `deploy_id, site_id` |
