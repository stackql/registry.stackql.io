---
title: log_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - log_profiles
  - monitor
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
<tr><td><b>Name</b></td><td><code>log_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.log_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `storageAccountId` | `string` | the resource id of the storage account to which you would like to send the Activity Log. |
| `locations` | `array` | List of regions for which Activity Log events should be stored or streamed. It is a comma separated list of valid ARM locations including the 'global' location. |
| `type` | `string` | Azure resource type |
| `categories` | `array` | the categories of the logs. These categories are created as is convenient to the user. Some values are: 'Write', 'Delete', and/or 'Action.' |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `serviceBusRuleId` | `string` | The service bus rule ID of the service bus namespace in which you would like to have Event Hubs created for streaming the Activity Log. The rule ID is of the format: '{service bus resource ID}/authorizationrules/{key name}'. |
| `retentionPolicy` | `object` | Specifies the retention policy for the log. |
| `location` | `string` | Resource location |
| `tags` | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LogProfiles_List` | `SELECT` | `subscriptionId` | List the log profiles. |
| `LogProfiles_CreateOrUpdate` | `INSERT` | `logProfileName, subscriptionId` | Create or update a log profile in Azure Monitoring REST API. |
| `LogProfiles_Delete` | `DELETE` | `logProfileName, subscriptionId` | Deletes the log profile. |
| `LogProfiles_Get` | `EXEC` | `logProfileName, subscriptionId` | Gets the log profile. |
| `LogProfiles_Update` | `EXEC` | `logProfileName, subscriptionId` | Updates an existing LogProfilesResource. To update other fields use the CreateOrUpdate method. |
