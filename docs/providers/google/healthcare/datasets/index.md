---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.healthcare.datasets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name of the dataset, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`. |
| `timeZone` | `string` | The default timezone used by this dataset. Must be a either a valid IANA time zone name such as "America/New_York" or empty, which defaults to UTC. This is used for parsing times in resources, such as HL7 messages, where no explicit timezone is specified. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_datasets_get` | `SELECT` | `name` | Gets any metadata associated with a dataset. |
| `projects_locations_datasets_list` | `SELECT` | `parent` | Lists the health datasets in the current project. |
| `projects_locations_datasets_create` | `INSERT` | `parent` | Creates a new health dataset. Results are returned through the Operation interface which returns either an `Operation.response` which contains a Dataset or `Operation.error`. The metadata field type is OperationMetadata. |
| `projects_locations_datasets_delete` | `DELETE` | `name` | Deletes the specified health dataset and all data contained in the dataset. Deleting a dataset does not affect the sources from which the dataset was imported (if any). |
| `projects_locations_datasets_deidentify` | `EXEC` | `sourceDataset` | Creates a new dataset containing de-identified data from the source dataset. The metadata field type is OperationMetadata. If the request is successful, the response field type is DeidentifySummary. If errors occur, error is set. The LRO result may still be successful if de-identification fails for some DICOM instances. The new de-identified dataset will not contain these failed resources. Failed resource totals are tracked in Operation.metadata. Error details are also logged to Cloud Logging. For more information, see [Viewing error logs in Cloud Logging](https://cloud.google.com/healthcare/docs/how-tos/logging). |
| `projects_locations_datasets_patch` | `EXEC` | `name` | Updates dataset metadata. |
