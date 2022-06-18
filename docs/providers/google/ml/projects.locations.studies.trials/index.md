---
title: projects.locations.studies.trials
hide_title: false
hide_table_of_contents: false
keywords:
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
<tr><td><b>Name</b></td><td><code>projects.locations.studies.trials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.ml.projects.locations.studies.trials</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `locationsId, projectsId, studiesId, trialsId` | Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service. |
| `list` | `SELECT` | `locationsId, projectsId, studiesId` | Lists the trials associated with a study. |
| `create` | `INSERT` | `locationsId, projectsId, studiesId` | Adds a user provided trial to a study. |
| `delete` | `DELETE` | `locationsId, projectsId, studiesId, trialsId` | Deletes a model version. Each model can have multiple versions deployed and in use at any given time. Use this method to remove a single version. Note: You cannot delete the version that is set as the default version of the model unless it is the only remaining version. |
| `addMeasurement` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Adds a measurement of the objective metrics to a trial. This measurement is assumed to have been taken before the trial is complete. |
| `checkEarlyStoppingState` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Checks whether a trial should stop or not. Returns a long-running operation. When the operation is successful, it will contain a CheckTrialEarlyStoppingStateResponse. |
| `complete` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Marks a trial as complete. |
| `listOptimalTrials` | `EXEC` | `locationsId, projectsId, studiesId` | Lists the pareto-optimal trials for multi-objective study or the optimal trials for single-objective study. The definition of pareto-optimal can be checked in wiki page. https://en.wikipedia.org/wiki/Pareto_efficiency |
| `stop` | `EXEC` | `locationsId, projectsId, studiesId, trialsId` | Stops a trial. |
| `suggest` | `EXEC` | `locationsId, projectsId, studiesId` | Adds one or more trials to a study, with parameter values suggested by AI Platform Vizier. Returns a long-running operation associated with the generation of trial suggestions. When this long-running operation succeeds, it will contain a SuggestTrialsResponse. |
