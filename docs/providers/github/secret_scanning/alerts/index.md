---
title: alerts
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
<tr><td><b>Name</b></td><td><code>github.secret_scanning.alerts</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.secret_scanning.alerts</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `secret` | `string` | The secret that was detected. |
| `locations_url` | `string` | The REST API URL of the code locations for this alert. |
| `resolved_at` | `string` | The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `resolution` | `string` | **Required when the `state` is `resolved`.** The reason for resolving the alert. Can be one of `false_positive`, `wont_fix`, `revoked`, or `used_in_tests`. |
| `secret_type` | `string` | The type of secret that secret scanning detected. |
| `number` | `integer` | The security alert number. |
| `url` | `string` | The REST API URL of the alert resource. |
| `state` | `string` | Sets the state of the secret scanning alert. Can be either `open` or `resolved`. You must provide `resolution` when you set the state to `resolved`. |
| `created_at` | `string` | The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `html_url` | `string` | The GitHub URL of the alert resource. |
| `resolved_by` | `object` | Simple User |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_alert` | `alert_number, owner, repo` | Gets a single secret scanning alert detected in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. | SELECT |
| `list_alerts_for_enterprise` | `enterprise` | Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest.<br />To use this endpoint, you must be a member of the enterprise, and you must use an access token with the `repo` scope or `security_events` scope. Alerts are only returned for organizations in the enterprise for which you are an organization owner or a [security manager](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization). | SELECT |
| `list_alerts_for_org` | `org` | Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.<br />To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. | SELECT |
| `list_alerts_for_repo` | `owner, repo` | Lists secret scanning alerts for a private repository, from newest to oldest. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` read permission to use this endpoint. | SELECT |
| `update_alert` | `alert_number, owner, repo, data__state` | Updates the status of a secret scanning alert in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the `repo` scope or `security_events` scope.<br /><br />GitHub Apps must have the `secret_scanning_alerts` write permission to use this endpoint. | EXEC |
