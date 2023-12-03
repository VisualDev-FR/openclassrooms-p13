docker build ^
-t tmenanteau/oc_lettings ^
--build-arg OC_LETTING_SENTRY_KEY="%OC_LETTING_SENTRY_KEY%" ^
--build-arg OC_LETTING_SK="%OC_LETTING_SK%" ^
.