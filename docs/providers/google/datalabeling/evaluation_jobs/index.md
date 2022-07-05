---
title: evaluation_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - evaluation_jobs
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
<tr><td><b>Name</b></td><td><code>evaluation_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datalabeling.evaluation_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. After you create a job, Data Labeling Service assigns a name to the job with the following format: "projects/{project_id}/evaluationJobs/ {evaluation_job_id}" |
| `description` | `string` | Required. Description of the job. The description can be up to 25,000 characters long. |
| `createTime` | `string` | Output only. Timestamp of when this evaluation job was created. |
| `evaluationJobConfig` | `object` | Configures specific details of how a continuous evaluation job works. Provide this configuration when you create an EvaluationJob. |
| `labelMissingGroundTruth` | `boolean` | Required. Whether you want Data Labeling Service to provide ground truth labels for prediction input. If you want the service to assign human labelers to annotate your data, set this to `true`. If you want to provide your own ground truth labels in the evaluation job's BigQuery table, set this to `false`. |
| `attempts` | `array` | Output only. Every time the evaluation job runs and an error occurs, the failed attempt is appended to this array. |
| `schedule` | `string` | Required. Describes the interval at which the job runs. This interval must be at least 1 day, and it is rounded to the nearest day. For example, if you specify a 50-hour interval, the job runs every 2 days. You can provide the schedule in [crontab format](https://cloud.google.com/scheduler/docs/configuring/cron-job-schedules) or in an [English-like format](https://cloud.google.com/appengine/docs/standard/python/config/cronref#schedule_format). Regardless of what you specify, the job will run at 10:00 AM UTC. Only the interval from this schedule is used, not the specific time of day. |
| `state` | `string` | Output only. Describes the current state of the job. |
| `annotationSpecSet` | `string` | Required. Name of the AnnotationSpecSet describing all the labels that your machine learning model outputs. You must create this resource before you create an evaluation job and provide its name in the following format: "projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}" |
| `modelVersion` | `string` | Required. The [AI Platform Prediction model version](https://cloud.google.com/ml-engine/docs/prediction-overview) to be evaluated. Prediction input and output is sampled from this model version. When creating an evaluation job, specify the model version in the following format: "projects/{project_id}/models/{model_name}/versions/{version_name}" There can only be one evaluation job per model version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_evaluationJobs_get` | `SELECT` | `name` | Gets an evaluation job by resource name. |
| `projects_evaluationJobs_list` | `SELECT` | `parent` | Lists all evaluation jobs within a project with possible filters. Pagination is supported. |
| `projects_evaluationJobs_create` | `INSERT` | `parent` | Creates an evaluation job. |
| `projects_evaluationJobs_delete` | `DELETE` | `name` | Stops and deletes an evaluation job. |
| `projects_evaluationJobs_patch` | `EXEC` | `name` | Updates an evaluation job. You can only update certain fields of the job's EvaluationJobConfig: `humanAnnotationConfig.instruction`, `exampleCount`, and `exampleSamplePercentage`. If you want to change any other aspect of the evaluation job, you must delete the job and create a new one. |
| `projects_evaluationJobs_pause` | `EXEC` | `name` | Pauses an evaluation job. Pausing an evaluation job that is already in a `PAUSED` state is a no-op. |
| `projects_evaluationJobs_resume` | `EXEC` | `name` | Resumes a paused evaluation job. A deleted evaluation job can't be resumed. Resuming a running or scheduled evaluation job is a no-op. |
