# Talend Management Console Public API Bash client

## Overview
This is a Bash client script for accessing Talend Management Console Public API service.

The script uses cURL underneath for making all REST calls.

## Usage

```shell
# Make sure the script has executable rights
$ chmod u+x tmc-cli

# Print the list of operations available on the service
$ ./tmc-cli -h

# Print the service description
$ ./tmc-cli --about

# Print detailed information about specific operation
$ ./tmc-cli <operationId> -h

# Make GET request
./tmc-cli --host http://<hostname>:<port> --accept xml <operationId> <queryParam1>=<value1> <header_key1>:<header_value2>

# Make GET request using arbitrary curl options (must be passed before <operationId>) to an SSL service using username:password
tmc-cli -k -sS --tlsv1.2 --host https://<hostname> -u <user>:<password> --accept xml <operationId> <queryParam1>=<value1> <header_key1>:<header_value2>

# Make POST request
$ echo '<body_content>' | tmc-cli --host <hostname> --content-type json <operationId> -

# Make POST request with simple JSON content, e.g.:
# {
#   "key1": "value1",
#   "key2": "value2",
#   "key3": 23
# }
$ echo '<body_content>' | tmc-cli --host <hostname> --content-type json <operationId> key1==value1 key2=value2 key3:=23 -

# Preview the cURL command without actually executing it
$ tmc-cli --host http://<hostname>:<port> --dry-run <operationid>

```

## Docker image
You can easily create a Docker image containing a preconfigured environment
for using the REST Bash client including working autocompletion and short
welcome message with basic instructions, using the generated Dockerfile:

```shell
docker build -t my-rest-client .
docker run -it my-rest-client
```

By default you will be logged into a Zsh environment which has much more
advanced auto completion, but you can switch to Bash, where basic autocompletion
is also available.

## Shell completion

### Bash
The generated bash-completion script can be either directly loaded to the current Bash session using:

```shell
source tmc-cli.bash-completion
```

Alternatively, the script can be copied to the `/etc/bash-completion.d` (or on OSX with Homebrew to `/usr/local/etc/bash-completion.d`):

```shell
sudo cp tmc-cli.bash-completion /etc/bash-completion.d/tmc-cli
```

#### OS X
On OSX you might need to install bash-completion using Homebrew:
```shell
brew install bash-completion
```
and add the following to the `~/.bashrc`:

```shell
if [ -f $(brew --prefix)/etc/bash_completion ]; then
  . $(brew --prefix)/etc/bash_completion
fi
```

### Zsh
In Zsh, the generated `_tmc-cli` Zsh completion file must be copied to one of the folders under `$FPATH` variable.


## Documentation for API Endpoints

