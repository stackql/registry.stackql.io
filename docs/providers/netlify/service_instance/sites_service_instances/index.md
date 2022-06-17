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
<tr><td><b>Name</b></td><td><code>netlify.service_instance.sites_service_instances</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.service_instance.sites_service_instances</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `url` | `string` |  |
| `service_path` | `string` |  |
| `updated_at` | `string` |  |
| `snippets` | `array` |  |
| `service_name` | `string` |  |
| `auth_url` | `string` |  |
| `config` | `object` |  |
| `env` | `object` |  |
| `external_attributes` | `object` |  |
| `created_at` | `string` |  |
| `service_slug` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `listServiceInstancesForSite` | `site_id` |  | SELECT |
