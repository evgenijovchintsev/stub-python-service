# stub-python-service
Python Service for testing MergeCrafted agentic system

## Helm chart (`chart/`)

Minimal NGINX chart (Deployment + Service) consumed by MergeCrafted E2E
deployment-pipeline runs: rendered with `helm template`, diffed with
`helm diff upgrade`, then installed into a disposable `mc-e2e-*` namespace.
The default image comes from the Harbor mirror — see `chart/values.yaml`.
