---
title: my_workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - my_workbooks
  - application_insights
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
<tr><td><b>Name</b></td><td><code>my_workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.my_workbooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `type` | `string` | Azure resource type |
| `kind` | `string` | The kind of workbook. Choices are user and shared. |
| `serializedData` | `string` | Configuration of this particular private workbook. Configuration data is a string containing valid JSON |
| `storageUri` | `string` | BYOS Storage Account URI |
| `location` | `string` | Resource location |
| `displayName` | `string` | The user-defined name of the private workbook. |
| `timeModified` | `string` | Date and time in UTC of the last modification that was made to this private workbook definition. |
| `userId` | `string` | Unique user id of the specific user that owns this private workbook. |
| `identity` | `object` | Customer Managed Identity |
| `tags` | `array` | A list of 0 or more tags that are associated with this private workbook definition |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `category` | `string` | Workbook category, as defined by the user at creation time. |
| `etag` | `` | Resource etag |
| `version` | `string` | This instance's version of the data model. This can change as new features are added that can be marked private workbook. |
| `sourceId` | `string` | Optional resourceId for a source resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `MyWorkbooks_ListByResourceGroup` | `SELECT` | `category, resourceGroupName, subscriptionId` | Get all private workbooks defined within a specified resource group and category. |
| `MyWorkbooks_ListBySubscription` | `SELECT` | `category, subscriptionId` | Get all private workbooks defined within a specified subscription and category. |
| `MyWorkbooks_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a new private workbook. |
| `MyWorkbooks_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a private workbook. |
| `MyWorkbooks_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get a single private workbook by its resourceName. |
| `MyWorkbooks_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a private workbook that has already been added. |
