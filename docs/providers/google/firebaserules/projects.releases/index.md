---
title: projects.releases
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
<tr><td><b>Name</b></td><td><code>projects.releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firebaserules.projects.releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | The pagination token to retrieve the next page of results. If the value is empty, no further results remain. |
| `releases` | `array` | List of `Release` instances. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `projectsId, releasesId` | Get a `Ruleset` by name including the full `Source` contents. |
| `list` | `SELECT` | `projectsId` | List the `Release` values for a project. This list may optionally be filtered by `Release` name, `Ruleset` name, `TestSuite` name, or any combination thereof. |
| `create` | `INSERT` | `projectsId` | Create a `Release`. Release names should reflect the developer's deployment practices. For example, the release name may include the environment name, application name, application version, or any other name meaningful to the developer. Once a `Release` refers to a `Ruleset`, the rules can be enforced by Firebase Rules-enabled services. More than one `Release` may be 'live' concurrently. Consider the following three `Release` names for `projects/foo` and the `Ruleset` to which they refer. Release Name -&#x7D; Ruleset Name * projects/foo/releases/prod -&#x7D; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/beta -&#x7D; projects/foo/rulesets/uuid123 * projects/foo/releases/prod/v23 -&#x7D; projects/foo/rulesets/uuid456 The relationships reflect a `Ruleset` rollout in progress. The `prod` and `prod/beta` releases refer to the same `Ruleset`. However, `prod/v23` refers to a new `Ruleset`. The `Ruleset` reference for a `Release` may be updated using the UpdateRelease method. |
| `delete` | `DELETE` | `projectsId, releasesId` | Delete a `Ruleset` by resource name. If the `Ruleset` is referenced by a `Release` the operation will fail. |
| `getExecutable` | `EXEC` | `projectsId, releasesId` | Get the `Release` executable to use when enforcing rules. |
| `patch` | `EXEC` | `projectsId, releasesId` | Update a `Release` via PATCH. Only updates to `ruleset_name` will be honored. `Release` rename is not supported. To create a `Release` use the CreateRelease method. |
