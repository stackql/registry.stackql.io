---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
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
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the issue. Format: projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue} |
| `createTime` | `string` | Output only. The time at which this issue was created. |
| `displayName` | `string` | The representative name for the issue. |
| `updateTime` | `string` | Output only. The most recent time that this issue was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_issueModels_issues_get` | `SELECT` | `name` | Gets an issue. |
| `projects_locations_issueModels_issues_list` | `SELECT` | `parent` | Lists issues. |
| `projects_locations_issueModels_issues_patch` | `EXEC` | `name` | Updates an issue. |
