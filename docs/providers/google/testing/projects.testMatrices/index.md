---
title: projects.testMatrices
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
<tr><td><b>Name</b></td><td><code>projects.testMatrices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.testing.projects.testMatrices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `state` | `string` | Output only. Indicates the current progress of the test matrix. |
| `timestamp` | `string` | Output only. The time this test matrix was initially created. |
| `testExecutions` | `array` | Output only. The list of test executions that the service creates for this matrix. |
| `environmentMatrix` | `object` | The matrix of environments in which the test is to be executed. |
| `resultStorage` | `object` | Locations where the results of running the test are stored. |
| `testSpecification` | `object` | A description of how to run the test. |
| `invalidMatrixDetails` | `string` | Output only. Describes why the matrix is considered invalid. Only useful for matrices in the INVALID state. |
| `failFast` | `boolean` | If true, only a single attempt at most will be made to run each execution/shard in the matrix. Flaky test attempts are not affected. Normally, 2 or more attempts are made if a potential infrastructure issue is detected. This feature is for latency sensitive workloads. The incidence of execution failures may be significantly greater for fail-fast matrices and support is more limited because of that expectation. |
| `outcomeSummary` | `string` | Output Only. The overall outcome of the test. Only set when the test matrix state is FINISHED. |
| `projectId` | `string` | The cloud project that owns the test matrix. |
| `testMatrixId` | `string` | Output only. Unique id set by the service. |
| `clientInfo` | `object` | Information about the client which invoked the test. |
| `flakyTestAttempts` | `integer` | The number of times a TestExecution should be re-attempted if one or more of its test cases fail for any reason. The maximum number of reruns allowed is 10. Default is 0, which implies no reruns. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `projectId, testMatrixId` | Checks the status of a test matrix. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist |
| `create` | `INSERT` | `projectId` | Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices. |
| `cancel` | `EXEC` | `projectId, testMatrixId` | Cancels unfinished test executions in a test matrix. This call returns immediately and cancellation proceeds asynchronously. If the matrix is already final, this operation will have no effect. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist |
