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
<tr><td><b>Name</b></td><td><code>netlify.deploy.sites_deploys</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.deploy.sites_deploys</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `ssl_url` | `string` |  |
| `error_message` | `string` |  |
| `site_id` | `string` |  |
| `screenshot_url` | `string` |  |
| `user_id` | `string` |  |
| `commit_ref` | `string` |  |
| `title` | `string` |  |
| `branch` | `string` |  |
| `deploy_url` | `string` |  |
| `framework` | `string` |  |
| `created_at` | `string` |  |
| `required` | `array` |  |
| `draft` | `boolean` |  |
| `skipped` | `boolean` |  |
| `published_at` | `string` |  |
| `updated_at` | `string` |  |
| `commit_url` | `string` |  |
| `url` | `string` |  |
| `review_id` | `number` |  |
| `site_capabilities` | `object` |  |
| `function_schedules` | `array` |  |
| `state` | `string` |  |
| `locked` | `boolean` |  |
| `required_functions` | `array` |  |
| `admin_url` | `string` |  |
| `review_url` | `string` |  |
| `deploy_ssl_url` | `string` |  |
| `build_id` | `string` |  |
| `context` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getSiteDeploy` | `deploy_id, site_id` |  | SELECT |
| `listSiteDeploys` | `site_id` |  | SELECT |
| `createSiteDeploy` | `site_id` |  | INSERT |
| `updateSiteDeploy` | `deploy_id, site_id` |  | EXEC |
