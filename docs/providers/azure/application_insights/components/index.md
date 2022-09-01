---
title: components
hide_title: false
hide_table_of_contents: false
keywords:
  - components
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
<tr><td><b>Name</b></td><td><code>components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.components</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `ConnectionString` | `string` | Application Insights component connection string. |
| `RetentionInDays` | `integer` | Retention period in days. |
| `tags` | `` | Resource tags |
| `Request_Source` | `string` | Describes what tool created this Application Insights component. Customers using this API should set this to the default 'rest'. |
| `DisableIpMasking` | `boolean` | Disable IP masking. |
| `Name` | `string` | Application name. |
| `DisableLocalAuth` | `boolean` | Disable Non-AAD based Auth. |
| `etag` | `string` | Resource etag |
| `publicNetworkAccessForQuery` | `string` | The network access type for operating on the Application Insights Component. By default it is Enabled |
| `publicNetworkAccessForIngestion` | `string` | The network access type for operating on the Application Insights Component. By default it is Enabled |
| `IngestionMode` | `string` | Indicates the flow of the ingestion. |
| `kind` | `string` | The kind of application that this component refers to, used to customize UI. This value is a freeform string, values should typically be one of the following: web, ios, other, store, java, phone. |
| `location` | `string` | Resource location |
| `provisioningState` | `string` | Current state of this component: whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed. |
| `ApplicationId` | `string` | The unique ID of your application. This field mirrors the 'Name' field and cannot be changed. |
| `SamplingPercentage` | `number` | Percentage of the data produced by the application being monitored that is being sampled for Application Insights telemetry. |
| `ForceCustomerStorageForProfiler` | `boolean` | Force users to create their own storage account for profiler and debugger. |
| `HockeyAppId` | `string` | The unique application ID created when a new application is added to HockeyApp, used for communications with HockeyApp. |
| `Application_Type` | `string` | Type of application being monitored. |
| `type` | `string` | Azure resource type |
| `CreationDate` | `string` | Creation Date for the Application Insights component, in ISO 8601 format. |
| `Flow_Type` | `string` | Used by the Application Insights system to determine what kind of flow this component was created by. This is to be set to 'Bluefield' when creating/updating a component via the REST API. |
| `TenantId` | `string` | Azure Tenant Id. |
| `LaMigrationDate` | `string` | The date which the component got migrated to LA, in ISO 8601 format. |
| `AppId` | `string` | Application Insights Unique ID for your Application. |
| `PrivateLinkScopedResources` | `array` | List of linked private link scope resources. |
| `WorkspaceResourceId` | `string` | Resource Id of the log analytics workspace which the data will be ingested to. This property is required to create an application with this API version. Applications from older versions will not have this property. |
| `ImmediatePurgeDataOn30Days` | `boolean` | Purge data immediately after 30 days. |
| `HockeyAppToken` | `string` | Token used to authenticate communications with between Application Insights and HockeyApp. |
| `InstrumentationKey` | `string` | Application Insights Instrumentation key. A read-only value that applications can use to identify the destination for all telemetry sent to Azure Application Insights. This value will be supplied upon construction of each new Application Insights component. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Components_List` | `SELECT` | `subscriptionId` | Gets a list of all Application Insights components within a subscription. |
| `Components_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Application Insights components within a resource group. |
| `Components_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId, data__kind` | Creates (or updates) an Application Insights component. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation. |
| `Components_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes an Application Insights component. |
| `Components_Get` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns an Application Insights component. |
| `Components_GetPurgeStatus` | `EXEC` | `purgeId, resourceGroupName, resourceName, subscriptionId` | Get status for an ongoing purge operation. |
| `Components_Purge` | `EXEC` | `resourceGroupName, resourceName, subscriptionId, data__filters, data__table` | Purges data in an Application Insights component by a set of user-defined filters.<br /><br />In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.<br />Note: this operation is intended for Classic resources, for  workspace-based Application Insights resource please run purge operation (directly on the workspace)(https://docs.microsoft.com/en-us/rest/api/loganalytics/workspace-purge/purge) , scoped to specific resource id. |
| `Components_UpdateTags` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates an existing component's tags. To update other fields use the CreateOrUpdate method. |
