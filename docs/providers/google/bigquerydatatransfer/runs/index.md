---
title: runs
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - runs
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigquerydatatransfer.runs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the transfer run. Transfer run names have the form `projects/{project_id}/locations/{location}/transferConfigs/{config_id}/runs/{run_id}`. The name is ignored when creating a transfer run. |
| `errorStatus` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `dataSourceId` | `string` | Output only. Data source id. |
| `endTime` | `string` | Output only. Time when transfer run ended. Parameter ignored by server for input requests. |
| `emailPreferences` | `object` | Represents preferences for sending email notifications for transfer run events. |
| `destinationDatasetId` | `string` | Output only. The BigQuery target dataset id. |
| `scheduleTime` | `string` | Minimum time after which a transfer run can be started. |
| `startTime` | `string` | Output only. Time when transfer run was started. Parameter ignored by server for input requests. |
| `params` | `object` | Output only. Parameters specific to each data source. For more information see the bq tab in the 'Setting up a data transfer' section for each data source. For example the parameters for Cloud Storage transfers are listed here: https://cloud.google.com/bigquery-transfer/docs/cloud-storage-transfer#bq |
| `schedule` | `string` | Output only. Describes the schedule of this transfer run if it was created as part of a regular schedule. For batch transfer runs that are scheduled manually, this is empty. NOTE: the system might choose to delay the schedule depending on the current load, so `schedule_time` doesn't always match this. |
| `notificationPubsubTopic` | `string` | Output only. Pub/Sub topic where a notification will be sent after this transfer run finishes. The format for specifying a pubsub topic is: `projects/{project}/topics/{topic}` |
| `runTime` | `string` | For batch transfer runs, specifies the date and time of the data should be ingested. |
| `state` | `string` | Data transfer run state. Ignored for input requests. |
| `updateTime` | `string` | Output only. Last time the data transfer run state was updated. |
| `userId` | `string` | Deprecated. Unique ID of the user on whose behalf transfer is done. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_transferConfigs_runs_get` | `SELECT` | `name` | Returns information about the particular transfer run. |
| `projects_locations_transferConfigs_runs_list` | `SELECT` | `parent` | Returns information about running and completed transfer runs. |
| `projects_transferConfigs_runs_get` | `SELECT` | `name` | Returns information about the particular transfer run. |
| `projects_transferConfigs_runs_list` | `SELECT` | `parent` | Returns information about running and completed transfer runs. |
| `projects_locations_transferConfigs_runs_delete` | `DELETE` | `name` | Deletes the specified transfer run. |
| `projects_transferConfigs_runs_delete` | `DELETE` | `name` | Deletes the specified transfer run. |
