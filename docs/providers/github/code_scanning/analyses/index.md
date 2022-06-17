---
title: analyses
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
  
    
See also:   
[[` SHOW `]](/docs/language-spec/show) [[` DESCRIBE `]](/docs/language-spec/describe)  
* * * 
## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyses</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.code_scanning.analyses</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` | Unique identifier for this analysis. |
| `ref` | `string` | The full Git reference, formatted as `refs/heads/&#x7B;branch name&#x7D;`,<br />`refs/pull/&#x7B;number&#x7D;/merge`, or `refs/pull/&#x7B;number&#x7D;/head`. |
| `analysis_key` | `string` | Identifies the configuration under which the analysis was executed. For example, in GitHub Actions this includes the workflow filename and job name. |
| `url` | `string` | The REST API URL of the analysis resource. |
| `tool` | `object` |  |
| `category` | `string` | Identifies the configuration under which the analysis was executed. Used to distinguish between multiple analyses for the same tool and commit, but performed on different languages or different parts of the code. |
| `environment` | `string` | Identifies the variable values associated with the environment in which this analysis was performed. |
| `results_count` | `integer` | The total number of results in the analysis. |
| `warning` | `string` | Warning generated when processing the analysis |
| `sarif_id` | `string` | An identifier for the upload. |
| `commit_sha` | `string` | The SHA of the commit to which the analysis you are uploading relates. |
| `created_at` | `string` | The time that the analysis was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`. |
| `rules_count` | `integer` | The total number of rules used in the analysis. |
| `deletable` | `boolean` |  |
| `error` | `string` |  |
## Methods
