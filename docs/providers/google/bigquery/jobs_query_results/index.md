---
title: jobs_query_results
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_query_results
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
<tr><td><b>Name</b></td><td><code>jobs_query_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.jobs_query_results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A hash of this response. |
| `jobReference` | `object` |  |
| `cacheHit` | `boolean` | Whether the query result was fetched from the query cache. |
| `pageToken` | `string` | A token used for paging results. |
| `totalRows` | `string` | The total number of rows in the complete query result set, which can be more than the number of rows in this single page of results. Present only when the query completes successfully. |
| `rows` | `array` | An object with as many results as can be contained within the maximum permitted reply size. To get any additional rows, you can call GetQueryResults and specify the jobReference returned above. Present only when the query completes successfully. |
| `schema` | `object` |  |
| `errors` | `array` | [Output-only] The first errors or warnings encountered during the running of the job. The final message includes the number of errors that caused the process to stop. Errors here do not necessarily mean that the job has completed or was unsuccessful. |
| `jobComplete` | `boolean` | Whether the query has completed or not. If rows or totalRows are present, this will always be true. If this is false, totalRows will not be available. |
| `totalBytesProcessed` | `string` | The total number of bytes processed for this query. |
| `kind` | `string` | The resource type of the response. |
| `numDmlAffectedRows` | `string` | [Output-only] The number of rows affected by a DML statement. Present only for DML statements INSERT, UPDATE or DELETE. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `jobs_getQueryResults` | `SELECT` | `jobId, projectId` |