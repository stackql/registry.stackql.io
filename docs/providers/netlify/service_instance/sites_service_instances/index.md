---
title: sites_service_instances
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
<tr><td><b>Name</b></td><td><code>sites_service_instances</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.service_instance.sites_service_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `service_path` | `string` |
| `snippets` | `array` |
| `service_name` | `string` |
| `url` | `string` |
| `env` | `object` |
| `service_slug` | `string` |
| `external_attributes` | `object` |
| `created_at` | `string` |
| `auth_url` | `string` |
| `updated_at` | `string` |
| `config` | `object` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `listServiceInstancesForSite` | `SELECT` | `site_id` |
