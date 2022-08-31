---
title: streaming_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_jobs
  - stream_analytics
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
<tr><td><b>Name</b></td><td><code>streaming_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.stream_analytics.streaming_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `provisioningState` | `string` | Describes the provisioning status of the streaming job. |
| `jobType` | `string` | Describes the type of the job. Valid modes are `Cloud` and 'Edge'. |
| `outputs` | `array` | A list of one or more outputs for the streaming job. The name property for each output is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual output. |
| `tags` | `object` | Resource tags. |
| `eventsLateArrivalMaxDelayInSeconds` | `integer` | The maximum tolerable delay in seconds where events arriving late could be included.  Supported range is -1 to 1814399 (20.23:59:59 days) and -1 is used to specify wait indefinitely. If the property is absent, it is interpreted to have a value of -1. |
| `contentStoragePolicy` | `string` | Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this requires the user to also specify jobStorageAccount property. . |
| `transformation` | `object` | A transformation object, containing all information associated with the named transformation. All transformations are contained under a streaming job. |
| `jobId` | `string` | A GUID uniquely identifying the streaming job. This GUID is generated upon creation of the streaming job. |
| `etag` | `string` | The current entity tag for the streaming job. This is an opaque string. You can use it to detect whether the resource has changed between requests. You can also use it in the If-Match or If-None-Match headers for write operations for optimistic concurrency. |
| `outputErrorPolicy` | `string` | Indicates the policy to apply to events that arrive at the output and cannot be written to the external storage due to being malformed (missing column values, column values of wrong type or size). |
| `location` | `string` | The geo-location where the resource lives |
| `cluster` | `object` | The properties associated with a Stream Analytics cluster. |
| `createdDate` | `string` | Value is an ISO-8601 formatted UTC timestamp indicating when the streaming job was created. |
| `inputs` | `array` | A list of one or more inputs to the streaming job. The name property for each input is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual input. |
| `sku` | `object` | The properties that are associated with a SKU. |
| `functions` | `array` | A list of one or more functions for the streaming job. The name property for each function is required when specifying this property in a PUT request. This property cannot be modify via a PATCH operation. You must use the PATCH API available for the individual transformation. |
| `eventsOutOfOrderMaxDelayInSeconds` | `integer` | The maximum tolerable delay in seconds where out-of-order events can be adjusted to be back in order. |
| `compatibilityLevel` | `string` | Controls certain runtime behaviors of the streaming job. |
| `identity` | `object` | Describes how identity is verified |
| `lastOutputEventTime` | `string` | Value is either an ISO-8601 formatted timestamp indicating the last output event time of the streaming job or null indicating that output has not yet been produced. In case of multiple outputs or multiple streams, this shows the latest value in that set. |
| `jobStorageAccount` | `object` | The properties that are associated with an Azure Storage account with MSI |
| `outputStartTime` | `string` | Value is either an ISO-8601 formatted time stamp that indicates the starting point of the output event stream, or null to indicate that the output event stream will start whenever the streaming job is started. This property must have a value if outputStartMode is set to CustomTime. |
| `dataLocale` | `string` | The data locale of the stream analytics job. Value should be the name of a supported .NET Culture from the set https://msdn.microsoft.com/en-us/library/system.globalization.culturetypes(v=vs.110).aspx. Defaults to 'en-US' if none specified. |
| `outputStartMode` | `string` | Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting point of the output event stream should start whenever the job is started, start at a custom user time stamp specified via the outputStartTime property, or start from the last event output time. |
| `eventsOutOfOrderPolicy` | `string` | Indicates the policy to apply to events that arrive out of order in the input event stream. |
| `jobState` | `string` | Describes the state of the streaming job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StreamingJobs_List` | `SELECT` | `subscriptionId` | Lists all of the streaming jobs in the given subscription. |
| `StreamingJobs_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the streaming jobs in the specified resource group. |
| `StreamingJobs_CreateOrReplace` | `INSERT` | `jobName, resourceGroupName, subscriptionId` | Creates a streaming job or replaces an already existing streaming job. |
| `StreamingJobs_Delete` | `DELETE` | `jobName, resourceGroupName, subscriptionId` | Deletes a streaming job. |
| `StreamingJobs_Get` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Gets details about the specified streaming job. |
| `StreamingJobs_Scale` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Scales a streaming job when the job is running. |
| `StreamingJobs_Start` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Starts a streaming job. Once a job is started it will start processing input events and produce output. |
| `StreamingJobs_Stop` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Stops a running streaming job. This will cause a running streaming job to stop processing input events and producing output. |
| `StreamingJobs_Update` | `EXEC` | `jobName, resourceGroupName, subscriptionId` | Updates an existing streaming job. This can be used to partially update (ie. update one or two properties) a streaming job without affecting the rest the job definition. |
