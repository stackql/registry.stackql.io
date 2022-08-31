---
title: web_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - web_tests
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
<tr><td><b>Name</b></td><td><code>web_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.application_insights.web_tests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource Id |
| `name` | `string` | Azure resource name |
| `Configuration` | `object` | An XML configuration specification for a WebTest. |
| `Description` | `string` | User defined description for this WebTest. |
| `location` | `string` | Resource location |
| `Request` | `object` | The collection of request properties |
| `ValidationRules` | `object` | The collection of validation rule properties |
| `RetryEnabled` | `boolean` | Allow for retries should this WebTest fail. |
| `provisioningState` | `string` | Current state of this component, whether or not is has been provisioned within the resource group it is defined. Users cannot change this value but are able to read from it. Values will include Succeeded, Deploying, Canceled, and Failed. |
| `type` | `string` | Azure resource type |
| `Timeout` | `integer` | Seconds until this WebTest will timeout and fail. Default value is 30. |
| `Frequency` | `integer` | Interval in seconds between test runs for this WebTest. Default value is 300. |
| `Kind` | `string` | The kind of web test this is, valid choices are ping, multistep and standard. |
| `kind` | `string` | The kind of WebTest that this web test watches. Choices are ping, multistep and standard. |
| `tags` | `` | Resource tags |
| `SyntheticMonitorId` | `string` | Unique ID of this WebTest. This is typically the same value as the Name field. |
| `Locations` | `array` | A list of where to physically run the tests from to give global coverage for accessibility of your application. |
| `Name` | `string` | User defined name if this WebTest. |
| `Enabled` | `boolean` | Is the test actively being monitored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebTests_List` | `SELECT` | `subscriptionId` | Get all Application Insights web test definitions for the specified subscription. |
| `WebTests_ListByComponent` | `SELECT` | `componentName, resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified component. |
| `WebTests_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all Application Insights web tests defined for the specified resource group. |
| `WebTests_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, webTestName` | Creates or updates an Application Insights web test definition. |
| `WebTests_Delete` | `DELETE` | `resourceGroupName, subscriptionId, webTestName` | Deletes an Application Insights web test. |
| `WebTests_Get` | `EXEC` | `resourceGroupName, subscriptionId, webTestName` | Get a specific Application Insights web test definition. |
| `WebTests_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, webTestName` | Updates the tags associated with an Application Insights web test. |
