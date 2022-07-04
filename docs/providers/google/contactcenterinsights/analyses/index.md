---
title: analyses
hide_title: false
hide_table_of_contents: false
keywords:
  - analyses
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
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.analyses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the analysis. Format: projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis} |
| `createTime` | `string` | Output only. The time at which the analysis was created, which occurs when the long-running operation completes. |
| `requestTime` | `string` | Output only. The time at which the analysis was requested. |
| `analysisResult` | `object` | The result of an analysis. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_conversations_analyses_get` | `SELECT` | `name` | Gets an analysis. |
| `projects_locations_conversations_analyses_list` | `SELECT` | `parent` | Lists analyses. |
| `projects_locations_conversations_analyses_create` | `INSERT` | `parent` | Creates an analysis. The long running operation is done when the analysis has completed. |
| `projects_locations_conversations_analyses_delete` | `DELETE` | `name` | Deletes an analysis. |