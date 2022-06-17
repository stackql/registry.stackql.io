---
title: sites_dns
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
<tr><td><b>Name</b></td><td><code>netlify.dns_zone.sites_dns</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.sites_dns</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `ipv6_enabled` | `boolean` |  |
| `supported_record_types` | `array` |  |
| `dedicated` | `boolean` |  |
| `created_at` | `string` |  |
| `account_id` | `string` |  |
| `account_slug` | `string` |  |
| `user_id` | `string` |  |
| `records` | `array` |  |
| `site_id` | `string` |  |
| `updated_at` | `string` |  |
| `dns_servers` | `array` |  |
| `account_name` | `string` |  |
| `errors` | `array` |  |
| `domain` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getDNSForSite` | `site_id` |  | SELECT |
| `configureDNSForSite` | `site_id` |  | EXEC |
