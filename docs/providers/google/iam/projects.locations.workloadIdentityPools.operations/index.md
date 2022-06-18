---
title: projects.locations.workloadIdentityPools.operations
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
<tr><td><b>Name</b></td><td><code>projects.locations.workloadIdentityPools.operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.iam.projects.locations.workloadIdentityPools.operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `name` | `string` | The name of the role. When Role is used in CreateRole, the role name must not be set. When Role is used in output and other input such as UpdateRole, the role name is the complete path, e.g., roles/logging.viewer for predefined roles and organizations/{ORGANIZATION_ID}/roles/logging.viewer for custom roles. |
| `description` | `string` | Optional. A human-readable description for the role. |
| `stage` | `string` | The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role. |
| `title` | `string` | Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes. |
| `deleted` | `boolean` | The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole. |
| `etag` | `string` | Used to perform a consistent read-modify-write. |
| `includedPermissions` | `array` | The names of the permissions this role grants when bound in an IAM policy. |
## Methods
| Name | Accessible by | Required Params |
| ---- | ------------- | --------------- |
| `get` | `SELECT` | `locationsId, operationsId, projectsId, workloadIdentityPoolsId` |
