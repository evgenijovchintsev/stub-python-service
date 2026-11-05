{{- define "mc-e2e-stub.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "mc-e2e-stub.fullname" -}}
{{- if .Values.fullnameOverride -}}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" -}}
{{- else -}}
{{- printf "%s-%s" .Release.Name (include "mc-e2e-stub.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}
{{- end -}}
