---
title: org_alert_items
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
<tr><td><b>Name</b></td><td><code>org_alert_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.org_alert_items</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `instances_url` | `string` | The REST API URL for fetching the list of instances for an alert. |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `tool` | `object` |  |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `dismissed_by` | `object` | Simple User |
| `dismissed_reason` | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`. |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `state` | `string` | State of a code scanning alert. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `most_recent_instance` | `object` |  |
| `repository` | `object` | Minimal Repository |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `url` | `string` | The REST API URL of the alert resource. |
| `rule` | `object` |  |
| `number` | `integer` | The security alert number. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `list_alerts_for_org` | `SELECT` | `org` |
