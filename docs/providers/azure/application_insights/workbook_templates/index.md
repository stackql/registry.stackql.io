---
title: workbook_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - workbook_templates
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
<tr><td><b>Name</b></td><td><code>workbook_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.workbook_templates</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name. |
| `priority` | `integer` | Priority of the template. Determines which template to open when a workbook gallery is opened in viewer mode. |
| `location` | `string` | Resource location |
| `templateData` | `object` | Valid JSON object containing workbook template payload. |
| `author` | `string` | Information about the author of the workbook template. |
| `localized` | `object` | Key value pair of localized gallery. Each key is the locale code of languages supported by the Azure portal. |
| `type` | `string` | Azure resource type |
| `tags` | `object` | Resource tags |
| `galleries` | `array` | Workbook galleries supported by the template. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkbookTemplates_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all Workbook templates defined within a specified resource group. |
| `WorkbookTemplates_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create a new workbook template. |
| `WorkbookTemplates_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a workbook template. |
| `WorkbookTemplates_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Get a single workbook template by its resourceName. |
| `WorkbookTemplates_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a workbook template that has already been added. |
