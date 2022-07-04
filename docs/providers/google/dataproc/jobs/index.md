---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `pigJob` | `object` | A Dataproc job for running Apache Pig (https://pig.apache.org/) queries on YARN. |
| `sparkJob` | `object` | A Dataproc job for running Apache Spark (https://spark.apache.org/) applications on YARN. |
| `placement` | `object` | Dataproc job config. |
| `sparkSqlJob` | `object` | A Dataproc job for running Apache Spark SQL (https://spark.apache.org/sql/) queries. |
| `driverControlFilesUri` | `string` | Output only. If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri. |
| `status` | `object` | Dataproc job status. |
| `pysparkJob` | `object` | A Dataproc job for running Apache PySpark (https://spark.apache.org/docs/0.9.0/python-programming-guide.html) applications on YARN. |
| `jobUuid` | `string` | Output only. A UUID that uniquely identifies a job within the project over time. This is in contrast to a user-settable reference.job_id that may be reused over time. |
| `done` | `boolean` | Output only. Indicates whether the job is completed. If the value is false, the job is still in progress. If true, the job is completed, and status.state field will indicate if it was successful, failed, or cancelled. |
| `labels` | `object` | Optional. The labels to associate with this job. Label keys must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty, but, if present, must contain 1 to 63 characters, and must conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). No more than 32 labels can be associated with a job. |
| `hadoopJob` | `object` | A Dataproc job for running Apache Hadoop MapReduce (https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html) jobs on Apache Hadoop YARN (https://hadoop.apache.org/docs/r2.7.1/hadoop-yarn/hadoop-yarn-site/YARN.html). |
| `yarnApplications` | `array` | Output only. The collection of YARN applications spun up by this job.Beta Feature: This report is available for testing purposes only. It may be changed before final release. |
| `scheduling` | `object` | Job scheduling options. |
| `statusHistory` | `array` | Output only. The previous job status. |
| `sparkRJob` | `object` | A Dataproc job for running Apache SparkR (https://spark.apache.org/docs/latest/sparkr.html) applications on YARN. |
| `prestoJob` | `object` | A Dataproc job for running Presto (https://prestosql.io/) queries. IMPORTANT: The Dataproc Presto Optional Component (https://cloud.google.com/dataproc/docs/concepts/components/presto) must be enabled when the cluster is created to submit a Presto job to the cluster. |
| `reference` | `object` | Encapsulates the full scoping used to reference a job. |
| `hiveJob` | `object` | A Dataproc job for running Apache Hive (https://hive.apache.org/) queries on YARN. |
| `driverOutputResourceUri` | `string` | Output only. A URI pointing to the location of the stdout of the job's driver program. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_regions_jobs_get` | `SELECT` | `jobId, projectId, region` | Gets the resource representation for a job in a project. |
| `projects_regions_jobs_list` | `SELECT` | `projectId, region` | Lists regions/{region}/jobs in a project. |
| `projects_regions_jobs_delete` | `DELETE` | `jobId, projectId, region` | Deletes the job from the project. If the job is active, the delete fails, and the response returns FAILED_PRECONDITION. |
| `projects_regions_jobs_cancel` | `EXEC` | `jobId, projectId, region` | Starts a job cancellation request. To access the job resource after cancellation, call regions/{region}/jobs.list (https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/list) or regions/{region}/jobs.get (https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/get). |
| `projects_regions_jobs_patch` | `EXEC` | `jobId, projectId, region` | Updates a job in a project. |
| `projects_regions_jobs_submit` | `EXEC` | `projectId, region` | Submits a job to a cluster. |
| `projects_regions_jobs_submitAsOperation` | `EXEC` | `projectId, region` | Submits job to a cluster. |