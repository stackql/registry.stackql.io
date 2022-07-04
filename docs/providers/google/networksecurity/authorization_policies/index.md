---
title: authorization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policies
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
<tr><td><b>Name</b></td><td><code>authorization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.networksecurity.authorization_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the AuthorizationPolicy resource. It matches pattern `projects/{project}/locations/{location}/authorizationPolicies/`. |
| `description` | `string` | Optional. Free-text description of the resource. |
| `rules` | `array` | Optional. List of rules to match. Note that at least one of the rules must match in order for the action specified in the 'action' field to be taken. A rule is a match if there is a matching source and destination. If left blank, the action specified in the `action` field will be applied on every request. |
| `updateTime` | `string` | Output only. The timestamp when the resource was updated. |
| `action` | `string` | Required. The action to take when a rule match is found. Possible values are "ALLOW" or "DENY". |
| `createTime` | `string` | Output only. The timestamp when the resource was created. |
| `labels` | `object` | Optional. Set of label tags associated with the AuthorizationPolicy resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_authorizationPolicies_get` | `SELECT` | `name` | Gets details of a single AuthorizationPolicy. |
| `projects_locations_authorizationPolicies_list` | `SELECT` | `parent` | Lists AuthorizationPolicies in a given project and location. |
| `projects_locations_authorizationPolicies_create` | `INSERT` | `parent` | Creates a new AuthorizationPolicy in a given project and location. |
| `projects_locations_authorizationPolicies_delete` | `DELETE` | `name` | Deletes a single AuthorizationPolicy. |
| `projects_locations_authorizationPolicies_patch` | `EXEC` | `name` | Updates the parameters of a single AuthorizationPolicy. |
