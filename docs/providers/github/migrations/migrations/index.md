---
title: migrations
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
<tr><td><b>Name</b></td><td><code>github.migrations.migrations</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.migrations.migrations</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `url` | `string` |  |
| `archive_url` | `string` |  |
| `updated_at` | `string` |  |
| `repositories` | `array` |  |
| `guid` | `string` |  |
| `state` | `string` |  |
| `lock_repositories` | `boolean` |  |
| `exclude_attachments` | `boolean` |  |
| `exclude_owner_projects` | `boolean` |  |
| `exclude_releases` | `boolean` |  |
| `exclude_git_data` | `boolean` |  |
| `created_at` | `string` |  |
| `exclude` | `array` |  |
| `owner` | `object` | Simple User |
| `exclude_metadata` | `boolean` |  |
| `node_id` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_status_for_authenticated_user` | `migration_id` | Fetches a single user migration. The response includes the `state` of the migration, which can be one of the following values:<br /><br />*   `pending` - the migration hasn't started yet.<br />*   `exporting` - the migration is in progress.<br />*   `exported` - the migration finished successfully.<br />*   `failed` - the migration failed.<br /><br />Once the migration has been `exported` you can [download the migration archive](https://docs.github.com/rest/reference/migrations#download-a-user-migration-archive). | SELECT |
| `get_status_for_org` | `migration_id, org` | Fetches the status of a migration.<br /><br />The `state` of a migration can be one of the following values:<br /><br />*   `pending`, which means the migration hasn't started yet.<br />*   `exporting`, which means the migration is in progress.<br />*   `exported`, which means the migration finished successfully.<br />*   `failed`, which means the migration failed. | SELECT |
| `list_for_authenticated_user` | `` | Lists all migrations a user has started. | SELECT |
| `list_for_org` | `org` | Lists the most recent migrations. | SELECT |
| `start_for_authenticated_user` | `data__repositories` | Initiates the generation of a user migration archive. | EXEC |
| `start_for_org` | `org, data__repositories` | Initiates the generation of a migration archive. | EXEC |
