---
title: projects.locations.workflowTemplates
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
<tr><td><b>Name</b></td><td><code>projects.locations.workflowTemplates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.projects.locations.workflowTemplates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `nextPageToken` | `string` | Output only. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListWorkflowTemplatesRequest. |
| `templates` | `array` | Output only. WorkflowTemplates list. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `locationsId, projectsId, workflowTemplatesId` | Retrieves the latest workflow template.Can retrieve previously instantiated template by specifying optional version parameter. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists workflows that match the specified filter in the request. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates new workflow template. |
| `delete` | `DELETE` | `locationsId, projectsId, workflowTemplatesId` | Deletes a workflow template. It does not cancel in-progress workflows. |
| `getIamPolicy` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set. |
| `instantiate` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Instantiates a template and begins execution.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `instantiateInline` | `EXEC` | `locationsId, projectsId` | Instantiates a template and begins execution.This method is equivalent to executing the sequence CreateWorkflowTemplate, InstantiateWorkflowTemplate, DeleteWorkflowTemplate.The returned Operation can be used to track execution of workflow by polling operations.get. The Operation will complete when entire workflow is finished.The running workflow can be aborted via operations.cancel. This will cause any inflight jobs to be cancelled and workflow-owned clusters to be deleted.The Operation.metadata will be WorkflowMetadata (https://cloud.google.com/dataproc/docs/reference/rpc/google.cloud.dataproc.v1#workflowmetadata). Also see Using WorkflowMetadata (https://cloud.google.com/dataproc/docs/concepts/workflows/debugging#using_workflowmetadata).On successful completion, Operation.response will be Empty. |
| `setIamPolicy` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Sets the access control policy on the specified resource. Replaces any existing policy.Can return NOT_FOUND, INVALID_ARGUMENT, and PERMISSION_DENIED errors. |
| `testIamPermissions` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning. |
| `update` | `EXEC` | `locationsId, projectsId, workflowTemplatesId` | Updates (replaces) workflow template. The updated template must contain version that matches the current server version. |
