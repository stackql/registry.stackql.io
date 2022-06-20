---
title: jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquery.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The resource type of the response. |
| `nextPageToken` | `string` | A token to request the next page of results. |
| `etag` | `string` | A hash of this page of results. |
| `jobs` | `array` | List of jobs that were requested. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobId, projectId` | Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role. |
| `list` | `SELECT` | `projectId` | Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property. |
| `insert` | `INSERT` | `projectId, data__configuration` | Starts a new asynchronous job. Requires the Can View project role. |
| `delete` | `DELETE` | `jobsId, projectsId` | Requests the deletion of the metadata of a job. This call returns when the job's metadata is deleted. |
| `cancel` | `EXEC` | `jobId, projectId` | Requests that a job be cancelled. This call will return immediately, and the client will need to poll for the job status to see if the cancel completed successfully. Cancelled jobs may still incur costs. |
| `getQueryResults` | `EXEC` | `jobId, projectId` | Retrieves the results of a query job. |
| `query` | `EXEC` | `projectId, data__query` | Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout. |
