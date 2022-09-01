---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - data_migration
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
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_migration.projects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `targetPlatform` | `string` | Target platform of the project |
| `systemData` | `object` |  |
| `targetConnectionInfo` | `object` | Defines the connection properties of a server |
| `type` | `string` |  |
| `azureAuthenticationInfo` | `object` | Azure Active Directory Application |
| `databasesInfo` | `array` | List of DatabaseInfo |
| `location` | `string` |  |
| `provisioningState` | `string` | The project's provisioning state |
| `sourceConnectionInfo` | `object` | Defines the connection properties of a server |
| `sourcePlatform` | `string` | Source platform of the project |
| `creationTime` | `string` | UTC Date and time when project was created |
| `tags` | `object` |  |
| `etag` | `string` | HTTP strong entity tag value. This is ignored if submitted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Projects_List` | `SELECT` | `api-version, groupName, serviceName, subscriptionId` | The project resource is a nested resource representing a stored migration project. This method returns a list of projects owned by a service resource. |
| `Projects_CreateOrUpdate` | `INSERT` |  | The project resource is a nested resource representing a stored migration project. The PUT method creates a new project or updates an existing one. |
| `Projects_Delete` | `DELETE` |  | The project resource is a nested resource representing a stored migration project. The DELETE method deletes a project. |
| `Projects_Get` | `EXEC` |  | The project resource is a nested resource representing a stored migration project. The GET method retrieves information about a project. |
| `Projects_Update` | `EXEC` |  | The project resource is a nested resource representing a stored migration project. The PATCH method updates an existing project. |
