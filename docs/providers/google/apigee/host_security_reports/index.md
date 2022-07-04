---
title: host_security_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - host_security_reports
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
<tr><td><b>Name</b></td><td><code>host_security_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.host_security_reports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `updated` | `string` | Output only. Last updated timestamp for the query. |
| `queryParams` | `object` | Metadata for the security report. |
| `executionTime` | `string` | ExecutionTime is available only after the query is completed. |
| `error` | `string` | Error is set when query fails. |
| `resultFileSize` | `string` | ResultFileSize is available only after the query is completed. |
| `result` | `object` | Contains informations about the security report results. |
| `self` | `string` | Self link of the query. Example: `/organizations/myorg/environments/myenv/securityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostSecurityReports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
| `created` | `string` | Creation time of the query. |
| `reportDefinitionId` | `string` | Report Definition ID. |
| `envgroupHostname` | `string` | Hostname is available only when query is executed at host level. |
| `displayName` | `string` | Display Name specified by the user. |
| `resultRows` | `string` | ResultRows is available only after the query is completed. |
| `state` | `string` | Query state could be "enqueued", "running", "completed", "failed". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_hostSecurityReports_get` | `SELECT` | `name` | Get status of a query submitted at host level. If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed" |
| `organizations_hostSecurityReports_list` | `SELECT` | `parent` | Return a list of Security Reports at host level. |
| `organizations_hostSecurityReports_create` | `INSERT` | `parent` | Submit a query at host level to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the `state` of "enqueued" means that the request succeeded. |