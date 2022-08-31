---
title: saved_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_searches
  - operational_insights
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved_searches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.saved_searches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `array` | The tags attached to the saved search. |
| `version` | `integer` | The version number of the query language. The current version is 2 and is the default. |
| `category` | `string` | The category of the saved search. This helps the user to find a saved search faster.  |
| `displayName` | `string` | Saved search display name. |
| `etag` | `string` | The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag |
| `functionAlias` | `string` | The function alias if query serves as a function. |
| `functionParameters` | `string` | The optional function parameters if query serves as a function. Value should be in the following format: 'param-name1:type1 = default_value1, param-name2:type2 = default_value2'. For more examples and proper syntax please refer to https://docs.microsoft.com/en-us/azure/kusto/query/functions/user-defined-functions. |
| `query` | `string` | The query expression for the saved search. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SavedSearches_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the saved searches for a given Log Analytics Workspace |
| `SavedSearches_CreateOrUpdate` | `INSERT` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Creates or updates a saved search for a given workspace. |
| `SavedSearches_Delete` | `DELETE` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Deletes the specified saved search in a given workspace. |
| `SavedSearches_Get` | `EXEC` | `resourceGroupName, savedSearchId, subscriptionId, workspaceName` | Gets the specified saved search for a given workspace. |
