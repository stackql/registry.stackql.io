---
title: trials
hide_title: false
hide_table_of_contents: false
keywords:
  - googlecloudplatform
  - gcp
  - google
  - trials
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
<tr><td><b>Name</b></td><td><code>trials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.trials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the trial assigned by the service. |
| `startTime` | `string` | Output only. Time at which the trial was started. |
| `measurements` | `array` | A list of measurements that are strictly lexicographically ordered by their induced tuples (steps, elapsed_time). These are used for early stopping computations. |
| `endTime` | `string` | Output only. Time at which the trial's status changed to COMPLETED. |
| `state` | `string` | The detailed state of a trial. |
| `clientId` | `string` | Output only. The identifier of the client that originally requested this trial. |
| `finalMeasurement` | `object` | A message representing a measurement. |
| `infeasibleReason` | `string` | Output only. A human readable string describing why the trial is infeasible. This should only be set if trial_infeasible is true. |
| `trialInfeasible` | `boolean` | Output only. If true, the parameters in this trial are not attempted again. |
| `parameters` | `array` | The parameters of the trial. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_studies_trials_get` | `SELECT` | `name` | Gets a trial. |
| `projects_locations_studies_trials_list` | `SELECT` | `parent` | Lists the trials associated with a study. |
| `projects_locations_studies_trials_create` | `INSERT` | `parent` | Adds a user provided trial to a study. |
| `projects_locations_studies_trials_delete` | `DELETE` | `name` | Deletes a trial. |
| `projects_locations_studies_trials_checkEarlyStoppingState` | `EXEC` | `name` | Checks whether a trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse. |
| `projects_locations_studies_trials_complete` | `EXEC` | `name` | Marks a trial as complete. |
| `projects_locations_studies_trials_stop` | `EXEC` | `name` | Stops a trial. |
| `projects_locations_studies_trials_suggest` | `EXEC` | `parent` | Adds one or more trials to a study, with parameter values suggested by AI Platform Vizier. Returns a long-running operation associated with the generation of trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse. |
