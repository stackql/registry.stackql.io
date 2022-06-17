---
title: dns_zones
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
<tr><td><b>Name</b></td><td><code>netlify.dns_zone.dns_zones</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `name` | `string` |  |
| `domain` | `string` |  |
| `user_id` | `string` |  |
| `account_slug` | `string` |  |
| `account_name` | `string` |  |
| `dns_servers` | `array` |  |
| `records` | `array` |  |
| `dedicated` | `boolean` |  |
| `updated_at` | `string` |  |
| `account_id` | `string` |  |
| `supported_record_types` | `array` |  |
| `site_id` | `string` |  |
| `created_at` | `string` |  |
| `ipv6_enabled` | `boolean` |  |
| `errors` | `array` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getDnsZone` | `zone_id` |  | SELECT |
| `getDnsZones` | `` |  | SELECT |
| `createDnsZone` | `` |  | INSERT |
| `deleteDnsZone` | `zone_id` |  | DELETE |
