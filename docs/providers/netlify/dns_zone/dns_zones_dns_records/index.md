---
title: dns_zones_dns_records
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
<tr><td><b>Name</b></td><td><code>netlify.dns_zone.dns_zones_dns_records</code></td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones_dns_records</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` |  |
| `site_id` | `string` |  |
| `type` | `string` |  |
| `dns_zone_id` | `string` |  |
| `flag` | `integer` |  |
| `hostname` | `string` |  |
| `value` | `string` |  |
| `priority` | `integer` |  |
| `managed` | `boolean` |  |
| `tag` | `string` |  |
| `ttl` | `integer` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `getDnsRecords` | `zone_id` |  | SELECT |
| `getIndividualDnsRecord` | `dns_record_id, zone_id` |  | SELECT |
| `createDnsRecord` | `zone_id` |  | INSERT |
| `deleteDnsRecord` | `dns_record_id, zone_id` |  | DELETE |
