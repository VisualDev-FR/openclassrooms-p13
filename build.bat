docker build ^
--tag tmenanteau/oc_lettings ^
--no-cache ^
--build-arg OC_LETTING_SENTRY_KEY="%OC_LETTING_SENTRY_KEY%" ^
--build-arg OC_LETTING_SK="%OC_LETTING_SK%" ^
.