All URIs are relative to */tmc/v2.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ArtifactsApi* | [**getArtifact**](docs/ArtifactsApi.md#getartifact) | **GET** /artifacts/{id} | Get Artifact by id
*ArtifactsApi* | [**getArtifactOfVersion**](docs/ArtifactsApi.md#getartifactofversion) | **GET** /artifacts/{id}/versions/{version} | Get Artifact of a specified version
*ConfigurationApi* | [**getConnection**](docs/ConfigurationApi.md#getconnection) | **GET** /connections/{id} | Get Connection by id
*ConfigurationApi* | [**getResource**](docs/ConfigurationApi.md#getresource) | **GET** /resources/{id} | Get Resource by id
*ExecutionsApi* | [**execute**](docs/ExecutionsApi.md#execute) | **POST** /executions | Execute Task
*ExecutionsApi* | [**getExecutionStatus**](docs/ExecutionsApi.md#getexecutionstatus) | **GET** /executions/{id} | Get Task execution status
*ExecutionsApi* | [**stopExecution**](docs/ExecutionsApi.md#stopexecution) | **DELETE** /executions/{id} | Terminate Task execution
*PlansExecutablesApi* | [**configurePlanExecution**](docs/PlansExecutablesApi.md#configureplanexecution) | **PUT** /executables/plans/{id}/run-config | Configure Plan execution
*PlansExecutablesApi* | [**createPlan**](docs/PlansExecutablesApi.md#createplan) | **POST** /executables/plans | Create Plan
*PlansExecutablesApi* | [**getAvailablePlans**](docs/PlansExecutablesApi.md#getavailableplans) | **GET** /executables/plans | Get available Plans
*PlansExecutablesApi* | [**getExecutableDetails**](docs/PlansExecutablesApi.md#getexecutabledetails) | **GET** /executables/plans/{id} | Get Plan details
*PlansExecutablesApi* | [**getPlanConfiguration**](docs/PlansExecutablesApi.md#getplanconfiguration) | **GET** /executables/plans/{id}/run-config | Get Plan configuration
*PlansExecutionsApi* | [**execute**](docs/PlansExecutionsApi.md#execute) | **POST** /executions/plans | Execute Plan
*PlansExecutionsApi* | [**getExecutionStatus**](docs/PlansExecutionsApi.md#getexecutionstatus) | **GET** /executions/plans/{id} | Get Plan execution status
*PromotionsExecutablesApi* | [**getExecutableDetails**](docs/PromotionsExecutablesApi.md#getexecutabledetails) | **GET** /executables/promotions/{id} | Get Promotion details
*PromotionsExecutablesApi* | [**getExecutablesAvailable**](docs/PromotionsExecutablesApi.md#getexecutablesavailable) | **GET** /executables/promotions | Get available Promotions
*PromotionsExecutionsApi* | [**execute**](docs/PromotionsExecutionsApi.md#execute) | **POST** /executions/promotions | Execute Promotion
*PromotionsExecutionsApi* | [**getExecutionStatus**](docs/PromotionsExecutionsApi.md#getexecutionstatus) | **GET** /executions/promotions/{id} | Get Promotion execution status
*RuntimeClustersApi* | [**addRemoteEngineToCluster**](docs/RuntimeClustersApi.md#addremoteenginetocluster) | **PUT** /runtimes/remote-engine-clusters/{clusterId}/engines/{engineId} | Add Remote Engine to Remote Engine Cluster
*RuntimeClustersApi* | [**createRemoteEngineCluster**](docs/RuntimeClustersApi.md#createremoteenginecluster) | **POST** /runtimes/remote-engine-clusters | Create Remote Engine Cluster
*RuntimeClustersApi* | [**deleteRemoteEngineCluster**](docs/RuntimeClustersApi.md#deleteremoteenginecluster) | **DELETE** /runtimes/remote-engine-clusters/{clusterId} | Delete Remote Engine Cluster by id
*RuntimeClustersApi* | [**getEngineClustersAvailable**](docs/RuntimeClustersApi.md#getengineclustersavailable) | **GET** /runtimes/remote-engine-clusters | Get all (available) Remote Engine Clusters
*RuntimeClustersApi* | [**getRemoteEngineCluster**](docs/RuntimeClustersApi.md#getremoteenginecluster) | **GET** /runtimes/remote-engine-clusters/{clusterId} | Get Remote Engine Cluster by id
*RuntimeClustersApi* | [**removeRemoteEngineFromCluster**](docs/RuntimeClustersApi.md#removeremoteenginefromcluster) | **DELETE** /runtimes/remote-engine-clusters/{clusterId}/engines/{engineId} | Remove Remote Engine from Remote Engine Cluster
*RuntimeEnginesApi* | [**createRemoteEngine**](docs/RuntimeEnginesApi.md#createremoteengine) | **POST** /runtimes/remote-engines | Create new Remote Engine
*RuntimeEnginesApi* | [**deleteRemoteEngine**](docs/RuntimeEnginesApi.md#deleteremoteengine) | **DELETE** /runtimes/remote-engines/{id} | Delete Remote Engine by id
*RuntimeEnginesApi* | [**getRemoteEngine**](docs/RuntimeEnginesApi.md#getremoteengine) | **GET** /runtimes/remote-engines/{id} | Get Remote Engine by id
*RuntimeEnginesApi* | [**getRemoteEngines**](docs/RuntimeEnginesApi.md#getremoteengines) | **GET** /runtimes/remote-engines | Get all (available) Remote Engines
*RuntimeEnginesApi* | [**unpairRemoteEngine**](docs/RuntimeEnginesApi.md#unpairremoteengine) | **DELETE** /runtimes/remote-engines/{id}/pairing | Unpair Remote Engine
*TasksApi* | [**configureTaskExecution**](docs/TasksApi.md#configuretaskexecution) | **PUT** /executables/tasks/{id}/run-config | Configure Task execution
*TasksApi* | [**createTask**](docs/TasksApi.md#createtask) | **POST** /executables/tasks | Create Task
*TasksApi* | [**getAvailableTasks**](docs/TasksApi.md#getavailabletasks) | **GET** /executables/tasks | Get available Tasks
*TasksApi* | [**getTask**](docs/TasksApi.md#gettask) | **GET** /executables/tasks/{id} | Get Task by id
*TasksApi* | [**getTaskConfiguration**](docs/TasksApi.md#gettaskconfiguration) | **GET** /executables/tasks/{id}/run-config | Get Task configuration
*WorkspacesApi* | [**getWorkspaces**](docs/WorkspacesApi.md#getworkspaces) | **GET** /workspaces | Get available Workspaces


## Documentation For Models

 - [AdvancedPromotionSpec](docs/AdvancedPromotionSpec.md)
 - [Artifact](docs/Artifact.md)
 - [ArtifactParameter](docs/ArtifactParameter.md)
 - [ArtifactRequest](docs/ArtifactRequest.md)
 - [ArtifactVersion](docs/ArtifactVersion.md)
 - [BaseArtifactVersion](docs/BaseArtifactVersion.md)
 - [BaseEngine](docs/BaseEngine.md)
 - [ClusterRequest](docs/ClusterRequest.md)
 - [DaySchedule](docs/DaySchedule.md)
 - [Engine](docs/Engine.md)
 - [EngineCluster](docs/EngineCluster.md)
 - [EngineDebug](docs/EngineDebug.md)
 - [EngineRequest](docs/EngineRequest.md)
 - [EnvironmentInfo](docs/EnvironmentInfo.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExecutableTask](docs/ExecutableTask.md)
 - [ExecutionFlow](docs/ExecutionFlow.md)
 - [ExecutionIdentifier](docs/ExecutionIdentifier.md)
 - [ExecutionStep](docs/ExecutionStep.md)
 - [JobExecutionStatus](docs/JobExecutionStatus.md)
 - [Message](docs/Message.md)
 - [Page](docs/Page.md)
 - [Plan](docs/Plan.md)
 - [PlanExecutableDetails](docs/PlanExecutableDetails.md)
 - [PlanExecutableTask](docs/PlanExecutableTask.md)
 - [PlanExecutionStatus](docs/PlanExecutionStatus.md)
 - [PlanRequest](docs/PlanRequest.md)
 - [PromotionArtifactExecutionInfo](docs/PromotionArtifactExecutionInfo.md)
 - [PromotionExecutableDetails](docs/PromotionExecutableDetails.md)
 - [PromotionExecutableInfo](docs/PromotionExecutableInfo.md)
 - [PromotionExecutableTask](docs/PromotionExecutableTask.md)
 - [PromotionExecutionInfo](docs/PromotionExecutionInfo.md)
 - [Report](docs/Report.md)
 - [Resource](docs/Resource.md)
 - [RunConfig](docs/RunConfig.md)
 - [RunConnection](docs/RunConnection.md)
 - [Runtime](docs/Runtime.md)
 - [Step](docs/Step.md)
 - [StepErrorHandler](docs/StepErrorHandler.md)
 - [Task](docs/Task.md)
 - [TaskRequest](docs/TaskRequest.md)
 - [TimeSchedule](docs/TimeSchedule.md)
 - [Trigger](docs/Trigger.md)
 - [Webhook](docs/Webhook.md)
 - [WorkspaceInfo](docs/WorkspaceInfo.md)
 - [WorkspacePromotionExecutionInfo](docs/WorkspacePromotionExecutionInfo.md)


## Documentation For Authorization


## Access Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## Basic Authentication

- **Type**: HTTP basic authentication

