---
title: projects.rulesets
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
<tr><td><b>Name</b></td><td><code>projects.rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firebaserules.projects.rulesets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The pagination token to retrieve the next page of results. If the value is empty, no further results remain. |
| `rulesets` | `array` | List of `Ruleset` instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, rulesetsId` | Get a `Ruleset` by name including the full `Source` contents. |
| `list` | `SELECT` | `projectsId` | List `Ruleset` metadata only and optionally filter the results by `Ruleset` name. The full `Source` contents of a `Ruleset` may be retrieved with GetRuleset. |
| `create` | `INSERT` | `projectsId` | Create a `Ruleset` from `Source`. The `Ruleset` is given a unique generated name which is returned to the caller. `Source` containing syntactic or semantics errors will result in an error response indicating the first error encountered. For a detailed view of `Source` issues, use TestRuleset. |
| `delete` | `DELETE` | `projectsId, rulesetsId` | Delete a `Ruleset` by resource name. If the `Ruleset` is referenced by a `Release` the operation will fail. |
