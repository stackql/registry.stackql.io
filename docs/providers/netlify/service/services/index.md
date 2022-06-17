---
title: services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.service.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
| ---- | -------- |
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `service_path` | `string` |
| `slug` | `string` |
| `events` | `array` |
| `icon` | `string` |
| `long_description` | `string` |
| `updated_at` | `string` |
| `environments` | `array` |
| `manifest_url` | `string` |
| `tags` | `array` |
| `created_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `getServices` | `SELECT` |  |
| `showService` | `EXEC` | `addonName` |
