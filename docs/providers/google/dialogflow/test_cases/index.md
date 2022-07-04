---
title: test_cases
hide_title: false
hide_table_of_contents: false
keywords:
  - test_cases
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
<tr><td><b>Name</b></td><td><code>test_cases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.test_cases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the test case. TestCases.CreateTestCase will populate the name automatically. Otherwise use format: `projects//locations//agents/ /testCases/`. |
| `notes` | `string` | Additional freeform notes about the test case. Limit of 400 characters. |
| `tags` | `array` | Tags are short descriptions that users may apply to test cases for organizational and filtering purposes. Each tag should start with "#" and has a limit of 30 characters. |
| `testCaseConversationTurns` | `array` | The conversation turns uttered when the test case was created, in chronological order. These include the canonical set of agent utterances that should occur when the agent is working properly. |
| `testConfig` | `object` | Represents configurations for a test case. |
| `creationTime` | `string` | Output only. When the test was created. |
| `displayName` | `string` | Required. The human-readable name of the test case, unique within the agent. Limit of 200 characters. |
| `lastTestResult` | `object` | Represents a result from running a test case in an agent environment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_testCases_get` | `SELECT` | `name` | Gets a test case. |
| `projects_locations_agents_testCases_list` | `SELECT` | `parent` | Fetches a list of test cases for a given agent. |
| `projects_locations_agents_testCases_create` | `INSERT` | `parent` | Creates a test case for the given agent. |
| `projects_locations_agents_testCases_batchDelete` | `DELETE` | `parent` | Batch deletes test cases. |
| `projects_locations_agents_testCases_batchRun` | `EXEC` | `parent` | Kicks off a batch run of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: BatchRunTestCasesMetadata - `response`: BatchRunTestCasesResponse |
| `projects_locations_agents_testCases_calculateCoverage` | `EXEC` | `agent` | Calculates the test coverage for an agent. |
| `projects_locations_agents_testCases_export` | `EXEC` | `parent` | Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: ExportTestCasesMetadata - `response`: ExportTestCasesResponse |
| `projects_locations_agents_testCases_import` | `EXEC` | `parent` | Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: ImportTestCasesMetadata - `response`: ImportTestCasesResponse |
| `projects_locations_agents_testCases_patch` | `EXEC` | `name` | Updates the specified test case. |
| `projects_locations_agents_testCases_run` | `EXEC` | `name` | Kicks off a test case run. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: RunTestCaseMetadata - `response`: RunTestCaseResponse |