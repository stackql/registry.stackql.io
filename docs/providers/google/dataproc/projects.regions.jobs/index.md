---
title: projects.regions.jobs
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
<tr><td><b>Name</b></td><td><code>projects.regions.jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.projects.regions.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Optional. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListJobsRequest. |
| `jobs` | `array` | Output only. Jobs list. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobId, projectId, region` | Gets the resource representation for a job in a project. |
| `list` | `SELECT` | `projectId, region` | Lists regions/{region}/jobs in a project. |
| `delete` | `DELETE` | `jobId, projectId, region` | Deletes the job from the project. If the job is active, the delete fails, and the response returns FAILED_PRECONDITION. |
| `cancel` | `EXEC` | `jobId, projectId, region` | Starts a job cancellation request. To access the job resource after cancellation, call regions/{region}/jobs.list (https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/list) or regions/{region}/jobs.get (https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/get). |
| `getIamPolicy` | `EXEC` | `jobsId, projectsId, regionsId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `patch` | `EXEC` | `jobId, projectId, region` | Updates a job in a project. |
| `setIamPolicy` | `EXEC` | `jobsId, projectsId, regionsId` | Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors. |
| `submit` | `EXEC` | `projectId, region` | Submits a job to a cluster. |
| `submitAsOperation` | `EXEC` | `projectId, region` | Submits job to a cluster. |
| `testIamPermissions` | `EXEC` | `jobsId, projectsId, regionsId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
