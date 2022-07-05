---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
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
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.entity_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The unique identifier of the session entity type. Format: `projects//locations//agents//sessions//entityTypes/` or `projects//locations//agents//environments//sessions//entityTypes/`. If `Environment ID` is not specified, we assume default 'draft' environment. |
| `entityOverrideMode` | `string` | Required. Indicates whether the additional data should override or supplement the custom entity type definition. |
| `entities` | `array` | Required. The collection of entities to override or supplement the custom entity type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_entityTypes_get` | `SELECT` | `name` | Retrieves the specified entity type. |
| `projects_locations_agents_entityTypes_list` | `SELECT` | `parent` | Returns the list of all entity types in the specified agent. |
| `projects_locations_agents_environments_sessions_entityTypes_get` | `SELECT` | `name` | Retrieves the specified session entity type. |
| `projects_locations_agents_environments_sessions_entityTypes_list` | `SELECT` | `parent` | Returns the list of all session entity types in the specified session. |
| `projects_locations_agents_sessions_entityTypes_get` | `SELECT` | `name` | Retrieves the specified session entity type. |
| `projects_locations_agents_sessions_entityTypes_list` | `SELECT` | `parent` | Returns the list of all session entity types in the specified session. |
| `projects_locations_agents_entityTypes_create` | `INSERT` | `parent` | Creates an entity type in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_environments_sessions_entityTypes_create` | `INSERT` | `parent` | Creates a session entity type. |
| `projects_locations_agents_sessions_entityTypes_create` | `INSERT` | `parent` | Creates a session entity type. |
| `projects_locations_agents_entityTypes_delete` | `DELETE` | `name` | Deletes the specified entity type. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_environments_sessions_entityTypes_delete` | `DELETE` | `name` | Deletes the specified session entity type. |
| `projects_locations_agents_sessions_entityTypes_delete` | `DELETE` | `name` | Deletes the specified session entity type. |
| `projects_locations_agents_entityTypes_patch` | `EXEC` | `name` | Updates the specified entity type. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_environments_sessions_entityTypes_patch` | `EXEC` | `name` | Updates the specified session entity type. |
| `projects_locations_agents_sessions_entityTypes_patch` | `EXEC` | `name` | Updates the specified session entity type. |
