---
title: results
hide_title: false
hide_table_of_contents: false
keywords:
  - results
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
<tr><td><b>Name</b></td><td><code>results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.results</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name for the test case result. Format: `projects//locations//agents//testCases/ /results/`. |
| `environment` | `string` | Environment where the test was run. If not set, it indicates the draft environment. |
| `testResult` | `string` | Whether the test case passed in the agent environment. |
| `testTime` | `string` | The time that the test was run. |
| `conversationTurns` | `array` | The conversation turns uttered during the test case replay in chronological order. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_testCases_results_get` | `SELECT` | `name` | Gets a test case result. |
| `projects_locations_agents_testCases_results_list` | `SELECT` | `parent` | Fetches a list of results for a given test case. |