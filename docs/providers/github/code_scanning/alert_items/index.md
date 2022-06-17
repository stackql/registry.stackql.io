---
title: alert_items
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
<tr><td><b>Name</b></td><td><code>github.code_scanning.alert_items</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.alert_items</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `dismissed_at` | `string` | The time that the alert was dismissed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `dismissed_reason` | `string` | **Required when the state is dismissed.** The reason for dismissing or closing the alert. Can be one of: `false positive`, `won't fix`, and `used in tests`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `url` | `string` | The REST API URL of the alert resource. |
| `most_recent_instance` | `object` |  |
| `instances_url` | `string` | The REST API URL for fetching the list of instances for an alert. |
| `tool` | `object` |  |
| `fixed_at` | `string` | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `rule` | `object` |  |
| `updated_at` | `string` | The time that the alert was last updated in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `number` | `integer` | The security alert number. |
| `state` | `string` | State of a code scanning alert. |
| `dismissed_by` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `list_alerts_for_repo` | `owner, repo` | Lists all open code scanning alerts for the default branch (usually `main`<br />or `master`). You must use an access token with the `security_events` scope to use<br />this endpoint with private repos, the `public_repo` scope also grants permission to read<br />security events on public repos only. GitHub Apps must have the `security_events` read<br />permission to use this endpoint.<br /><br />The response includes a `most_recent_instance` object.<br />This provides details of the most recent instance of this alert<br />for the default branch or for the specified Git reference<br />(if you used `ref` in the request). | SELECT |
