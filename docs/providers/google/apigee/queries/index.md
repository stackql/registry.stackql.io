---
title: queries
hide_title: false
hide_table_of_contents: false
keywords:
  - queries
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
<tr><td><b>Name</b></td><td><code>queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.queries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Asynchronous Query Name. |
| `queryParams` | `object` |  |
| `result` | `object` |  |
| `self` | `string` | Self link of the query. Example: `/organizations/myorg/environments/myenv/queries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` or following format if query is running at host level: `/organizations/myorg/hostQueries/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
| `created` | `string` | Creation time of the query. |
| `reportDefinitionId` | `string` | Asynchronous Report ID. |
| `state` | `string` | Query state could be "enqueued", "running", "completed", "failed". |
| `resultRows` | `string` | ResultRows is available only after the query is completed. |
| `executionTime` | `string` | ExecutionTime is available only after the query is completed. |
| `updated` | `string` | Last updated timestamp for the query. |
| `envgroupHostname` | `string` | Hostname is available only when query is executed at host level. |
| `error` | `string` | Error is set when query fails. |
| `resultFileSize` | `string` | ResultFileSize is available only after the query is completed. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_queries_get` | `SELECT` | `name` | Get query status If the query is still in progress, the `state` is set to "running" After the query has completed successfully, `state` is set to "completed" |
| `organizations_environments_queries_list` | `SELECT` | `parent` | Return a list of Asynchronous Queries |
| `organizations_environments_queries_create` | `INSERT` | `parent` | Submit a query to be processed in the background. If the submission of the query succeeds, the API returns a 201 status and an ID that refer to the query. In addition to the HTTP status 201, the `state` of "enqueued" means that the request succeeded. |
