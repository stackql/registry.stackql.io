---
title: schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas
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
<tr><td><b>Name</b></td><td><code>schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsub.schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. Name of the schema. Format is `projects/{project}/schemas/{schema}`. |
| `revisionCreateTime` | `string` | Output only. The timestamp that the revision was created. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the schema. |
| `type` | `string` | The type of the schema definition. |
| `definition` | `string` | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_schemas_get` | `SELECT` | `name` | Gets a schema. |
| `projects_schemas_list` | `SELECT` | `parent` | Lists schemas in a project. |
| `projects_schemas_create` | `INSERT` | `parent` | Creates a schema. |
| `projects_schemas_delete` | `DELETE` | `name` | Deletes a schema. |
| `projects_schemas_validate` | `EXEC` | `parent` | Validates a schema. |
| `projects_schemas_validateMessage` | `EXEC` | `parent` | Validates a message against a schema. |
