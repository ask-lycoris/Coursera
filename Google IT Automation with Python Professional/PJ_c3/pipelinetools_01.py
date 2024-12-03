Argo CD
Tekton
Openshift
Gitops


Application Repository：
The application repository stores the source code, which the CI pipeline pulls for build and testing operations.	Components of DevOps Pipeline

Argo CD：
Argo CD is a powerful open-source continuous delivery tool specifically designed for Kubernetes environments.	GitOps with ArgoCD

CD Pipeline：
The CD pipeline mainly deploysdeploys the prepared artifacts into specific target environments. It ensures a smooth transition from development to production.	Components of DevOps Pipeline

Change Request Tool：
A change request tool manages and tracks system changes. It integrates with the pipeline to ensure documented and validated changes before deployment.	Components of DevOps Pipeline

CI Pipeline：
The CI pipeline validates, packages, and builds essential components, creating deployable artifacts like container images and helm charts. It ensures versioning and resource preparation.	Components of DevOps Pipeline

Continuous Compliance Pipeline：
This pipeline ensures that organizations maintain security and compliance standards throughout the deployment lifecycle of their applications and infrastructure.	Components of DevOps Pipeline

DevOps Insights：
DevOps Insights collects data from the CI pipeline, generating reports to identify bottlenecks and areas for improvement.	Components of DevOps Pipeline
DevOps Pipeline	A DevOps pipeline is a workflow that automates software delivery. It is a series of interconnected steps that enable efficient and consistent execution of tasks such as building, testing, deploying, and releasing software.	Components of DevOps Pipeline

Evidence Component：
An evidence component stores artifacts and documentation generated during pipeline execution for traceability and auditing.	Components of DevOps Pipeline
GitOps：
It is an operational framework that utilizes the best practices of DevOps, which are used for application development.	Introduction to GitOps
Inventory Component	The inventory component tracks deployed applications, dependencies, and infrastructure configurations, ensuring consistency and control over software deployments.	Components of DevOps Pipeline
Key Protect	Key Protect securely stores cryptographic keys and sensitive information, providing secure access during deployment.	Components of DevOps Pipeline
OpenShift Pipelines：
OpenShift Pipelines, provided by Red Hat OpenShift, is a cloud-native solution for continuous integration and continuous delivery (CI/CD). It relies on Kubernetes objects to automate deployments across various platforms.	CI/CD with OpenShift Pipelines

PipelineRun	A：
PipelineRun is a resource that represents the execution of a specific pipeline instance. It defines the runtime configuration and parameters for running a pipeline in OpenShift Pipelines.	CI/CD with OpenShift Pipelines

Resource	A resource represents an input or output artifact that is used by tasks within a pipeline. Resources in OpenShift Pipelines can include source code repositories, images, configuration files, secrets, or other artifacts.	CI/CD with OpenShift Pipelines
Secrets Manager	A secrets manager securely stores sensitive information and integrates it with the CI pipeline to provide authorized access during build and deployment.	Components of DevOps Pipeline
Security and Compliance Center	The security and compliance center enforces policies, conducting security scans, vulnerability assessments, and compliance checks.	Components of DevOps Pipeline
Slack Integration	Slack integration enables efficient communication by sending notifications and reports to the development team.	Components of DevOps Pipeline
SonarQube	SonarQube, a code quality management platform, performs static code analysis, measures code coverage, and assesses maintainability.	Components of DevOps Pipeline

TaskRun	A：
TaskRun is a resource representing the execution of a specific task instance within a pipeline. It is created based on a Task resource, which defines the steps and configuration for a particular task.	CI/CD with OpenShift Pipelines

Tekton：
This abstraction allows developers and operators to define and configure pipelines using higher-level constructs that are easier to understand and work with.	CI/CD with OpenShift Pipelines
