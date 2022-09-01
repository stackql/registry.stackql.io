---
title: workbooks
hide_title: false
hide_table_of_contents: false
keywords:
  - workbooks
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
<tr><td><b>Name</b></td><td><code>workbooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.workbooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `description` | `string` | The description of the workbook. |
| `serializedData` | `string` | Configuration of this particular workbook. Configuration data is a string containing valid JSON |
| `revision` | `string` | The unique revision id for this workbook definition |
| `userId` | `string` | Unique user id of the specific user that owns this workbook. |
| `displayName` | `string` | The user-defined name (display name) of the workbook. |
| `category` | `string` | Workbook category, as defined by the user at creation time. |
| `timeModified` | `string` | Date and time in UTC of the last modification that was made to this workbook definition. |
| `version` | `string` | Workbook schema version format, like 'Notebook/1.0', which should match the workbook in serializedData |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `etag` | `string` | Resource etag |
| `sourceId` | `string` | ResourceId for a source resource. |
| `kind` | `string` | The kind of workbook. Only valid value is shared. |
| `identity` | `object` | Identity used for BYOS |
| `storageUri` | `string` | The resourceId to the storage account when bring your own storage is used |
| `tags` | `array` | Being deprecated, please use the other tags field |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Workbooks_ListByResourceGroup` | `SELECT` | `category, resourceGroupName, subscriptionId` | Get all Workbooks defined within a specified resource group and category. |
| `Workbooks_ListBySubscription` | `SELECT` | `category, subscriptionId` | Get all Workbooks defined within a specified subscription and category. |
| `Workbooks_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a new workbook. |
| `Workbooks_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a workbook. |
| `Workbooks_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get a single workbook by its resourceName. |
| `Workbooks_RevisionGet` | `EXEC` | `resourceGroupName, resourceName, revisionId, subscriptionId` | Get a single workbook revision defined by its revisionId. |
| `Workbooks_RevisionsList` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get the revisions for the workbook defined by its resourceName. |
| `Workbooks_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a workbook that has already been added. |
