---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the experiment. Format: projects//locations//agents//environments//experiments/.. |
| `description` | `string` | The human-readable description of the experiment. |
| `result` | `object` | The inference result which includes an objective metric to optimize and the confidence interval. |
| `lastUpdateTime` | `string` | Last update time of this experiment. |
| `variantsHistory` | `array` | The history of updates to the experiment variants. |
| `rolloutState` | `object` | State of the auto-rollout process. |
| `endTime` | `string` | End time of this experiment. |
| `state` | `string` | The current state of the experiment. Transition triggered by Experiments.StartExperiment: DRAFT-&gt;RUNNING. Transition triggered by Experiments.CancelExperiment: DRAFT-&gt;DONE or RUNNING-&gt;DONE. |
| `rolloutConfig` | `object` | The configuration for auto rollout. |
| `definition` | `object` | Definition of the experiment. |
| `startTime` | `string` | Start time of this experiment. |
| `rolloutFailureReason` | `string` | The reason why rollout has failed. Should only be set when state is ROLLOUT_FAILED. |
| `displayName` | `string` | Required. The human-readable name of the experiment (unique in an environment). Limit of 64 characters. |
| `createTime` | `string` | Creation time of this experiment. |
| `experimentLength` | `string` | Maximum number of days to run the experiment/rollout. If auto-rollout is not enabled, default value and maximum will be 30 days. If auto-rollout is enabled, default value and maximum will be 6 days. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_environments_experiments_get` | `SELECT` | `name` | Retrieves the specified Experiment. |
| `projects_locations_agents_environments_experiments_list` | `SELECT` | `parent` | Returns the list of all experiments in the specified Environment. |
| `projects_locations_agents_environments_experiments_create` | `INSERT` | `parent` | Creates an Experiment in the specified Environment. |
| `projects_locations_agents_environments_experiments_delete` | `DELETE` | `name` | Deletes the specified Experiment. |
| `projects_locations_agents_environments_experiments_patch` | `EXEC` | `name` | Updates the specified Experiment. |
| `projects_locations_agents_environments_experiments_start` | `EXEC` | `name` | Starts the specified Experiment. This rpc only changes the state of experiment from PENDING to RUNNING. |
| `projects_locations_agents_environments_experiments_stop` | `EXEC` | `name` | Stops the specified Experiment. This rpc only changes the state of experiment from RUNNING to DONE. |
